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
        print(probabilidade)

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

# Populacao ###############################################################################

pop = []
mochila = []
n_pop = 6


for i in range(n_pop):
    mochila.clear()
    for i in range(22):
        indice = random.randint(0, 1)
        mochila.append(indice)
    pop.append(mochila.copy())
    

print(pop)


# Fitness Function ###############################################################################

fitness = []

for i in range(n_pop):
    peso = 0
    for j in range(22):
        peso = peso + pop[i][j]*data["Peso (g)"][j]
        if peso > 3000:
            peso = 0
    fitness.append(peso)
    

print(fitness)

# Seleção natural ###############################################################################

pais = []
num_pais = n_pop/2  

for i in range(num_pais):
    pai = selecao_roleta(pop, fitness)
    pais.append(pai)

print("Pais selecionados:")
print(pais)



