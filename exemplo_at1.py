# from sys import float_repr_style
"""Module providingFunction printing python version."""
print("Bem vindo a Loja do Wellington")
valor_produto = float(input("Digite o valor do produto: "))
qtd_produto = int(input("Digite a quantidade de produtos: "))
valor_sem_desconto = valor_produto * qtd_produto
DESCONTO = float(0)

if qtd_produto <= 4:
    print("Essa quantidade não tem desconto")
elif 5 <= qtd_produto <= 19:
    DESCONTO = 0.03 # desconto de 3%
elif 20 <= qtd_produto <= 99:
    DESCONTO = 0.06 #desconto de 6%
else:
    DESCONTO = 0.10 #desconto de 10%

valor_com_desconto = valor_sem_desconto*(1-DESCONTO)
PERCENTUAL = int(DESCONTO*100)
print("O valor sem desconto foi: R$", valor_sem_desconto)
if qtd_produto >=5:
    print(f"O valor com desconto foi: R$ {valor_com_desconto:.2f} (desconto {PERCENTUAL}%)")
