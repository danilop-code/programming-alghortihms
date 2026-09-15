import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_ALL, 'Portuguese_Brazil.1252')
    except:
        def formatar_moeda(valor):
            return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    else:
        def formatar_moeda(valor):
            return locale.currency(valor, grouping=True, symbol='R$ ').replace('R$ ', '').strip()
else:
    def formatar_moeda(valor):
        return locale.currency(valor, grouping=True, symbol='R$ ')

print("=" * 50)
print("         SISTEMA DE VENDAS")
print("=" * 50)

cliente = input("Nome do cliente: ")
item = input("Nome do item: ")
valor_unitario = float(input("Valor unitario (R$): "))
qtd = int(input("Quantidade: "))
desconto_percentual = float(input("Percentual de desconto (%): "))

subtotal = valor_unitario * qtd
abatimento = subtotal * (desconto_percentual / 100)
total_final = subtotal - abatimento
valor_medio = total_final / qtd

print("\n" + "=" * 50)
print("         NOTA DE VENDA")
print("=" * 50)

print(f"Cliente:          {cliente}")
print(f"Item:             {item}")
print(f"Quantidade:       {qtd} unidade(s)")
print(f"Valor unitario:   R$ {formatar_moeda(valor_unitario)}")
print("-" * 50)
print(f"Subtotal:         R$ {formatar_moeda(subtotal)}")
print(f"Desconto:         {desconto_percentual:.0f}% (R$ {formatar_moeda(abatimento)})")
print("-" * 50)
print(f"TOTAL A PAGAR:    R$ {formatar_moeda(total_final)}")
print(f"\nValor medio por unidade: R$ {formatar_moeda(valor_medio)}")

print("\n" + "=" * 50)
print("       VOLTE SEMPRE!")
print("=" * 50)

print("Processando venda", end="... ")
print("Concluida!", end="\n\n")
