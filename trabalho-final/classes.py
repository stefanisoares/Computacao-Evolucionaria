import random
import copy
import time
import pandas as pd
import os

####  FUNCIONARIOS #########################################################################################################
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
        print(f"Atuação: {self.atua}")
        print(f"Função Primária: {self.funcao_primaria}")
        print(f"Função Secundária: {self.funcao_secundaria}")
        print(f"Função Terciária: {self.funcao_terciaria}")
        print(f"Início de Férias: {self.inicio_ferias}")
        print(f"Fim de Férias: {self.fim_ferias}")
        print("-" * 40)
        

    
#### EQUIPES ################################################################################################################

class Equipe:
    def __init__(self, nome, min_funcion, max_funcion, hora_inicio, hora_fim, ritmo):
        self.nome = nome
        self.min_funcion = min_funcion
        self.max_funcion = max_funcion
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.ritmo = ritmo

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Minimo Funcionarios: {self.min_funcion}")
        print(f"Maximo Funcionarios: {self.max_funcion}")
        print(f"Hora Inicio: {self.hora_inicio}")
        print(f"Hora Fim: {self.hora_fim}")
        print(f"Ritmo de Trabalho: {self.ritmo}")
        print("-" * 40)
        
        
    