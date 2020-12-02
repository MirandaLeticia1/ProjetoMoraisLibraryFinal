#Função para ler um número inteiro
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('Erro: Por favor Digite um número válido')
            continue
        except (KeyboardInterrupt):
            print('Usuário não digitou o número')
            return 0
        else:
            return n

#Função para criar uma linha
def linha(tam = 50):
    return '-' * tam

#Função para criar um cabeçalho
def cabeçalho(txt):
    print(linha())
    print(txt.center(50))
    print(linha())

#Função para exibir opções do menu
def menu(lista):
    cabeçalho('BEM VINDO AO MORAIS LIBRARY')
    print('MENU PRINCIPAL:')
    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c += 1
    print(linha())
    opcao = leiaInt('Sua opção:')
    return opcao

def opcoes(lista):
    print('OPÇÕES')
    c = 1
    for item in lista:
        print(f' {c} - {item}')
        c += 1
    print(linha())