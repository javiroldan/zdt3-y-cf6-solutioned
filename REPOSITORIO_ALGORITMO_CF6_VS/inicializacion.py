import main as _main
import CF6 as CF6
import random
from math import dist


''' FUNCIONES AUXILIARES '''

def crea_vector_landa(): #creación vector landa para cada subproblema (N individuos)
    vector_landa = []    
    for i in range(0,_main.N):
        vector_landa.append([_main.max_1 - ((i)/(_main.N-1)), _main.min_1 + ((i)/(_main.N-1))])
    return vector_landa

def vecinos_landa_mas_cercanos(vector_landa): #devuelve una lista que engloba los T vecinos mas cercanos para cada vecotr landa i
    vecinos_cercanos_global = []
    for i in range(0,_main.N):
        vecinos_cercanos_i = [] 
        landa_i = vector_landa[i]
        for j in range(0,_main.N): #bucle para calcular todas las distancias entre los vectores de forma euclídea
            aux_peso = dist(landa_i,vector_landa[j])
            vecinos_cercanos_i.append(aux_peso)
        vecinos_cercanos_i = vecindad(vecinos_cercanos_i) #llamada a función que te devuelve los T vecinos mas cercanos para un landa i específico
        vecinos_cercanos_global.append(vecinos_cercanos_i)
    return vecinos_cercanos_global
    
def vecindad(vecinos_cercanos_i):
    l = list(sorted(enumerate(vecinos_cercanos_i), key=lambda x: x[1])[0:_main.T]) #creo una lista enumerada ordenada con los T vecinos
    res = []
    for i in range(0,_main.T):
        #añado al vector resultado los T vecinos mas cercanos en una lista en forma de: item 1: corrdenadas / item 2: posicion / item 3: distancia euclidea
        #ejemplo de vector l --> [(0, 0.0), (1, 0.014142135623730958), (2, 0.028284271247461915), (3, 0.042426406871192875), (4, 0.05656854249492383), (5, 0.07071067811865478), (6, 0.08485281374238575), (7, 0.0989949493661167), (8, 0.11313708498984758), (9, 0.12727922061357852), (10, 0.1414213562373095), (11, 0.15556349186104046), (12, 0.16970562748477142), (13, 0.18384776310850237), (14, 0.19798989873223333), (15, 0.21213203435596428), (16, 0.22627416997969524), (17, 0.2404163056034262), (18, 0.25455844122715704), (19, 0.26870057685088805), (20, 0.282842712474619), (21, 0.2969848480983499), (22, 0.3111269837220809), (23, 0.3252691193458119), (24, 0.33941125496954283), (25, 0.3535533905932738), (26, 0.36769552621700474), (27, 0.3818376618407357), (28, 0.39597979746446665), (29, 0.4101219330881976)]
        res.append(l[i][0]) 
    return res

def crea_vector_random():
    res = []
    for i in range(0,_main.N):    
        res_aux = []
        res_aux.append(random.uniform(0,1))
        for j in range(1,_main.D1):
            res_aux.append(random.uniform(-2.0,2.0))
        res.append(res_aux)
    return res


''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


''' FUNCIÓN DE INICIALIZACIÓN '''


def inicializacion():
    
    ''' CREACIÓN DE VECTOR LANDA''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''
    vector_landa = crea_vector_landa()
    #print("\nEl vector landa de tamaño "+str(vector_landa.__len__())+" es:")
    #print(vector_landa)
    #print("\n\n")
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''

    ''' CALCULO DE VECINDAD PARA CADA VECTOR PESO(LANDA) ''' ''' ''' ''' ''' ''' '''
    vecindad_global = vecinos_landa_mas_cercanos(vector_landa)
    #print(vecindad_global[0]) #vecindad del vector landa i = 0
    #print(vecindad_global[0][0][0]) #valores del vector landa
    #print(vecindad_global[0][0][1]) #distancia euclidea desde/a cada vector
    #print(vecindad_global[0][1][2]) #indice donde se encuentra inicialmente en el vector landa
    #print(vecindad_global[0][1]) #las tres anteriores del segundo(primer) vector landa mas cercano al vector landa i = 0
    #for i in range(50,60):
    #    print("        Vector landa i = "+str(i)+", con los "+str(vecindad_global[i].__len__())+" vecinos mas cercanos")
    #    print(vecindad_global[i])
    #    print(("\n"))
    ''''''''''''''''''''''''''''''''''''''''''''''''''''''
    
    '''VECTOR SOLUCIÓN INICIAL (RANDOM) ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' 
    random_vector = crea_vector_random() #creación del vector random
    #print("\n\nVector Inicial Random de tamaño (N individuos): "+str(random_vector.__len__())+" :")
    #print(random_vector)
    #print("\n\nVector Random de individuo i = 0: "+str(random_vector[0].__len__())+" :")
    #print(random_vector[0])
    #print("\n")
    
    ''' EVALUACIONES '''
    evaluaciones = [] #para cada subproblema, calculo "fitness" y evaluo
    for i in range(0,_main.N):
        evaluaciones.append(CF6.func(random_vector[i])) #añado a evaluaciones, el valor de obj[0](f1) y obj[1](f2)
    
    obj_1 = min(evaluaciones, key = lambda x:x[0])
    obj_2 = min(evaluaciones, key = lambda x:x[1])
    #print("min obj[0]: "+str(obj_1))
    #print("min obj[1]: "+str(obj_2))
    
    ''' CREACIÓN DEL VECTOR Z '''
    z = [obj_1[0],obj_2[1]]
    #print(z)

    ''' VALOR DEVUELTO '''
    res = [vector_landa,vecindad_global,random_vector,z]
    return res


''' FIN INICIALIZACIÓN  ''' 
    
if __name__ == "__main__":
    inicializacion()
