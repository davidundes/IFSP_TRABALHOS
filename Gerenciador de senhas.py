#Gerenciador de senhas 

def menu():
    while True:
        print("Digite o número da área que deseja acessar: ")
        selecao = int(input("(1)novo arquivo \t (2)ver serviços \t (3)atualizar arquivo \t(4)buscar arquivo (5)excluir arquivo (6)sair "))

        match(selecao):
            case 1:
                novoServico()
            case 2:
                verServico()
            case 3:
                pass
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
        novo = {"nome": input("Digite o nome do arquivo"),"login": input("Digite o login"),"senha": input("Digite a senha ")}
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
    
