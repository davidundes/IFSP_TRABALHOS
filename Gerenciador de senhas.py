#Gerenciador de senhas 

def menu():
    while True:
        print("Digite o número da área que deseja acessar: ")
        selecao = int(input("(1)novo serviço \t (2)ver serviços \t (3)atualizar serviço \t(4)buscar serviço (5)excluir serviço (6)sair "))

        match(selecao):
            case 1:
                novoServico()
            case 2:
                verServico()
            case 3:
                atualizarServiço()
            case 4:
                buscarServico()
            case 5:
                excluirServico()
            case 6:
                break
            case _:
                print("Você digitou um valor invalido")

def buscarServico():
    arquivo = open("servicos.txt", mode="r")
    servico = []
    procurar = input("Digite o servico que deseja ")
    
    for linha in arquivo:
        nome = linha.split()

        if procurar == nome[0]:
            servico.append(linha)

    if len(servico) != 0:
        i = 1 
        for linha in servico:
            print(f"{i} {linha}")
            i += 1 
        
    else:
        print("Não existe")

def verServico():
    arquivo = open("servicos.txt")
    for linha in arquivo:
        print(linha.strip())


def novoServico():
    arquivo = open("servicos.txt", mode="r+")
    linhas = arquivo.readlines()

    while True:
        novo = {"nome": input("Digite o nome do serviço"),"login": input("Digite o login"),"senha": input("Digite a senha ")}
        print(novo)
        if  confirmacao():
            break
    linhas.append(f"{novo["nome"]}\t{novo["login"]}\t{novo["senha"]}")

    arquivo.seek(0)

    for linha in linhas:
        arquivo.write(linha + "\n")
    arquivo.truncate

    

def excluirServico():
    arquivo = open("servicos.txt", mode="r+")
    servico = []
    procurar = input("Digite o servico que deseja apagar ")

    for linha in arquivo:
        nome = linha.split()

        if procurar == nome[0]:
            servico.append(linha)

    if len(servico) != 0:
        i = 1 
        for linha in servico:
            print(f"{i} {linha}")
            i += 1 
        indice = int(input("Qual senha voce deseja apagar(digite o indice)?"))
        if confirmacao() == True:
            arquivo.seek(0)
            linhas = arquivo.readlines()
            arquivo =  open("servicos.txt", mode="w")
            for linha in linhas:
                if servico[indice-1] != linha:
                    print(linha)
                    arquivo.write(linha)
            arquivo.truncate()
    else:
        print("Não existe")

def atualizarServiço():
    arquivo = open("servicos.txt", mode="r+")
    servico = []
    procurar = input("Digite o servico que deseja atualizar ")

    for linha in arquivo:
        nome = linha.split()

        if procurar == nome[0]:
            servico.append(linha)

    if len(servico) != 0:
        i = 1 
        for linha in servico:
            print(f"{i} {linha}")
            i += 1 
        indice = int(input("Qual serviço voce deseja atualizar(digite o indice)?"))-1
        if confirmacao() == True:
            campos = servico[indice].split(' ')
            arquivo.seek(0)
            linhas = arquivo.readlines()
            arquivo =  open("servicos.txt", mode="w")
            for linha in linhas:
                if servico[indice] != linha:
                    arquivo.write(linha)
            arquivo.truncate()
            while True:
                print(f"{campos[0]}\t{campos[1]}\t{campos[2]}")
                print("O que você deseja mudar: (1)Serviço (2)Login (3)Senha (4)Sair:")
                selecao = int(input())
                match(selecao):
                    case 1:
                        campos[0] = input("Digite o novo serviço: ")
                    case 2:
                        campos[1] = input("Digite o novo login: ")
                    case 3:
                        campos[2] = input("Digite a nova senha: ")
                    case 4:
                        break
                    case _:
                        print("Valor invalido")
            for i in range(3):
                arquivo.write(campos[i] + " ")
            arquivo.truncate()
    else:
        print("Esse serviço não existe")
                  


    
def confirmacao():
    while True:
        certeza = input("Você tem certeza? (S ou N )").upper()
        if certeza != "S" and certeza != "N":
            print("Você digitou um valor invalido")
            pass
        break
    if certeza == "S":
        return True
    else:
        return False
    
menu()
    
