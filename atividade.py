"""Module providingFunction printing python version."""
print("Bem vindo a Loja do José Wellington de Lima Bezerra")
valor_produto = float(input("Entre com valor do produto: ")) #Digitar o valor unitário do produto
qtd_produto = int(input("Entre com valor da quantidade: ")) #Quantos produtos
valor_sem_frete = valor_produto * qtd_produto

if 0 <= qtd_produto < 11: # Se a quantidade de produtos estiver entre 0 e 11
    FRETE = 30.00 #Será acrescentado o frete de R$30.00
elif 11 <= qtd_produto < 101: # Se a quantidade de produtos estiver entre 0 e 11
    FRETE = 60.00 #Será acrescentado o frete de R$60.00
elif 101 <= qtd_produto < 1001: # Se a quantidade de produtos estiver entre 0 e 11
    FRETE = 120.00 #Será acrescentado o frete de R$120.00
else: # Se a quantidade de produtos estiver acima ou igual a 1001
    FRETE = 240.00 #Será acrescentado o frete de R$240.00
valor_com_frete = valor_sem_frete + FRETE
print(f"O valor sem frete foi: R$ {valor_sem_frete:.2f}")
print(f"O valor com frete foi: R$ {valor_com_frete:.2f} (frete foi de R$ {FRETE:.2f})")
