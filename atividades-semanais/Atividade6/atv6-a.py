import random

w = 0.3
n1 = 0.7
n2 = 0.2
gbest_ant = 0
count = 0
ite = 6

particulas = { "Particulas": [4.4, 5.6, 8.32],
                "Pbest":     [4.4, 5.6, 8.32],
                "Gbest":     [5.6],
                "fx":        [  0,   0,    0],   #fitness
                "fx_ant":    [600, 600,  600],
                "pbest-x":   [  0,   0,    0],
                "gbest-x":   [  0,   0,    0],
                "v":         [0.41, 0, -0.75]}
print("Particula", " | ", "F(x)", " | " "Pbest", " | ", "Pbest-x", " | ", "Gbest-x", " | ", "rnd1", " | ", "rnd2", " |  ", "v", "  | ", "Prox-x")
while count < 2:
    gbest_ant = particulas["Gbest"][0]
    
    print("Iteração: ", ite)
    
    for i in range(3):
        # Calcula f(x)
        particulas["fx"][i] = round((particulas["Particulas"][i] - 4)**2 - (particulas["Particulas"][i] - 8)**3 + 5, 2)
        
        # Calcula Pbest
        if particulas["fx"][i] < particulas["fx_ant"][i]:
            particulas["Pbest"][i] = particulas["Particulas"][i]  
        
        # Calcula Gbest 
        if particulas["fx"][i] < particulas["fx"][i-1]:
            particulas["Gbest"][0] = particulas["Particulas"][i] 
            
        
    for i in range(3):    
        # Calcula Pbest-x
        particulas["pbest-x"][i] = round(particulas["Pbest"][i] - particulas["Particulas"][i],1)
        
        # Calcula Gbest-x
        particulas["gbest-x"][i] = round(particulas["Gbest"][0] - particulas["Particulas"][i],1)
        
        # Calcula rnd1 e rnd2
        rnd1 = round(random.random(), 1)
        rnd2 = round(random.random(), 1)
        
        # Calcula v 
        particulas["v"][i] = round(w*particulas["v"][i] + n1*rnd1*particulas["pbest-x"][i] + n2*rnd2*particulas["gbest-x"][i], 2)
        
        # Print
        print("    ", particulas["Particulas"][i]," | ", particulas["fx"][i], " | ", particulas["Pbest"][i], " |   ", particulas["pbest-x"][i], " |   ", particulas["gbest-x"][i], " | ", rnd1, " | ", rnd2, " | ", particulas["v"][i], " |  ", round(particulas["Particulas"][i] + particulas["v"][i],2))
        
        
        # Calcula proximo x
        particulas["Particulas"][i] = round(particulas["Particulas"][i] + particulas["v"][i],2)
        
        
        
    if particulas["Gbest"][0] == gbest_ant:
        count += 1
    else:
        count = 0
    ite += 1
    print("Gbest:", particulas["Gbest"][0])
    print("\n")
        
       

