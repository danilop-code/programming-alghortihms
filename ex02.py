titulo = "Cálculo da compra na papelaria"
descricao = "Um cliente comprou três cadernos, cada um por: "
frase_desconto = " e ganhou um desconto de: "
pergunta = "Qual foi o valor total pago?"
resposta = "O valor pago foi: "

preco_unitario = 18.50
quantidade = 3
desconto = 5.00

subtotal = preco_unitario * quantidade
total = subtotal - desconto

print(f"""
{titulo}
{descricao}R$ {preco_unitario:.2f}{frase_desconto}R$ {desconto:.2f}
{pergunta}
{resposta}R$ {total:.2f}
""")
