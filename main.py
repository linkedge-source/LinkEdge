import math

temperatura = 0
nivel_agua = 0
movimento = 0
rede = ""
satelite = ""
sinal_a = 0
sinal_b = 0
sinal_c = 0
latencia = 0

while True:

    print("\n=== LINKEDGE ===")
    print("1 - Monitoramento")
    print("2 - Roteamento")
    print("3 - Calcular angulo")
    print("4 - Relatorio")
    print("5 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":

        temperatura = float(input("Digite a temperatura: "))
        nivel_agua = float(input("Digite o nivel da agua: "))
        movimento = int(input("Movimento detectado? (1 = SIM / 0 = NAO): "))
        rede = input("Status da rede (ONLINE/OFFLINE): ")
        satelite = input("Satelite conectado? (SIM/NAO): ")

        print("\n=== MONITORAMENTO ===")
        print("Temperatura:", temperatura, "C")
        print("Nivel da agua:", nivel_agua, "%")

        if movimento == 1:
            print("Movimento detectado: SIM")
        else:
            print("Movimento detectado: NAO")

        print("Status da rede:", rede)
        print("Satelite conectado:", satelite)

    elif opcao == "2":

        sinal_a = int(input("Digite o sinal do NO A: "))
        sinal_b = int(input("Digite o sinal do NO B: "))
        sinal_c = int(input("Digite o sinal do NO C: "))
        latencia = int(input("Digite a latencia da rede: "))

        if sinal_a >= sinal_b and sinal_a >= sinal_c:
            melhor_no = "NO A"
        elif sinal_b >= sinal_a and sinal_b >= sinal_c:
            melhor_no = "NO B"
        else:
            melhor_no = "NO C"

        print("\n=== ROTEAMENTO ===")
        print("Melhor rota selecionada:", melhor_no)
        print("Latencia estimada:", latencia, "ms")

    elif opcao == "3":

        altura = float(input("Digite a altura do satelite: "))
        distancia = float(input("Digite a distancia horizontal: "))

        angulo = math.degrees(math.atan(altura / distancia))

        print("Angulo calculado:", round(angulo, 2), "graus")

        if angulo >= 45:
            print("Conexao estavel com o satelite")
        else:
            print("Conexao instavel")

    elif opcao == "4":

        temperatura = float(input("Digite a temperatura: "))
        nivel_agua = float(input("Digite o nivel da agua: "))
        movimento = int(input("Movimento detectado? (1 = SIM / 0 = NAO): "))
        rede = input("Status da rede (ONLINE/OFFLINE): ")
        satelite = input("Satelite conectado? (SIM/NAO): ")

        print("\n=== RELATORIO FINAL ===")

        if nivel_agua >= 80:
            risco = "ENCHENTE"
        elif temperatura >= 45:
            risco = "INCENDIO"
        elif movimento == 1:
            risco = "DESLIZAMENTO"
        else:
            risco = "AREA SEGURA"

        print("Risco identificado:", risco)

    elif opcao == "5":
        print("Encerrando o sistema...")
        break

    else:
        print("Opcao invalida")

# Matheus Dionisio Cintra RM569844
# Leonardo Daniel dos Santos RM571092
# Kaio Hiroki Kinoshita RM569127