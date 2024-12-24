import random
import copy
import matplotlib.pyplot as plt
import pandas as pd
import time
from classes import Funcionario
from classes import Equipe

# Grava o tempo inicial ###############################################################################
inicio = time.time()



# Funções ###############################################################################

def criar_funcionarios_arquivo(caminho_planilha):
    # Lê os dados da planilha em um DataFrame
    df = pd.read_excel(caminho_planilha)

    # Cria uma lista para armazenar os objetos Funcionario
    funcionarios = []

    # Itera sobre as linhas do DataFrame e cria objetos Funcionario
    for _, row in df.iterrows():
        funcionario = Funcionario(
            id=row['ID'],
            nome=row['NOME'],
            atua=row['ATUA'],
            funcao_primaria=row['FUNÇÃO P'],
            funcao_secundaria=row['FUNÇÃO S'],
            funcao_terciaria=row['FUNÇÃO T'],
            inicio_ferias=row['INÍCIO FÉRIAS'],
            fim_ferias=row['FIM FÉRIAS']
        )
        funcionarios.append(funcionario)

    return funcionarios

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
    # print(probabilidade)
    # print(list_cumulativa)

    r = random.random()
    for i, p in enumerate(list_cumulativa):
        if r < p:
            # print(i, p)
            return pop[i]

def fitness_function(n,fit):
    peso = 0
    for j in range(itens):
        peso += fit[n][j]*data["Peso (g)"][j]
        if peso > 3000:
            peso = 0
    return peso

def valor_function(n,vlr):
    valor = 0
    for j in range(itens):
        valor += vlr[n][j]*data["Valor"][j]
    return valor



# Dados iniciais ###############################################################################

# Criar funcionários a partir da planilha
funcionarios = criar_funcionarios_arquivo(r"C:\Users\stefa\Desktop\funcoes.xlsx")

# Exibir dados de todos os funcionários
for funcionario in funcionarios:
    funcionario.exibir_dados()

equipe_adm = Equipe("ADM", 0, 3, "08:00", "17:00", dias_uteis)
equipe_alfa = Equipe("ALFA", 5, 8, "07:00", "18:00", dobradinha)
equipe_bravo = Equipe("BRAVO", 5, 8, "13:00", "00:00", dobradinha)
equipe_charlie = Equipe("CHARLIE", 8, 8, "07:00", "18:00", dobradinha)
equipe_delta = Equipe("DELTA", 6, 8, "13:00", "00:00", dobradinha)


# Inicializacao ###############################################################################

itens = 22
n_pop = 100
taxa_mutacao = 0.03
num_ite = 1000
pop = []
mochila = []
mutacao = []
fitness_pop = []
fitness_mut = []
fitness_cross = []
valor_pop = []
filho1 = []
filho2 = [] ############################################################################### retirar filho 2
filhos = []
pais = []
melhor_geracao = []
melhor_iteracao = 0
melhor_fitness = []
melhor_valor = []
count_patamar = 0
num_patamar = 10
ite = 0
graf = {"Valor": [], "Fitness": []}



# Populacao inicial ###############################################################################

for i in range(n_pop):
    mochila.clear()
    mochila = []
    for i in range(itens):
        indice = random.randint(0, 1)
        mochila.append(indice)
    pop.append(mochila.copy())
    
    # print(mochila)


# Valor População inicial ########################################################################

valor_pop.clear()

for i in range(len(pop)):
    valor_pop.append(valor_function(i,pop))
# print(valor_pop)
# print("Valor populacao inicial: ", sum(valor_pop))


while True:

    # Fitness População ###############################################################################

    fitness_pop.clear()  # Limpa a lista de fitness antes de calcular novamente

    for i in range(len(pop)):
        fitness_pop.append(fitness_function(i,pop))
    # print(fitness_pop)
    # print("Fitness População: ", sum(fitness_pop))


    # Seleção natural ###############################################################################

    num_pais = round(len(pop)/2)
    pais.clear()
    for i in range(num_pais):
        pai = selecao_roleta(pop, fitness_pop)
        pais.append(pai)
        # print(pai)


    # Cross Over ###############################################################################
    
    filhos.clear()
    for i in range(num_pais):
        # for j in range(i+1,num_pais,2): ############################################################################### retirar exponencial de filhos
        secao = 10#random.randint(1,itens-1)
        filho1.clear()
        filho2.clear()
        for k in range(itens):
            if(k<=secao):
                filho1.append(pais[num_pais-(num_pais-i)][k])
                filho2.append(pais[num_pais-(num_pais-i+1)][k])
            else:
                filho1.append(pais[num_pais-(num_pais-i+1)][k])
                filho2.append(pais[num_pais-(num_pais-i)][k])
        filhos.append(filho1)  
        filhos.append(filho2)
    # print("len filhos",len(filhos))


    # Fitness Cross Over ###############################################################################

    fitness_cross.clear()
    for i in range(len(filhos)):
        fitness_cross.append(fitness_function(i,filhos))
    # print(fitness_cross)
    # print("Fitness Cross Over: ", sum(fitness_cross))


    # Mutacao ###############################################################################

    mutacao.clear()

    for i in filhos:
        r = random.random()
        filho = copy.deepcopy(i)
        if r <= taxa_mutacao:
            indice = random.randint(0, itens-1)
            filho[indice] = 1 - filho[indice]  
        mutacao.append(filho)

        
    # Fitness Mutacao ###############################################################################

    fitness_mut.clear()

    for i in range(len(mutacao)):
        fitness_mut.append(fitness_function(i,mutacao))

    # print("Fitness Mutacao: ", sum(fitness_mut))


    # Nova Populacao ###############################################################################

    pop.clear()
    pop.extend(mutacao)  # Adiciona todos os elementos de mutacao a pop
    valor_pop.clear()

    for i in range(len(pop)):
        valor_pop.append(valor_function(i,pop))
        
    #print("Valor nova populacao: ", valor_pop)
        
    graf["Valor"].append(sum(valor_pop))
    graf["Fitness"].append(sum(fitness_mut))


    # Melhor Geração ###############################################################################

    if sum(valor_pop) > sum(melhor_valor):
        melhor_iteracao = ite
        melhor_valor.clear()
        melhor_valor.extend(valor_pop)
        melhor_geracao.clear()
        melhor_geracao.extend(pop)
        melhor_fitness.clear()
        melhor_fitness.extend(fitness_mut)


    # Criterio de Parada ###############################################################################

    """if ((sum(valor_pop) <= (mem_valor)*1.01) and (sum(valor_pop) >= (mem_valor)*0.99)):
        count_patamar += 1
    else:
        mem_valor = sum(valor_pop)"""

    if ((ite >= num_ite)):
    #if ((count_patamar>num_patamar) or (ite >= num_ite)):
        #print(count_patamar)
        count_patamar = 0
        #print(ite)
        ite = 0
        break
    ite += 1


# Melhor geracao ###############################################################################
print("Melhor Geração:", melhor_iteracao)
print("Valor Querer:", sum(melhor_valor))
print("Valor Fitness:", sum(melhor_fitness))

for i in range(len(melhor_geracao)):
    print("Mochila:", i+1, "/ Fitness", melhor_fitness[i], "/ Querer", melhor_valor[i])
    print([melhor_geracao[i][j] * data["Item"][j] for j in range(itens)])


# Grava o tempo final
fim = time.time()

# Calcula o tempo total decorrido
tempo_total = fim - inicio

print(f"Tempo de execução: {round(tempo_total,3)} segundos")


# Plotando o gráfico ###############################################################################
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
