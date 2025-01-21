import random

# Definindo o formato do ritmo e horários das equipes
class Equipe:
    def _init_(self, nome, min_funcion, max_funcion, hora_inicio, hora_fim, ritmo):
        self.nome = nome
        self.min_funcion = min_funcion
        self.max_funcion = max_funcion
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.ritmo = ritmo

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Mínimo Funcionários: {self.min_funcion}")
        print(f"Máximo Funcionários: {self.max_funcion}")
        print(f"Horário: {self.hora_inicio} às {self.hora_fim}")
        print(f"Ritmo de Trabalho: {self.ritmo}")

# Representação de Funcionário
class Funcionario:
    def _init_(self, nome, cargo, ferias):
        self.nome = nome
        self.cargo = cargo
        self.ferias = ferias  # Lista de dias do mês em que está de férias

# Inicializando equipes e funcionários
funcionarios = [
    Funcionario("CAP COELHO", "ADMINISTRACAO", []),
    Funcionario("2º SGT LINHARES", "ADMINISTRACAO", []),
    Funcionario("3º SGT LEONARDO", "ADMINISTRACAO", []),
    Funcionario("2º TEN TORRES", "TRÂNSITO CMD", []),
    Funcionario("2º SGT PRISCILA", "TRÂNSITO CMD", []),
    Funcionario("3º SGT NETO", "TRÂNSITO CMD", []),
    Funcionario("3º SGT  WAINE", "CMT GuPTran", []),
    Funcionario("3º SGT FRANCINE", "CMT GuPTran", []),
    Funcionario("3º SGT L. MOREIRA", "CMT GuPTran", []),
    Funcionario("CB OLIVEIRA", "MOT", []),
    Funcionario("CB SOARES", "MOT", []),
    Funcionario("CB SIQUEIRA", "MOT", []),
    Funcionario("CB VIANA", "MOT", [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("SD SILVINO", "MOT", []),
    Funcionario("2º SGT GALVÃO", "TRÂNSITO CMD", []),
    Funcionario("3º SGT NUNES", "CMT GuPTran", []),
    Funcionario("3º SGT  SÉRGIO", "CMT GuPTran", []),
    Funcionario("3º SGT HENRIQUE", "CMT GuPTran", []),
    Funcionario("3º SGT IESUS", "CMT GuPTran", []),
    Funcionario("CB HUGO", "MOT", []),
    Funcionario("CB VALVERDE", "MOT", []),
    Funcionario("CB DOUGLAS", "PAT", [3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("SD M. DOUGLAS", "PAT", []),
    Funcionario("SD MARIANA", "PAT", []),
    Funcionario("2º SGT SANTANNA", "TRÂNSITO CMD", []),
    Funcionario("3º SGT  ALYSSON", "TRÂNSITO CMD", []),
    Funcionario("3º SGT  SPAKOSKI", "CMT GuPTran", []),
    Funcionario("3º SGT CUNHA", "CMT GuPTran", []),
    Funcionario("3º SGT WESLEY", "CMT GuPTran", []),
    Funcionario("CB VANESSA", "CMT GuPTran", []),
    Funcionario("CB VASCONCELOS", "MOT", []),
    Funcionario("SD LEMOS JR", "MOT", []),
    Funcionario("SD JORDAN", "MOT", []),
    Funcionario("2º TEN BORGES", "TRÂNSITO CMD", []),
    Funcionario("1º SGT M. PAULO", "TRÂNSITO CMD", [3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("3º SGT NOGOEIRA", "CMT GuPTran", [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]),
    Funcionario("3º SGT ARAÚJO", "CMT GuPTran", []),
    Funcionario("3º SGT THIAGO", "CMT GuPTran", []),
    Funcionario("CB SANTOS", "MOT", []),
    Funcionario("CB THOMAZ", "MOT", []),
    Funcionario("CB BAZÍLIO", "MOT", [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("CB ASSIS", "PAT", []),
    Funcionario("SD NEROCI", "MOT", [3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("SD ZEIDAN", "MOT", []),
    Funcionario("SD BRUNA", "RADIOPERADOR", []),
    Funcionario("CB MORAES", "RADIOPERADOR", []),
    Funcionario("1º SGT MARTINS", "RADIOPERADOR", []),
    Funcionario("CB ALMEIDA", "RADIOPERADOR", []),
    Funcionario("3 SGT MACHADO", "RADIOPERADOR", []),
    Funcionario("CB DEIVID", "INTENDENTE", []),
    Funcionario("CB ALEX", "INTENDENTE", []),
    Funcionario("CB VICTOR", "INTENDENTE", []),
    Funcionario("CB LEÃO", "INTENDENTE", [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]),
    Funcionario("CB LUIZ", "GUARDA", []),
    Funcionario("CB MILTON", "GUARDA", []),
    Funcionario("CB LAGUARDIA", "GUARDA", [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]),
    Funcionario("SD ALVES", "GUARDA", []),
    Funcionario("CB LÚCIO", "GUARDA", []),
    Funcionario("CB DUQUE", "GUARDA", [3, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("CB LUIZ SILVA", "GUARDA", []),
    Funcionario("3º SGT FERNANDO", "GARAGISTA", []),
    Funcionario("3º SGT MILSON", "GARAGISTA AUX", []),
    Funcionario("CB JAMAR", "CROP", []),
    Funcionario("CB ESTEVAM", "CROP", [2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]),
    Funcionario("2º SGT  REIS", "A DISPOSIÇÃO", []),
    Funcionario("3º SGT CAPISTRANO", "A DISPOSIÇÃO", [])
]

equipes = [
    Equipe("Administração", 2, 5, "08:00", "17:00", ["SV"] * 22),
    Equipe("Alfa", 5, 8, "07:00", "18:00", ["SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV"]),
    Equipe("Bravo", 5, 8, "13:00", "00:00", ["SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV"]),
    Equipe("Charlie", 8, 10, "07:00", "18:00", ["F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F"]),
    Equipe("Delta", 6, 8, "13:00", "00:00", ["F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F", "SV", "SV", "F", "F"])
]

# Inicialização da população inicial

def inicializar_populacao_completa(dias):
    individuo = {}
    for dia in range(1, dias + 1):
        individuo[dia] = {}
        funcionarios_disponiveis = [f for f in funcionarios if dia not in f.ferias]
        for equipe in equipes:
            if equipe.ritmo[dia - 1] == "SV":
                if len(funcionarios_disponiveis) >= equipe.min_funcion:
                    alocacao = random.sample(funcionarios_disponiveis, k=equipe.min_funcion)
                    individuo[dia][equipe.nome] = alocacao
                    funcionarios_disponiveis = [f for f in funcionarios_disponiveis if f not in alocacao]
                else:
                    individuo[dia][equipe.nome] = []
    return individuo

# Função de avaliação (fitness)
def calcular_fitness(individuo):
    fitness = 1000  # Pontuação inicial

    for dia, equipes_dia in individuo.items():
        for equipe_nome, funcionarios_equipe in equipes_dia.items():
            equipe = next((e for e in equipes if e.nome == equipe_nome), None)
            if not equipe:
                continue

            # Penalidade por não atingir o mínimo de funcionários
            if len(funcionarios_equipe) < equipe.min_funcion:
                fitness -= 20

            # Penalidade por exceder o máximo de funcionários
            if len(funcionarios_equipe) > equipe.max_funcion:
                fitness -= 20

            # Verificar especializações obrigatórias
            especializacoes = {"TRÂNSITO CMD": 0, "MOT": 0, "CMT GuPTran": 0}
            for funcionario in funcionarios_equipe:
                if funcionario.cargo in especializacoes:
                    especializacoes[funcionario.cargo] += 1

            for cargo, presente in especializacoes.items():
                if presente == 0:
                    fitness -= 50  # Penalidade por falta de especialização

    return fitness

# Exibir alocação final
def exibir_alocacao(individuo):
    for dia, equipes_dia in individuo.items():
        print(f"Dia {dia}:")
        for equipe, funcionarios in equipes_dia.items():
            nomes = [f.nome for f in funcionarios]
            print(f"  {equipe}: {', '.join(nomes) if nomes else 'Nenhum funcionário alocado'}")
        print("-" * 40)

# Testando a alocação completa
individuo_completo = inicializar_populacao_completa(22)
print("Alocação completa:")
exibir_alocacao(individuo_completo)

# Testando fitness para o indivíduo alocado
fitness = calcular_fitness(individuo_completo)
print(f"Fitness do indivíduo: {fitness}")
