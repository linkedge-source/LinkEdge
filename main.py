import math

historico_riscos = []


def descricao_projeto():
    print("\n=== SOBRE O PROJETO ===")
    print("O LinkEdge monitora áreas de risco em tempo real.")
    print("Utiliza sensores e comunicação via satélite.")
    print("Analisa sinais da rede mesh para identificar falhas.")
    print("Detecta situações de emergência como enchentes e incêndios.")
    print("E gera relatórios para apoio à resposta rápida.")


def escolher_melhor_no(sinais):
    maior = max(sinais)
    indice = sinais.index(maior)
    nos = ["NÓ A", "NÓ B", "NÓ C"]
    return nos[indice]


def entrada_numero(mensagem, tipo="float"):
    while True:
        valor = input(mensagem)
        valido = True

        if tipo == "float":
            ponto = False
            inicio = 0
            if valor.startswith("-"):
                inicio = 1
            for i in range(inicio, len(valor)):
                c = valor[i]
                if c == "." and not ponto:
                    ponto = True
                elif c < "0" or c > "9":
                    valido = False
                    break
            if len(valor) == 0 or (valor.startswith("-") and len(valor) == 1):
                valido = False

        elif tipo == "int":
            inicio = 0
            if valor.startswith("-"):
                inicio = 1
            for i in range(inicio, len(valor)):
                c = valor[i]
                if c < "0" or c > "9":
                    valido = False
                    break
            if len(valor) == 0 or (valor.startswith("-") and len(valor) == 1):
                valido = False

        if valido:
            if tipo == "float":
                return float(valor)
            else:
                return int(valor)
        else:
            print("Entrada inválida. Digite apenas números.")


def entrada_binaria(mensagem):
    while True:
        valor = input(mensagem).strip()
        match valor:
            case "1":
                return 1
            case "0":
                return 0
            case _:
                print("Digite apenas 1 (SIM) ou 0 (NÃO).")


def entrada_sinal(mensagem):
    while True:
        valor = entrada_numero(mensagem, tipo="int")
        if 0 <= valor <= 100:
            return valor
        else:
            print("O sinal deve estar entre 0 e 100.")


def monitoramento():
    print("\n=== MONITORAMENTO ===")
    print("Informe os dados coletados pelos sensores:\n")

    temperatura = entrada_numero("Temperatura (°C, ex: 32.5): ", tipo="float")
    nivel_agua = entrada_numero("Nível da água (%, 0 a 100): ", tipo="float")

    while nivel_agua < 0 or nivel_agua > 100:
        print("O nível deve estar entre 0 e 100.")
        nivel_agua = entrada_numero("Nível da água (%, 0 a 100): ", tipo="float")

    movimento = entrada_binaria("Movimento detectado? (1=SIM / 0=NÃO): ")

    print("\n=== DADOS COLETADOS ===")
    print(f"Temperatura: {temperatura} °C")
    print(f"Nível d'água: {nivel_agua} %")

    match movimento:
        case 1:
            print("Movimento: SIM")
        case 0:
            print("Movimento: NÃO")


def roteamento():
    print("\n=== ROTEAMENTO ===")
    print("Informe a intensidade do sinal de cada nó (0 a 100):\n")

    sinal_a = entrada_sinal("Sinal do NÓ A: ")
    sinal_b = entrada_sinal("Sinal do NÓ B: ")
    sinal_c = entrada_sinal("Sinal do NÓ C: ")

    sinais = [sinal_a, sinal_b, sinal_c]

    print("\nSinais recebidos:")
    for i in range(len(sinais)):
        print(f"    NÓ {chr(65 + i)} = {sinais[i]}")

    melhor_no = escolher_melhor_no(sinais)
    print(f"\nMelhor rota selecionada: {melhor_no}")


def calcular_angulo():
    print("\n=== CÁLCULO DE ÂNGULO ===")
    print("Informe os dados de posicionamento do satélite:\n")

    altura = entrada_numero("Altura do satélite (km, ex: 550.0): ", tipo="float")
    distancia = entrada_numero("'Distância horizontal (km, ex: 300.0): ", tipo="float")

    while distancia == 0:
        print("A distância não pode ser zero.")
        distancia = entrada_numero(
            "Distância horizontal (km, ex: 300.0): ", tipo="float"
        )

    angulo = math.degrees(math.atan(altura / distancia))

    print(f"\n  Ângulo calculado: {round(angulo, 2)}°")

    match True:
        case _ if angulo >= 45:
            print("Conexão estável")
        case _:
            print("Conexão instável")


def gerar_risco(temperatura, nivel_agua, movimento):
    if nivel_agua >= 80:
        return "ENCHENTE"
    elif temperatura >= 45:
        return "INCÊNDIO"
    elif movimento == 1:
        return "DESLIZAMENTO"
    else:
        return "ÁREA SEGURA"


def relatorio():
    print("\n=== RELATÓRIO FINAL ===")
    print("Informe os dados para análise de risco:\n")

    temperatura = entrada_numero("  Temperatura (°C, ex: 32.5): ", tipo="float")
    nivel_agua = entrada_numero("  Nível da água (%, 0 a 100): ", tipo="float")

    while nivel_agua < 0 or nivel_agua > 100:
        print("O nível deve estar entre 0 e 100.")
        nivel_agua = entrada_numero("  Nível da água (%, 0 a 100): ", tipo="float")

    movimento = entrada_binaria("Movimento detectado? (1=SIM / 0=NÃO): ")

    risco = gerar_risco(temperatura, nivel_agua, movimento)
    historico_riscos.append(risco)

    print("\n=== RESULTADO ===")
    print(f"Risco identificado: {risco}")

    print(
        f"\nHistórico de análises desta sessão ({len(historico_riscos)} registro(s)):"
    )
    for i, item in enumerate(historico_riscos, start=1):
        print(f"{i}. {item}")


while True:
    print("\n================================")
    print("        L I N K E D G E        ")
    print("================================")
    print("  1 - Sobre o Projeto")
    print("  2 - Monitoramento")
    print("  3 - Roteamento")
    print("  4 - Calcular Ângulo")
    print("  5 - Relatório de Risco")
    print("  6 - Sair")
    print("--------------------------------")

    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            descricao_projeto()
        case "2":
            monitoramento()
        case "3":
            roteamento()
        case "4":
            calcular_angulo()
        case "5":
            relatorio()
        case "6":
            print("\nEncerrando sistema. Até logo!\n")
            break
        case _:
            print("\nOpção inválida! Digite um número de 1 a 6.")

# Matheus Dionisio Cintra RM569844
# Leonardo Daniel dos Santos RM571092
# Kaio Hiroki Kinoshita RM569127
