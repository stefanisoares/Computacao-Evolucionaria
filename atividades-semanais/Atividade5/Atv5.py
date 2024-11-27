import numpy as np

""" FUNÇÕES """

def imprime_matriz(matriz):
    for i in matriz:
        print(i)

continuar = 9

""" PARÂMETROS INICIAIS """

iteracoes = 5           # Número de iterações
alpha = 0.5             # Peso do feromônio
beta = 0.5              # Peso da heurística (1/dij)
evaporacao = 0.5        # Taxa de evaporação do feromônio
num_formigas = 5        # Número de formigas
Q = 1                   # Constante para quantidade de feromonio depositado

n_best=5                # Quantas melhores formigas contribuem com feromônio

c = [
[0.0, 1.0, 2.2, 2.0, 4.1],
[1.0, 0.0, 1.4, 2.2, 4.0],
[2.2, 1.4, 0.0, 2.2, 3.2],
[2.0, 2.2, 2.2, 0.0, 2.2],
[4.1, 4.0, 3.2, 2.2, 0.0]] # Matriz de distâncias (cij)
# print("custos")
# imprime_matriz(custos)

#############################deve ser gerada aleatoriamente####################################
t = [
[0.00, 0.30, 0.25, 0.20, 0.30],
[0.30, 0.00, 0.20, 0.20, 0.30],
[0.25, 0.20, 0.00, 0.10, 0.15],
[0.20, 0.20, 0.10, 0.00, 0.45],
[0.30, 0.30, 0.15, 0.45, 0.00]] # Matriz de Feromônios

n = []
linha = []
for i in c:
    linha = []
    for j in i:
        if j == 0:
            linha.append(0)
        else:
            linha.append(round(1/j,2))
    n.append(linha)

# print("nij")
# imprime_matriz(nij)

caminho_anterior = []
caminho_atual = []

""" ALGORITMO """
for ite in range(iteracoes):
    caminho_atual = []
    print("t",ite)
    imprime_matriz(t)
    L = []
    depositos = []
    x = []

    for formiga in range(num_formigas):
        p = np.zeros((5,5))
        x.append(np.zeros((5,5)))
        # print("FORMIGA", formiga+1)
        cidades = []
        for i in range(len(c)):
            cidades.append(i)
        i = formiga
        for k in range(len(cidades)):
            cidades.remove(i)
            # print("cidades",cidades)
            if len(cidades) == 1:
                for a in range(len(c)):
                    if a == cidades[0]:
                        p[i][a] = int(1)
                        x[formiga][i][a] = int(1) 
                    else:
                        p[i][a] = int(0)
                        x[formiga][i][a] = int(0)
                # print("p")
                # imprime_matriz(p)
                i = cidades[0]
                # print('foi pra cidade',i+1)
            elif len(cidades) == 0:
                for a in range(len(c)):
                    if a == formiga:
                        p[i][a] = int(1)
                        x[formiga][i][a] = int(1)
                    else:
                        p[i][a] = int(0)
                        x[formiga][i][a] = int(0)
                # print("p")
                # imprime_matriz(p)
                # print('foi pra cidade',formiga+1)
            else:
                for j in range(len(c)):
                    if not(j in cidades):
                        p[i][j] = int(0)
                        x[formiga][i][j] = int(0)
                    else:
                        # print("cidades", i+1,j+1)
                        # print("tij nij",t[i][j],n[i][j])
                        num = round(pow(t[i][j],alpha) * pow(n[i][j],beta),3)
                        den = 0
                        for l in range(len(c)):
                            if l in cidades and l != j:
                                # print("til njl",t[i][l],n[j][l])
                                den += round(pow(t[i][l],alpha) * pow(n[j][l],beta),3)
                        prob = round(num/den,3)
                        # print(pij)
                        p[i][j] = prob
                # print("p")
                # imprime_matriz(p)

                maior_pij = 0
                for ind_pij in range(len(p[i])):
                    if p[i][ind_pij] > maior_pij:
                        maior_pij = p[i][ind_pij]
                        ind_maior_pij = ind_pij
                # print('foi pra cidade',ind_maior_pij+1)
                x[formiga][i][ind_maior_pij] = int(1)
                i = ind_maior_pij
        # print("p")
        # imprime_matriz(p)
        # print("x")
        # imprime_matriz(x)
        # print("\n")
        caminho = []
        distancia = 0
        print("formiga", formiga+1,"- caminho:", formiga+1, end=" ")
        caminho.append(formiga+1)
        for a in range(len(c)):
            for b in range(len(c[a])):
                if x[formiga][a][b] == 1:
                    print(b+1, end=" ")
                    caminho.append(b+1)
                    distancia += c[a][b] * x[formiga][a][b]
        print()
        caminho_atual.append(caminho)
        L.append(float(round(distancia,2)))
        depositos.append(float(round((Q/distancia),3)))
        
    # print("x")
    # imprime_matriz(x)

    # print("L")
    # print(L)

    # print("Depositos")
    # print(depositos)
    if caminho_anterior == caminho_atual:
        print()
        print("Acabou")
        print()
        break
        # while not((continuar == 0) or (continuar == 1)):
            # continuar = int(input("Deseja digite 0 se deseja parar ou 1 se deseja continuar: "))
    
    if continuar == 0:
        break
    elif continuar == 1 or continuar == 9:
        caminho_anterior = caminho_atual
        for a in range(len(t)):
            for b in range(len(t[a])):
                delta_t = 0
                if a != b:
                    for f in range(len(x)):
                        if x[f][a][b] == 1:
                            # print("arco",a+1,b+1, "formiga", f+1)
                            delta_t += x[f][a][b] * depositos[f]
                t[a][b] = float(round(((1-evaporacao) * t[a][b] + delta_t),2))

    # print("novo t")
    # imprime_matriz(t)
    print()
            





            








