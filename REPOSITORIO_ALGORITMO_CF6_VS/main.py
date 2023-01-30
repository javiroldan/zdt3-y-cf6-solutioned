import inicializacion as ini
import random
import CF6
import numpy as np
from crea_grafica import crea_pelicula


''' VARIABLES GLOBALES '''

R = 30 #numero de veces que se ejecuta el programa

N = 400 #numero de subproblemas e individuos
G = 25 #numero de generaciones
D1 = 4 #numero de variables/dimensiones
#D1 = 16 #numero de variables/dimensiones

t = 100
T = int(N*t/100) #numero vecindad 

min_1 = 0.0
max_1 = 1.0
min_2 = -2.0
max_2 = 2.0

Pc = 0.5 #definido para la funcion crea_vector_y()
FACTOR = 1

''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' ''' '''

def crea_vector_mutante(v1,v2,v3): 
    res = [] #valor devuelto del vector_mutante 
    #print(v1,v2,v3)
    
    #para elemento 0 del vector mutante:
    aux = v1[0]+0.5*(v2[0]-v3[0]) 
    probabilidad = random.uniform(0.0,1.0)
    if(probabilidad<=1/D1): aux = aux + np.random.normal(0,(1.0-0.0)/20)
    #comprobacion de los bordes: 0.0 - 1.0
    if(aux<0.0): aux = abs(aux)#;print(aux);print("AAA")
    if(aux>1.0): aux = 1.0-(aux-1.0)
    res.append(aux) #añado el primer elemento del nuevo vector en el rango 0.0 -  1.0

    #para elemento resto de elementos vector mutante:
    for s in range(1,D1):
        aux = v1[s]+0.5*(v2[s]-v3[s])
        probabilidad = random.uniform(0.0,1.0)
        if(probabilidad<=1/D1): aux = aux + np.random.normal(0,(2.0- -2.0)/20) #aplicacion de la normal
        #comprobacion de los bordes: -2.0-2.0
        if(aux<-2.0): aux = -2.0 + (aux - -2.0)
        if(aux>2.0): aux = 2.0 - (aux - 2.0)
        res.append(aux)

    return res

def crea_vector_y(x,vector_mutante):
    random_sigma = random.randint(0,D1-1) #se elige un elemento del vector mutante aleatoriamente para asegurar minimo una mutacion
    vector_y = []
    for i in range(0,D1): #creamos vector en este bucle
        if(i==random_sigma): vector_y.append(vector_mutante[random_sigma])
        else:
            pc_aux = random.uniform(0.0,1.0) #si supera valor de Pc
            if(Pc>=pc_aux): vector_y.append(x[i])
            else: vector_y.append(vector_mutante[i])
    return vector_y


def func_bool_actualiza_vecino_j_4D(new_eval, eval_i_j, vector_landa_j, z, j, i):
    
    if(new_eval[2]>=0 and new_eval[3]>=0): #nueva_evaluacion cumple ambas restriccionnes
        if(eval_i_j[2]>=0 and eval_i_j[3]>=0): #eval_vecino cumple ambas restricciones
            ###se cumplen restricciones, evaluacion de actualizacion de vecinos normal:
            aux_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
            aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
            if(max(aux_1)<max(aux_2)): return 1
            else: return 0
            
        else: return 1 #nueva_eval mejora a eval_i_j por restricciones
    

    else:  #nueva_evaluacion no cumple ambas restriccionnes
        if(new_eval[2]<0 and new_eval[3]<0):  #nueva_evaluacion no cumple ninguna restriccion
            if(eval_i_j[2]<0 and eval_i_j[3]<0):  #eval_vecino no cumple ninguna restriccion
                #r2 = eval_i_j[3]
                #COMPARACIONES: NINGUNO CUMPLE NINGUNA RESTRICCION
                #aux_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
                #aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
                #max_1 = max(aux_1)
                #max_2 = max(aux_2)
                ##################################################
                # Devuelvo la suma de ambas restricciones
                aux_1 = new_eval[2] + new_eval[3]
                aux_2 = eval_i_j[2] + eval_i_j[3]
                if(aux_1 >= aux_2): return 1
                else: return 0 
                
            else: return 0 #para eval_i_j: cumple una o mas restricciones
                
        else: #nueva_evaluacion cumple una unica restricciones
            if(eval_i_j[2]>=0 and eval_i_j[3]>=0): return 0 #si evaluacion vecino cumple ambas y nueva_eval solo cumple una
            else:
                if(eval_i_j[2]<0 and eval_i_j[3]<0):return 1  
                #else: return 0
                else: #ambas cumplen una unica restriccion
                    aux_1 = [new_eval[2],new_eval[3]]
                    aux_2 = [eval_i_j[2],eval_i_j[3]]
                    if(min(aux_1) >= min(aux_2)): return 1
                    else: return 0 
    



               
def func_bool_actualiza_vecino_j(new_eval, eval_i_j, vector_landa_j, z, j, i):
    
    '''
    if(new_eval[2]>=0 and new_eval[3]>=0): 
        #CASO 1: AMBOS CUMPLEN RESTRICCIONES
        if(eval_i_j[2]>=0 and eval_i_j[3]>=0): 
            aux_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
            aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
            if(max(aux_1)<max(aux_2)): return 1
        #CASO 2: NEW_EVAL CUMPLE RESTRICCIONES Y EVAL_I_J NO LAS CUMPLE
        else: 
            if(j==i): return 1 #solo devuelvo 1 si se actualiza a si mismo new_eval
    else: #new_eval no cunple restricciones
        if(eval_i_j[2]>=0 and eval_i_j[3]>=0): return 0
        else:
            #if(j==i): 
                aux_1 = abs(new_eval[2] + new_eval[3])
                aux_2 = abs(eval_i_j[2] + eval_i_j[3])
                if(aux_1 >= aux_2): return 1
                else: return 0 
