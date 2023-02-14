"""Module providingFunction printing python version."""
lista_funcionarios = []
ID_FUNCIONARIO = 0
def cadastrar_funcionario(id):
    """Menu cadastrar funcionários"""
    print("**********************************************************************************")
    print("--------------------------- MENU CADASTRAR FUNCIONÁRIO ---------------------------")
    print(f"Código do Funcionário: {id}") #Id exclusivo para cada funcionário
    nome = input("Por favor entre com o NOME: ")
    setor = input("Por favor entre com o SETOR: ")
    salario = float(input("Por favor entre com o SALÁRIO (R$): "))
    dicionario_funcionario = {'id' : id, 'nome' : nome, 'setor' : setor, 'salario' : salario} #Dicionário para armazenar todos os dados do funcionário
    lista_funcionarios.append(dicionario_funcionario.copy())

def consultar_funcionarios():
    """Menu consulta funcionários"""
    while True:
        print("**********************************************************************************")
        print("--------------------------- MENU CONSULTAR FUNCIONÁRIO ---------------------------")
        menu_consulta = input("Escolha a opção desejada:\n1-Consultar todos os Funcionários\n2-Consultar Funcionários por ID\n3-Consultar Funcionários por SETOR\n4-Retornar\n>>") #Menu para consulta dos funcionários
        if menu_consulta == "1": #Se "1" apresentará todos os funcionários cadastrados
            for funcionario in lista_funcionarios:
                print("-------------------------")
                for key, value in funcionario.items():
                    print(f'{key}: {value}')
        elif menu_consulta == "2":
            consulta = int(input("Digite o ID do Funcionário: "))
            for funcionario in lista_funcionarios:
                if funcionario['id'] == consulta:
                    print("-------------------------")
                    for key, value in funcionario.items():
                        print(f'{key}: {value}')
        elif menu_consulta == "3":
            consulta = input("Digite o SETOR do(s) Funcionário(s): ")
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == consulta:
                    print("-------------------------")
                    for key, value in funcionario.items():
                        print(f'{key}: {value}')
        elif menu_consulta == "4":
            return #Retorna para main
        else:
            print("Opção Inválida. Tente Novamente")
            continue

def remover_funcionario():
    """Menu remover funcionário"""
    print("**********************************************************************************")
    print("---------------------------- MENU REMOVER FUNCIONÁRIO ----------------------------")
    consulta = int(input("Digite o ID do Funcionário a ser Removido: "))
    for funcionario in lista_funcionarios:
        if funcionario['id'] == consulta:
            lista_funcionarios.remove(funcionario) #Remover funcionário
            print("Funcionário Removido")

print("Bem vindo ao Controle de Funcionários do José Wellington de Lima Bezerra")
while True:
    print("**********************************************************************************")
    print("--------------------------------- MENU PRINCIPAL ---------------------------------")
    menu_principal = input("Escolha a opção desejada:\n1-Cadastrar Funcionário\n2-Consultar Funcionário(s)\n3-Remover Funcionário\n4-Sair\n>>")
    if menu_principal == "1":
        ID_FUNCIONARIO = ID_FUNCIONARIO + 1 #Contador para controle de funcionários por ID exclusivo
        cadastrar_funcionario(ID_FUNCIONARIO) #Chama a Função
    elif menu_principal == "2":
        consultar_funcionarios()
    elif menu_principal == "3":
        remover_funcionario()
    elif menu_principal == "4":
        break
    else:
        print("Opção Inválida. Tente Novamente")
        continue #Retorna para linha do while