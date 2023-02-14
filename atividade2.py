"""Module providingFunction printing python version."""
print("Bem vindo a Sorveteria do José Wellington de Lima Bezerra")
VALOR = 0 #Variável que receberá a soma dos valores em reais
DESCRICAO = "" #Variável com a Descrição dos sabores
UNITARIO = 0 #Variável para armazenar o valor unitário em reais de cada pedido
print("--------------------------------------------Cardápio--------------------------------------------")
print("| Código | Descrição            | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (1000ml) |")
print("|   TR   | sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |       R$ 18,00     |")
print("|   ES   | sabores Especiais    |      R$ 7,00      |      R$ 12,00      |       R$ 21,00     |")
print("|   PR   | sabores Premium      |      R$ 8,00      |      R$ 14,00      |       R$ 24,00     |")
print("------------------------------------------------------------------------------------------------")
while True:
    tamanho = input("Entre com o TAMANHO do pote desejado (P/M/G): ").upper() #Entrada do usuário será em maiúscula
    sabor = input("Entre com o CÓDIGO do sabor desejado (TR/ES/PR): ").upper() #Entrada do usuário será em maiúscula
    if tamanho == "P" and sabor == "TR":
        DESCRICAO = "TRADICIONAL"
        UNITARIO = 6
        VALOR = VALOR + UNITARIO
    elif tamanho == "M" and sabor == "TR":
        DESCRICAO = "TRADICIONAL"
        UNITARIO = 10
        VALOR = VALOR + UNITARIO
    elif tamanho == "G" and sabor == "TR":
        DESCRICAO = "TRADICIONAL"
        UNITARIO = 18
        VALOR = VALOR + UNITARIO
    elif tamanho == "P" and sabor == "ES":
        DESCRICAO = "ESPECIAL"
        UNITARIO = 7
        VALOR = VALOR + UNITARIO
    elif tamanho == "M" and sabor == "ES":
        DESCRICAO = "ESPECIAL"
        UNITARIO = 12
        VALOR = VALOR + UNITARIO
    elif tamanho == "G" and sabor == "ES":
        DESCRICAO = "ESPECIAL"
        UNITARIO = 21
        VALOR = VALOR + UNITARIO
    elif tamanho == "P" and sabor == "PR":
        DESCRICAO = "PREMIUM"
        UNITARIO = 8
        VALOR = VALOR + UNITARIO
    elif tamanho == "M" and sabor == "PR":
        DESCRICAO = "PREMIUM"
        UNITARIO = 14
        VALOR = VALOR + UNITARIO
    elif tamanho == "G" and sabor == "PR":
        DESCRICAO = "PREMIUM"
        UNITARIO = 24
        VALOR = VALOR + UNITARIO
    else:
        print("!!!!!!!  TAMANHO ou CÓDIGO inválido(s)  !!!!!!!") #retornar essa frase, caso o usuário digite alguma entrada errada
        continue
    print(f"Você pediu um sorvete sabor {DESCRICAO} {tamanho} de R$ {UNITARIO:.2f}") # Descrição do pedido e valor
    print("---------------------------------------------------")
    resposta = input("Deseja pedir mais alguma coisa? (S/N): ")
    if resposta.upper() == "S":
        continue #Se "S" retorna para a linha do while
    print(f"O total a ser pago é: R$ {VALOR:.2f}") # retorna a soma dos pedidos em reais
    break
