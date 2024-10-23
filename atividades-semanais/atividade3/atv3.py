import random
import copy
import numpy as np
import matplotlib.pyplot as plt


def selecao_roleta(pop, fitness):
    soma_fitness = sum(fitness)
    probabilidade = []
    cumulativa = 0
    list_cumulativa = []
    list_cumulativa.clear()
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
n_pop = 100
geracao = []
fitness = []
fitness_mut = []
fitness_cross = []
valor_pop = []
filho1 = []
filho2 = []
filhos = []
pais = []
mem_valor = 0
count_patamar = 0
num_patamar = 10
ite = 0
num_ite = 1000
graf = {"Valor": [], "Fitness": []}

# Populacao inicial ###############################################################################


for i in range(n_pop):
    mochila.clear()
    for i in range(22):
        indice = random.randint(0, 1)
        mochila.append(indice)
    pop.append(mochila.copy())
    

while True:

    # Fitness Function ###############################################################################
    fitness.clear()  # Limpa a lista de fitness antes de calcular novamente
    for i in range(n_pop):
        peso = 0
        for j in range(22):
            peso = peso + pop[i][j]*data["Peso (g)"][j]
            if peso > 3000:
                peso = 0
        fitness.append(peso)
        

    #print("Fitness Population: ", sum(fitness))

    # Seleção natural ###############################################################################

    num_pais = int(n_pop/2)  
    pais.clear()
    for i in range(num_pais):
        pai = selecao_roleta(pop, fitness)
        pais.append(pai)


    # Cross Over ###############################################################################

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


    # Fitness Cross Over ###############################################################################

    fitness_cross.clear()

    for i in range(len(filhos)):
        peso = 0
        for j in range(22):
            peso = peso + filhos[i][j]*data["Peso (g)"][j]
            if peso > 3000:
                peso = 0
        fitness_cross.append(peso)

    #print("Fitness Cross Over: ", sum(fitness_cross))

    # Mutacao ###############################################################################

    geracao.clear()

    for i in filhos:
        r = random.random()
        filho = copy.deepcopy(i)
        if r <= 0.05:
            indice = random.randint(0, 21)
            filho[indice] = 1 - filho[indice]  
        geracao.append(filho)

        
    # Fitness Mutacao ###############################################################################

    fitness_mut.clear()

    for i in range(n_pop):
        peso = 0
        for j in range(22):
            peso = peso + geracao[i][j]*data["Peso (g)"][j]
            if peso > 3000:
                peso = 0
        fitness_mut.append(peso)
        
    #print("Fitness Mutacao: ", sum(fitness_mut))

    # Nova Populacao ###############################################################################

    pop.clear()
    pop.extend(geracao)  # Adiciona todos os elementos de geracao a pop
    valor_pop.clear()

    for i in range(n_pop):
        valor = 0
        for j in range(22):
            valor = valor + pop[i][j]*data["Valor"][j]
        valor_pop.append(valor)
        
    #print("Valor nova populacao: ", sum(valor_pop))
      
    graf["Valor"].append(sum(valor_pop))
    graf["Fitness"].append(sum(fitness_mut))
        
    # Criterio de Parada ###############################################################################

    if ((sum(valor_pop) <= (mem_valor)*1.001) and (sum(valor_pop) >= (mem_valor)*0.99)):
        count_patamar += 1
    else:
        mem_valor = sum(valor_pop)
    if ((ite >= num_ite)):
    #if ((count_patamar>num_patamar) or (ite >= num_ite)):
        count_patamar = 0
        print(ite)
        ite = 0
        break
    
    ite += 1
    
    
# Plotando o gráfico
plt.plot(graf["Fitness"])  # 'o' para marcar os pontos
plt.title("Gráfico de Fitness")  # Título do gráfico
plt.xlabel("Geracao")  # Rótulo do eixo X
plt.ylabel("Fitness")  # Rótulo do eixo Y
plt.grid(True)  # Exibir grade
plt.show()  # Exibir o gráfico

plt.plot(graf["Valor"])  # 'o' para marcar os pontos
plt.title("Gráfico de Querer")  # Título do gráfico
plt.xlabel("Geracao")  # Rótulo do eixo X
plt.ylabel("Querer")  # Rótulo do eixo Y
plt.grid(True)  # Exibir grade
plt.show()  # Exibir o gráfico

#Melhor solucao
print("Melhor Solucao: \n")
for i in range(n_pop):
    print(f"Filho {i}:")
    print([pop[i][j] * data["Item"][j] for j in range(22)])

