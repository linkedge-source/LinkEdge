import math

# =====================================
# FUNCOES
# =====================================

def descricao_projeto():
    print("\n=== SOBRE O PROJETO ===")
    print("O LinkEdge monitora areas de risco.")
    print("Utiliza sensores e comunicacao via satelite.")
    print("Analisa sinais da rede mesh.")
    print("Identifica situacoes de emergencia.")
    print("E gera relatorios para resposta rapida.")

def escolher_melhor_no(sinais):
    maior = max(sinais)
    indice = sinais.index(maior)

    nos = ["NO A", "NO B", "NO C"]

    return nos[indice]

def monitoramento():

    print("\n=== MONITORAMENTO ===")

    temperatura = float(input("Digite a temperatura: "))
    nivel_agua = float(input("Digite o nivel da agua (%): "))
    movimento = int(input("Movimento detectado? (1=SIM / 0=NAO): "))

    print("\n=== DADOS COLETADOS ===")
    print("Temperatura:", temperatura, "C")
    print("Nivel da agua:", nivel_agua, "%")

    if movimento == 1:
        print("Movimento detectado: SIM")
    else:
        print("Movimento detectado: NAO")

def roteamento():

    print("\n=== ROTEAMENTO ===")

    sinal_a = int(input("Sinal do NO A: "))
    sinal_b = int(input("Sinal do NO B: "))
    sinal_c = int(input("Sinal do NO C: "))

    sinais = [sinal_a, sinal_b, sinal_c]

    print("\nSinais recebidos:")

    for i in range(len(sinais)):
        print("NO", chr(65 + i), "=", sinais[i])

    melhor_no = escolher_melhor_no(sinais)

    print("\nMelhor rota selecionada:", melhor_no)
    
def calcular_angulo():

    print("\n=== CALCULO DE ANGULO ===")

    altura = float(input("Altura do satelite: "))
    distancia = float(input("Distancia horizontal: "))

    angulo = math.degrees(
        math.atan(altura / distancia)
    )

    print("Angulo:", round(angulo, 2), "graus")

    if angulo >= 45:
        print("Conexao estavel")
    else:
        print("Conexao instavel")
        
def gerar_risco(temperatura, nivel_agua, movimento):

    if nivel_agua >= 80:
        return "ENCHENTE"

    elif temperatura >= 45:
        return "INCENDIO"

    elif movimento == 1:
        return "DESLIZAMENTO"

    else:
        return "AREA SEGURA"


def relatorio():

    print("\n=== RELATORIO FINAL ===")

    temperatura = float(input("Digite a temperatura: "))
    nivel_agua = float(input("Digite o nivel da agua (%): "))
    movimento = int(input("Movimento detectado? (1=SIM / 0=NAO): "))

    risco = gerar_risco(
        temperatura,
        nivel_agua,
        movimento
    )

    historico = []

    historico.append(risco)

    print("\n=== RESULTADO ===")
    print("Risco identificado:", risco)

    print("\nHistorico de analises:")

    for item in historico:
        print("-", item)


# =====================================
# MENU PRINCIPAL
# =====================================

while True:

    print("\n================================")
    print("LINKEDGE")
    print("================================")
    print("1 - Sobre o Projeto")
    print("2 - Monitoramento")
    print("3 - Roteamento")
    print("4 - Calcular Angulo")
    print("5 - Relatorio")
    print("6 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        descricao_projeto()

    elif opcao == "2":
        monitoramento()

    elif opcao == "3":
        roteamento()

    elif opcao == "4":
        calcular_angulo()

    elif opcao == "5":
        relatorio()

    elif opcao == "6":
        print("Encerrando sistema...")
        break
        
    else:
        print("Opcao invalida!")
