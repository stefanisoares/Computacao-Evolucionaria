import random
import numpy as np


def selecao_roleta(pop, fitness):
    soma_fitness = sum(fitness)
    probabilidade = []
    cumulativa = 0
    list_cumulativa = []
    for i in fitness:
        probabilidade.append(i/soma_fitness)
        cumulativa = cumulativa + i/soma_fitness
        list_cumulativa.append(cumulativa)
        #print(probabilidade)

    r = random.random()
    for i, p in enumerate(list_cumulativa):
        if r < p:
            return pop[i]






# Dados iniciais

data = {
    "Item": list(range(1, 23)),
    "Peso (g)": [350, 250, 160, 120, 200, 100, 120, 220, 40, 80, 
                 100, 300, 180, 250, 220, 150, 280, 310, 120, 160, 
                 110, 210],
    "Valor": [300, 400, 450, 350, 250, 300, 200, 250, 150, 400, 
              350, 300, 450, 500, 350, 400, 200, 300, 250, 300, 
              150, 200]
}

# Inicializacao ###############################################################################

pop = []
mochila = []
n_pop = 6
fitness = []

# Populacao ###############################################################################


for i in range(n_pop):
    mochila.clear()
    for i in range(22):
        indice = random.randint(0, 1)
        mochila.append(indice)
    pop.append(mochila.copy())
    

#print(pop)


# Fitness Function ###############################################################################

for i in range(n_pop):
    peso = 0
    for j in range(22):
        peso = peso + pop[i][j]*data["Peso (g)"][j]
        if peso > 3000:
            peso = 0
    fitness.append(peso)
    

#print(fitness)

# Seleção natural ###############################################################################

pais = []
num_pais = int(n_pop/2)  

for i in range(num_pais):
    pai = selecao_roleta(pop, fitness)
    pais.append(pai)

print("Pais selecionados:")
for i in pais:
    print(i)


# Cross Over ###############################################################################

filho1 = []
filho2 = []
filhos = []
filhos.clear()

for i in range(num_pais):
    for j in range(i+1,num_pais):
        secao = random.randint(1,21)
        filho1.clear()
        filho2.clear()
        for k in range(22):
            if(k<secao):
                filho1.append(pais[i][k])
                filho2.append(pais[j][k])
            else:
                filho1.append(pais[j][k])
                filho2.append(pais[i][k])
        filhos.append(filho1)  
        filhos.append(filho2) 
        # print("Pais: ", i, " e ", j)
        # print("Secao: ", secao)
        # print("Filho 1: ", filho1)
        # print("Filho 2: ", filho2)
        # print("\n\n")

print("\n\n")        
for i in filhos:
    print(i)

print("\n\n")

# Mutação

geracao = []
geracao.clear()

for i in filhos:
    r = random.random()
    print(r)
    if r <= 0.05:
        indice = random.randint(0, 22)
        print(indice)
        if i[indice] == 0:
            i[indice] = 1
        if i[indice] == 1:
            i[indice] = 0    
    geracao.append(i)
    
for i in geracao:
    print(i)