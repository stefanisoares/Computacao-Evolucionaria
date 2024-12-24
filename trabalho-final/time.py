import random
import copy
import time
import pandas as pd
import os

class Funcionario:
    def __init__(self, id, nome, atua, funcao_primaria, funcao_secundaria, funcao_terciaria, inicio_ferias, fim_ferias):
        self.id = id
        self.nome = nome
        self.atua = atua
        self.funcao_primaria = funcao_primaria
        self.funcao_secundaria = funcao_secundaria
        self.funcao_terciaria = funcao_terciaria
        self.inicio_ferias = inicio_ferias
        self.fim_ferias = fim_ferias

    def exibir_dados(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Equipe: {self.atua}")
        print(f"Função Primária: {self.funcao_primaria}")
        print(f"Função Secundária: {self.funcao_secundaria}")
        print(f"Função Terciária: {self.funcao_terciaria}")
        print(f"Período de Férias: {self.inicio_ferias}")
        print(f"Período de Férias: {self.fim_ferias}")
        print("-" * 40)

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

# Caminho do arquivo Excel
caminho = r"C:\Users\stefa\Desktop\funcoes.xlsx"

# Criar funcionários a partir da planilha
funcionarios = criar_funcionarios_arquivo(caminho)

# Exibir dados de todos os funcionários
for funcionario in funcionarios:
    funcionario.exibir_dados()