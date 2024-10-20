import random
import numpy as np

# Dados iniciais


peso = np.array([350, 250, 160, 120, 200, 100, 120, 220, 40, 80, 
                 100, 300, 180, 250, 220, 150, 280, 310, 120, 160, 
                 110, 210])

quero = np.array([300, 400, 450, 350, 250, 300, 200, 250, 150, 400, 
              350, 300, 450, 500, 350, 400, 200, 300, 250, 300, 
              150, 200])

# Populacao
pop = np.array([])
individuo = np.array([])

for i in range (10):
    individuo = np.array([])
    for j in range(22):
        individuo = np.append(individuo,[random.randint(0,1)])
    #print(individuo)
    pop = [pop,individuo]
print(pop)
    
#for ind in pop:
#    ptotal = ind * peso
#    print(ind)
#    print(peso)
#   print(ptotal)
    
        
    



