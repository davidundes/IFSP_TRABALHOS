#Gerenciador de senhas 

def menu():
    while True:
        print("Digite o número da área que deseja acessar: ")
        selecao = input("(1)novo serviço \t (2)ver serviços \t (3)atualizar serviço \t(4)buscar serviço (5)excluir serviço (6)sair ")

        match(selecao):
            case '1':
                novoServico()
            case '2':
                verServico()
            case '3':
                atualizarServiço()
            case '4':
                buscarServico()
            case '5':
                excluirServico()
            case '6':
                break
            case _:
                print("Você digitou um valor invalido")

def buscarServico():
    arquivo = open("servicos.txt", mode="r", encoding="utf-8")
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
    arquivo.close()

def verServico():
    arquivo = open("servicos.txt", encoding="utf-8")
    for linha in arquivo:
        print(linha.strip())
    arquivo.close()


def novoServico():
    arquivo = open("servicos.txt", mode="a", encoding="utf-8")

    while True:
        novo = {"nome": input("Digite o nome do serviço "),"login": input("Digite o login "),"senha": input("Digite a senha ")}
        print(novo)
        if  confirmacao():
            break
    linha = (f"{novo['nome']}\t{novo['login']}\t{novo['senha']}\n")

    arquivo.write(linha)
    arquivo.truncate()
    arquivo.close()

    

def excluirServico():
    arquivo = open('servicos.txt', mode="r", encoding="utf-8")
    campos = pesquisa("excluir")
    arquivo.seek(0)
    linhas = arquivo.readlines()
    arquivo =  open("servicos.txt", mode="w", encoding="utf-8")
    for linha in linhas:
        if campos != linha:
            arquivo.write(linha)
    arquivo.truncate()
    arquivo.close()

def atualizarServiço():
    arquivo = open('servicos.txt', mode="r", encoding="utf-8")
    campos = pesquisa("atualizar")
    if campos == 0:
        return 0 
    arquivo.seek(0)
    linhas = arquivo.readlines()
    arquivo =  open("servicos.txt", mode="w", encoding="utf-8")
    for linha in linhas:
        if campos != linha:
            arquivo.write(linha)
    arquivo.truncate()
    campos = campos.split()
    print(campos)
    while True:
        print(f"{campos[0]}\t{campos[1]}\t{campos[2]}")
        print("O que você deseja mudar: (1)Serviço (2)Login (3)Senha (4)Sair:")
        try:
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
        except:
            print('Valor inválido digitado.')
    for i in range(3):
        arquivo.write(campos[i] + "\t")
    arquivo.write("\n")
    arquivo.truncate()
    arquivo.close()
                  

def pesquisa(tipo):
    arquivo = open("servicos.txt", mode="r+", encoding="utf-8")
    servico = []
    procurar = input(f"Digite o servico que deseja {tipo} ")

    for linha in arquivo:
        nome = linha.split()
        if procurar == nome[0]:
            servico.append(linha)
        
    if len(servico) != 0:
        while True:
            i = 1 
            for linha in servico:
                print(f"{i} {linha}")
                i += 1 
            try:
                indice = int(input("Qual serviço voce deseja atualizar(digite o indice)?"))-1
                if confirmacao() == True:
                    return servico[indice]
            except:
                print('Valor inválido digitado.')    
    else:
        print("Este serviço não existe\n")
        return 0
    arquivo.close()

    
def confirmacao():
    while True:
        certeza = input("Você tem certeza? (S ou N )").upper()
        if certeza != "S" and certeza != "N":
            print("Você digitou um valor invalido")
            continue
        break
    if certeza == "S":
        return True
    else:
        return False
    
menu()
    
