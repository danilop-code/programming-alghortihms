while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade < 0:
            print("Idade nao pode ser negativa. Tente novamente.")
            continue
        break
    except ValueError:
        print("Entrada invalida! Digite um numero inteiro para a idade.")

while True:
    resposta = input("Voce possui carteirinha? (sim/nao): ").strip().lower()
    if resposta in ['sim', 's', 'yes', 'y']:
        tem_carteirinha = True
        break
    elif resposta in ['nao', 'não', 'n', 'no']:
        tem_carteirinha = False
        break
    else:
        print("Resposta invalida! Digite 'sim' ou 'nao'.")

if idade < 12:
    mensagem = "Acesso nao permitido"
    status = "negado"
elif idade >= 12 and tem_carteirinha:
    mensagem = "Entrada liberada"
    status = "permitido"
else:
    mensagem = "Solicite sua carteirinha na recepcao"
    status = "pendente"

print("\n" + "=" * 50)
print("       RESULTADO DA LIBERACAO DE ACESSO")
print("=" * 50)

print(f"Idade informada:        {idade} anos")
print(f"Possui carteirinha:     {'Sim' if tem_carteirinha else 'Nao'}")
print("-" * 50)
print(f"Status:                 {mensagem.upper()}")

if status == "negado":
    print("Motivo: Idade minima para acesso e 12 anos.")
elif status == "permitido":
    print("Motivo: Idade e carteirinha confirmadas com sucesso.")
else:
    print("Motivo: E necessario apresentar a carteirinha para entrar.")

print("=" * 50)

print("\n[TESTES RAPIDOS]")
print("-" * 50)

print("Caso 1 - Idade: 10, Carteirinha: Nao")
if 10 < 12:
    print("  Resultado: Acesso nao permitido")
else:
    print("  Resultado: ERRO no teste!")

print("Caso 2 - Idade: 15, Carteirinha: Sim")
if 15 >= 12 and True:
    print("  Resultado: Entrada liberada")
else:
    print("  Resultado: ERRO no teste!")

print("Caso 3 - Idade: 20, Carteirinha: Nao")
if 20 >= 12 and False:
    print("  Resultado: ERRO no teste!")
else:
    print("  Resultado: Solicite sua carteirinha na recepcao")

print("-" * 50)
