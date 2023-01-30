import inicializacion
import random
import ZDT3
import numpy as np
from crea_grafica import crea_pelicula


''' VARIABLES GLOBALES '''
R = 30 #numero de veces que se ejecuta el programa

N = 40 #numero de subproblemas e individuos
G = 250 #numero de generaciones
D = 30 #numero de variables/dimensiones

t = 50
T = int(N*t/100) #numero vecindad 

min_ = 0.0
max_ = 1.0

Pc = 0.5
''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''
''' FUNCIONES AUXILIARES '''

def crea_vector_mutante(v1,v2,v3): 
    res = [] #guardo operacion de resta de vectores v2-v3
    for s in range(0,D):
        aux = v1[s]+0.5*(v2[s]-v3[s])
        probabilidad = random.uniform(0.0,1.0)
        if(probabilidad<=1/D): aux = aux + np.random.normal(0,(1.0-0.0)/20)
        #comprobacion de rangos
        if(aux<0.0): aux = abs(aux)
        if(aux>1.0): aux = 1.0 - (aux - 1.0)
        res.append(aux)
    return res

def crea_vector_y(x,vector_mutante):
    random_sigma = random.randint(0,D) #se elige un elemento del vector mutante aleatoriamente para asegurar minimo una mutacion
    vector_y = []
    for i in range(0,D): #creamos vector en este bucle
        if(i==random_sigma): vector_y.append(vector_mutante[random_sigma])
        else:
            pc_aux = random.uniform(0,1) #si supera valor de Pc
            if(Pc>=pc_aux): vector_y.append(x[i])
            else: vector_y.append(vector_mutante[i])
    #for i in range(0,D): #aplicamos funcion de densidad de probabilidad de Gauss
    #    probabilidad = random.random()
    #    if(probabilidad<=1/D): 
    #        vector_y[i] = vector_y[i] + 1.0/20.0
    return vector_y
                               
def func_bool_actualiza_vecino_j(new_eval_z, eval_i_j, vector_landa_j, z):
    aux_1 = [vector_landa_j[0] * abs(new_eval_z[0]-z[0]), vector_landa_j[1] * abs(new_eval_z[1]-z[1])]
    max_1 = max(aux_1)
    
    aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
    max_2 = max(aux_2)
    
    if(max_1<=max_2): return 1
    else: return 0


if __name__ == "__main__":


        ''' NUMERO DE EJECUCIONES '''
    #for r in range(0,R):

        ''' INICIALIZACION '''
        items_inicializacion = inicializacion.inicializacion() #llamada a la funcion de inicializacion
        
        vector_landa = items_inicializacion[0] #vector landa
        vecindad_global = items_inicializacion[1] #vecindad para cada individuo // len = N , tam_vecindad = T
        random_vector = items_inicializacion[2] #vector random inicial: N individuos con D dimensiones
        #evaluaciones = items_inicializacion[3] #valores z(f1,f2) para cada individuo 
        ''' '''
        z = items_inicializacion[3] #vector z*
        x = random_vector #primera generacion de N individuos
        

        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_zdt3/salida_z_zdt3_10000_all.txt','w')    
        #f.close()




        ''' ITERACION '''
        cont = 0
        for g in range(0,G):
            for i in range(0,N):
                    
                vecindad_i = vecindad_global[i] #vecinos para el individuo i
                
                vector_mutante = crea_vector_mutante(x[random.choice(vecindad_i)],
                        x[random.choice(vecindad_i)], x[random.choice(vecindad_i)]) #vector mutante i para individuo i de D dimensiones
                
                vector_y = crea_vector_y(x[i],vector_mutante) #vector resultante de D dimensiones
                    
                new_eval_z = ZDT3.func(vector_y) #evaluamos f1 y f2 para el nuevo vector y
                
                if(new_eval_z[0]<z[0]): z[0] = new_eval_z[0]; 
                if(new_eval_z[1]<z[1]): z[1] = new_eval_z[1];   

                #sustituimos vector_y para cada vecino
                for j in range(0,T):
                    bool_actualiza_vecinos = func_bool_actualiza_vecino_j(new_eval_z, ZDT3.func(x[vecindad_i[j]]), vector_landa[vecindad_i[j]], z) #si devuelve 1: el vector_y mejora al vecino j
                    if(bool_actualiza_vecinos==1): x[vecindad_i[j]] = vector_y

            '''
            f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_zdt3/salida_z_zdt3_10000_all.txt','a')
            for h in range(0,N):
                res = ZDT3.func(x[h])
                f.write(str(res[0])+"    "+str(res[1])+"\n")
            f.close()

            '''
        #ESCRITURA EN ARCHIVOS DE TEXTO DE LAS SOLUCIONES
        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_zdt3/salida_z_zdt3_4000.txt','w')    
        '''
        f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_zdt3/salida_z_zdt3_10000.txt','w')
        for h in range(0,N):
            res = ZDT3.func(x[h])
            f.write(str(res[0])+"    "+str(res[1])+"\n")
        f.close()
        #print(x)
        '''
        #USO DE MATPLOTLIB        
        crea_pelicula(x)

    
    
    
    
    

    