# res = (eval_i_j - eval_i_j)
    '''
    
    if(new_eval[2]<0 and new_eval[3]<0):
        aux_1 = abs(new_eval[2] + new_eval[3])*FACTOR
    else:
        if(new_eval[2]<0 or new_eval[3]<0):
            if(new_eval[2]<0):
                aux_1 = abs(new_eval[2])*FACTOR
            else: aux_1 = abs(new_eval[3])*FACTOR
        else: aux_1 = 0
    
    
    if(eval_i_j[2]<0 and eval_i_j[3]<0):
        aux_2 = abs(eval_i_j[2] + eval_i_j[3])*FACTOR
    else:
        if(eval_i_j[2]<0 or eval_i_j[3]<0):
            if(eval_i_j[2]<0):
                aux_2 = abs(eval_i_j[2])*FACTOR
            else: aux_2 = abs(eval_i_j[3])*FACTOR
        else: aux_2 = 0


    if(aux_1==0 and aux_2==0):
        res_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
        res_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]    
        if(max(res_1)<=max(res_2)): return 1
        else: return 0
    else: 
        res_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
        res_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]   
        if(aux_1<=aux_2): return 1
        else: return 0
    
    #max_1 = max(res_1)+aux_1
    #max_2 = max(res_2)+aux_2
    #print("ITERACION I J")
    #print(max_1,max_2)
    
    
    
    '''
    if(new_eval[2]>=0 and new_eval[3]>=0): #nueva_evaluacion cumple ambas restriccionnes
        if(eval_i_j[2]>=0 and eval_i_j[3]>=0): #eval_vecino cumple ambas restricciones
            ###se cumplen restricciones, evaluacion de actualizacion de vecinos normal:
            aux_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
            aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
            if(max(aux_1)<=max(aux_2)): return 1
            else: return 0
            
        else: 
            aux_1 = [vector_landa_j[0] * abs(new_eval[0]+abs(new_eval[2])-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
            aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
            if(max(aux_1)<max(aux_2)): return 1
            else: return 0


    else:  #nueva_evaluacion no cumple ambas restriccionnes
        if(new_eval[2]<0 and new_eval[3]<0):  #nueva_evaluacion no cumple ninguna restriccion
            if(eval_i_j[2]<0 and eval_i_j[3]<0):  #eval_vecino no cumple ninguna restriccion
                #r2 = eval_i_j[3]
                #COMPARACIONES: NINGUNO CUMPLE NINGUNA RESTRICCION
                #aux_1 = [vector_landa_j[0] * abs(new_eval[0]-z[0]), vector_landa_j[1] * abs(new_eval[1]-z[1])]
                #aux_2 = [vector_landa_j[0] * abs(eval_i_j[0]-z[0]), vector_landa_j[1] * abs(eval_i_j[1]-z[1])]
                #max_1 = max(aux_1)
                #max_2 = max(aux_2)
                ##################################################
                # Devuelvo la suma de ambas restricciones
                aux_1 = new_eval[2] + new_eval[3]
                aux_2 = eval_i_j[2] + eval_i_j[3]
                if(aux_1 > aux_2): return 1
                else: return 0 
                
            else: return 0 #para eval_i_j: cumple una o mas restricciones
                
        else: #nueva_evaluacion cumple una unica restricciones
            if(eval_i_j[2]>=0 and eval_i_j[3]>=0): return 0 #si evaluacion vecino cumple ambas y nueva_eval solo cumple una
            else:
                if(eval_i_j[2]<0 and eval_i_j[3]<0):return 1  
                #else: return 0
                else: #ambas cumplen una unica restriccion
                    aux_1 = [new_eval[2],new_eval[3]]
                    aux_2 = [eval_i_j[2],eval_i_j[3]]
                    if(min(aux_1) > min(aux_2)): 
                        if(i==j):return 1
                        else: return 0
                    else: return 0 
    '''



if __name__ == "__main__":
        
        ''' EJECUCION '''
    #for r in range(0,R):

        ''' INICIALIZACION '''
        items_inicializacion = ini.inicializacion() #llamada a la funcinon de inicializacion
        
        vector_landa = items_inicializacion[0] #vector landa
        vecindad_global = items_inicializacion[1] #vecindad para cada individuo
        random_vector = items_inicializacion[2] #vector random inicial: N individuos con D dimensiones
        
        #evaluaciones = items_inicializacion[3] #valores z(f1,f2) para cada individuo 

        z = items_inicializacion[3] #vector z*
        x = random_vector #primera generacion de N individuos
        
        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_cf6/salida_z_cf6_4000_all.txt','w')
        #f.close()


        ''' ITERACION '''
        for g in range(0,G):
            for i in range(0,N):
                    
                vecindad_i = vecindad_global[i] #vecinos para el individuo i
                
                vector_mutante = crea_vector_mutante(x[random.choice(vecindad_i)], #elegimos uno de los indices de vecindad_i para el vector x aleatoriamente
                        x[random.choice(vecindad_i)], x[random.choice(vecindad_i)]) #vector mutante i para individuo i de D dimensiones
                
                vector_y = crea_vector_y(x[i],vector_mutante) #vector resultante de D dimensiones
                    
                new_eval = CF6.func(vector_y) #evaluamos f1 y f2 para el nuevo vector y
                
                #f = 100 
                #sum = abs(new_eval[2]+new_eval[3])
                if(new_eval[0]<z[0] and new_eval[2]>=0 and new_eval[3]>=0): z[0] = new_eval[0]#+(new_eval[2]+new_eval[3])*FACTOR; 
                if(new_eval[1]<z[1] and new_eval[2]>=0 and new_eval[3]>=0): z[1] = new_eval[1]
                    
                #sustituimos vector_y para cada vecino
                for j in range(0,T):
                    eval_i_j = CF6.func(x[vecindad_i[j]])
                    bool_actualiza_vecinos = func_bool_actualiza_vecino_j_4D(new_eval, eval_i_j, vector_landa[vecindad_i[j]], z, j, i) #si devuelve 1: el vector_y mejora al vecino j
                    if(bool_actualiza_vecinos==1): x[vecindad_i[j]] = vector_y#;print("aa");print(i,j)

            #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_cf6/salida_z_cf6_4000_all.txt','a')
            #for h in range(0,N):
            #    res = CF6.func(x[h])
            #    f.write(str(res[0])+"    "+str(res[1])+"\n")
            #f.close()



        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_cf6/salida_z_cf6_4000.txt','w')
        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_cf6_16D/salida_z_cf6_10000.txt','w')        
        
        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_cf6_16D/salida_z_cf6_4000.txt','w')        
        #f = open ('/home/javier/Universidad/ASC/BLOQUE_1/sol_cf6/salida_z_cf6_10000.txt','w')
        
        #f.write("\n\n EJECUCION N:"+str(g))
        #for h in range(0,N):
        #    res = CF6.func(x[h])
        #    f.write(str(res[0])+"    "+str(res[1])+"\n")
        #f.close()
        #print(x)
        
        crea_pelicula(x)
    
    
    
    
    
    
    

    