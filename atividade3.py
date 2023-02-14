"""Module providingFunction printing python version."""
def metragem_limpeza(): #Função para definir a metragem
    """Função metragem"""
    print("**********************************************************************************")
    print("--------------------Menu 1 de 3 - Metragem Limpeza--------------------------------") #Menu
    while True:
        try:
            metragem = int(input("Entre com a metragem da casa: ")) #Variável metragem receberá dado do usuário
            if 30 <= metragem < 300:
                print("Será necessário um(a) funcionário(a) para a limpeza")
                return 60 + 0.3 * metragem
            elif 300 <= metragem < 700:
                print("Seram necessários(as) dois(duas) funcionários(as) para a limpeza")
                return 120 + 0.5 * metragem
            else:
                print("!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!") #Caso o usuário digite um dado não aceito
            continue
        except ValueError:
            print("Favor não digitar um valor não numérico e tente novamente!")
            continue
def tipo_limpeza(): #Função para definir o tipo de limpeza
    """Função tipo Limpeza"""
    print("**********************************************************************************")
    print("--------------------Menu 2 de 3 - Tipo de Limpeza---------------------------------")
    while True:
        modelo = input("Entre com o tipo de limpeza:\n"+"B - BÁSICA - Indicado para sujeiras semanais ou quinzenais\n"+"C - COMPLETA (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras\n").upper()
        if modelo == "B":
            print("Você selecionou a limpeza BÁSICA")
            return 1.00
        elif modelo == "C":
            print("Você selecionou a limpeza COMPLETA")
            return 1.30
        else:
            print("!!!!!!!  Opçãp Inválida  !!!!!!!")
        continue

def adicional_limpeza(): #Função para verificar se deseja adicional
    """Função Adicional Limpeza"""
    print("**********************************************************************************")
    print("--------------------Menu 3 de 3 - Adicional de Limpeza----------------------------")
    valor_adicional = 0.00
    while True:
        try:
            add = int(input("Deseja mais algum adicional?\n"+"0- Não desejo mais nada (encerrar)\n"+"1- Passar 10 peças de roupas - R$ 10,00\n"+"2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n"+"3- Limpeza de 1 Geladeira/Freezer - R$ 20,00\n"+">>"))
            if add == 0:
                return valor_adicional
            if add == 1:
                valor_adicional = valor_adicional + 10
            elif add == 2:
                valor_adicional = valor_adicional + 12
            elif add == 3:
                valor_adicional = valor_adicional + 20
            else:
                print("Digite apenas uma das opções válidas")
            continue
        except ValueError:
            print("Favor não digitar um valor não numérico e tente novamente!")
            continue


print("Bem vindo a Sorveteria do José Wellington de Lima Bezerra")

metra = metragem_limpeza() #Armazenada a função em uma variável
TIPO = tipo_limpeza()
ADICIONAL = adicional_limpeza()
TOTAL = metra * TIPO + ADICIONAL

print("**********************************************************************************")
print(f"TOTAL: R$ {TOTAL:.2f} (metragem: {metra:.2f} * tipo: {TIPO:.2f} + adicional: {ADICIONAL:.2f})") # Resultado
print("**********************************************************************************")
