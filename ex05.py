def verificar_situacao():
    print("\n=== VERIFICACAO DE SITUACAO ===")
    pontuacao = float(input("Digite a pontuacao do funcionario (0 a 10): "))
    presenca = float(input("Digite o percentual de presenca (0 a 100): "))
    print(f"Pontuacao: {pontuacao} - Presenca: {presenca}%")

    if presenca >= 80:
        print("Presenca OK")
        if pontuacao >= 7.0:
            print("RESULTADO: APROVADO - Pontuacao e presenca suficientes")
        else:
            print(f"RESULTADO: REPROVADO - Presenca OK, mas pontuacao {pontuacao} abaixo de 7.0")
    else:
        print(f"RESULTADO: REPROVADO - Presenca {presenca}% abaixo de 80%")


def classificar_desempenho():
    print("\n=== CLASSIFICACAO DE DESEMPENHO ===")
    pontuacao = float(input("Digite a pontuacao para classificar (0 a 10): "))
    print(f"Pontuacao: {pontuacao}")

    if pontuacao >= 9.0:
        classificacao = "EXCELENTE"
    elif pontuacao >= 7.0:
        classificacao = "BOM"
    elif pontuacao >= 5.0:
        classificacao = "REGULAR"
    elif pontuacao >= 3.0:
        classificacao = "RUIM"
    else:
        classificacao = "PESSIMO"

    print(f"CLASSIFICACAO: {classificacao}")


def processar_menu():
    print("\n=== PROCESSADOR DE MENU ===")
    print("1 - Listar funcionarios")
    print("2 - Cadastrar funcionario")
    print("3 - Calcular media")
    print("4 - Sair do sistema")

    opcao = input("Digite a opcao desejada: ")

    match opcao:
        case "1":
            print("OPCAO 1: Listar funcionarios")
        case "2":
            print("OPCAO 2: Cadastrar funcionario")
        case "3":
            print("OPCAO 3: Calcular media")
        case "4" | "sair":
            print("OPCAO 4: Sair do sistema")
        case _:
            print(f"OPCAO INVALIDA: {opcao}")


def avaliar_funcionario():
    print("\n=== AVALIACAO DO FUNCIONARIO ===")
    nome = input("Digite o nome do funcionario: ")
    pontuacao = float(input("Digite a pontuacao do funcionario (0 a 10): "))
    faltas = int(input("Digite o numero de faltas: "))
    print(f"Funcionario: {nome} - Pontuacao: {pontuacao} - Faltas: {faltas}")

    dados = (pontuacao, faltas)

    match dados:
        case (p, _) if p >= 9.0:
            print(f"{nome}: DESTAQUE - Pontuacao {p}")
        case (p, f) if p >= 7.0 and f <= 10:
            print(f"{nome}: APROVADO - Pontuacao {p}, Faltas {f}")
        case (p, f) if p >= 5.0 and f <= 10:
            print(f"{nome}: EM OBSERVACAO - Pontuacao {p}, Faltas {f}")
        case (p, f) if p < 5.0 or f > 10:
            print(f"{nome}: REPROVADO - Pontuacao {p}, Faltas {f}")
        case _:
            print(f"{nome}: SITUACAO INDEFINIDA")


def menu_principal():
    while True:
        print("\n===== SISTEMA DE AVALIACAO DE FUNCIONARIOS =====")
        print("1 - Verificar situacao (if aninhado)")
        print("2 - Classificar desempenho (elif encadeado)")
        print("3 - Processar menu (match simples)")
        print("4 - Avaliar funcionario (match com guarda)")
        print("0 - Encerrar")

        escolha = input("Escolha uma opcao: ")

        if escolha == "1":
            verificar_situacao()
        elif escolha == "2":
            classificar_desempenho()
        elif escolha == "3":
            processar_menu()
        elif escolha == "4":
            avaliar_funcionario()
        elif escolha == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opcao invalida, tente novamente.")


if __name__ == "__main__":
    menu_principal()
