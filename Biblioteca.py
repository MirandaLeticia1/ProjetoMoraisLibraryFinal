import os.path
import json
from Interface import *


def linha(tam = 50):
    return '-' * tam
livros = []

def cadastroConta():
    loginFuncionario = 'admin'
    senhaFuncionario = 'admin'
    return {'login': loginFuncionario, 'senha': senhaFuncionario}

def loginSistema():
    while True:
        login = str(input("Login: "))
        senha = str(input("Senha: "))
        if login == cadastroConta()['login'] and senha == cadastroConta()['senha']:
            return True
        else:
            print("Login ou senha inválida, tente novamente")

#Função para cadastrar novos livros
def cadastroLivros():

    titulo = input("Digite o titulo do livro: ").title().strip()
    autor = input("Digite o autor do livro: ").title().strip()
    ano = input("Digite o ano do livro: ").strip()
    quantidade = input("Digite a quantidade de exemplares: ").strip()
    tematica = input("Qual o tema do livro: ").title().strip()
    categoria = input("Livro fisico ou digital: ").title().strip()
    reservavel= input("Livro pode ser reservado? (S/N): ")[0].strip().lower()

    return {'titulo': titulo, 'autor': autor, 'ano': ano, 'quantidade': quantidade,
            'tematica': tematica,'categoria': categoria, 'reservavel': reservavel}

#Função para remover livros do sistema por título
def removerLivrosTitulo():
    livroExiste = True
    removerLivro = str(input("Digite o titulo do livro que deseja remover: ")).title().strip()
    for i in livros:
        if i['titulo'] == removerLivro:
            livroExiste = True
            livros.remove(i)
            print(linha())
            print('Livro removido com sucesso!')
            print(linha())
        else:
            livroExiste = False
    if livroExiste == False:
        print(linha())
        print("Não existe livro com esse título na Biblioteca!")
        print(linha())


# Função para remover livros do sistema por ano
def removerLivrosAno():
    livroExiste = True
    removerLivro = str(input("Digite o titulo do livro que deseja remover: ")).title().strip()
    for i in livros:
        if i['ano'] == removerLivro:
            livroExiste = True
            livros.remove(i)
            print(linha())
            print('Livro removido com sucesso!')
            print(linha())
        else:
            livroExiste = False
    if livroExiste == False:
        print(linha())
        print("Não existe livro com esse ano na Biblioteca!")
        print(linha())


#Função para buscar Livros
def buscarLivros():
    livroExiste = True
    opcoes(["Buscar por titulo", "Buscar por ano", "Buscar por categoria", "Buscar por tema"])
    opcaoBusca = int(input("Digite a opção: "))
    if opcaoBusca == 1:
        nomeLivro = str(input("Titulo: ")).title().strip()
        for i in livros:
            if i["titulo"] == nomeLivro:
                print(i)
                livroExiste = True
            else:
                livroExiste = False
        if livroExiste == False:
            print("Não foi encontrado livro com esse titulo")

    if opcaoBusca == 2:
        anoLivro = str(input("Ano: "))
        for i in livros:
            if i["ano"] == anoLivro:
                print(i)
                livroExiste = True
            else:
                livroExiste = False
        if livroExiste == False:
            print("Não foi encontrado livro com esse ano de lançamento")

    if opcaoBusca == 3:
        catLivro = str(input("Categoria (Fisico ou Digital): ")).title().strip()
        for i in livros:
            if i["categoria"] == catLivro:
                print(i)
                livroExiste = True
            else:
                livroExiste = False
        if livroExiste == False:
            print("Não foi encontrado livro com essa categoria")

    if opcaoBusca == 4:
        temaLivro = str(input("Tematica: ")).title().strip()
        for i in livros:
            if i["tematica"] == temaLivro:
                print(i)
                livroExiste = True
            else:
                livroExiste = False
        if livroExiste == False:
            print("Não foi encontrado livro com essa temática")


#Função para atualizar a quantidade de um livro
def atualizarQnt():
    livroExiste = True
    nomeLivro = str(input("Digite o titulo do livro que deseja atualizar a quantidade: ")).title().strip()
    quantLivro = int(input("Nova quantidade: "))
    for i in livros:
        if i['titulo'] == nomeLivro:
            i["quantidade"] = quantLivro
            print(linha())
            print('Quantidade atualizada com sucesso!')
            print(linha())
            livroExiste = True
        else:
            livroExiste = False
    if livroExiste == False:
        print(linha())
        print("Não existe livro com esse título na Biblioteca!")
        print(linha())

#Função para importar arquivos de livros
def importLivros():
    arq = str(input("Digite o nome do arquivo .json"))
    if os.path.exists(arq) == True:
        with open(arq, 'r', encoding='utf8') as json_file:
            objeto = json.loads(json_file.read())
            for i in objeto:
                livros.append(i)

            print("Dados importados")
    else:
        print("Arquivo não localizado")

#Função para saber o status de um livro
def statusLivro():
    livroExiste = True
    nomeLivro = str(input("Digite o titulo do livro que deseja verificar: ")).title().strip()
    for i in livros:
        if i["titulo"] == nomeLivro:
            quantLivros = i["quantidade"]
            catLivro = i['categoria']
            if i['reservavel'] == 's':
                print(f"- O livro {nomeLivro} pode ser reservado")
            elif i['reservavel'] == 'n':
                print(f"- O livro {nomeLivro} não pode ser alugado, deve ser lido apenas na biblioteca")
            print(f'- Atualmente há {quantLivros} unidades deste livro disponíveis na biblioteca')
            print(f'- O livro {nomeLivro} está na categoria {catLivro}')
        else:
            livroExiste = False
    if livroExiste == False:
        print("Livro não localizado na Biblioteca!")

#Função para gerar relatórios
def relatorios():
    livroExiste = True
    relatorioCriado = False
    print(linha())
    opcoes(["Relatório Acervo", "Relatório por categoria", "Relatório por temática"])
    opcao = int(input("Digite a opção: "))
    if opcao == 1:
        relatorio = open('relatorioAcervo.txt', 'w', encoding="utf8")
        relatorio.writelines('RELATÓRIO COMPLETO DO ACERVO'.center(50, " ") + "\n")
        for i in livros:
            relatorio.write("-*-" * 20 + "\n")
            relatorio.write(f"Livro: {i['titulo']}\n" +
                            f"Ano: {i['ano']}\n" +
                            f"Autor: {i['autor']}\n" +
                            f"Quantidade de exemplares: {i['quantidade']}\n" +
                            f"Categoria: {i['categoria']}\n" +
                            f"Tema: {i['tematica']}\n" +
                            f"O livro pode ser reservado?: {i['reservavel']}\n")
        relatorio.close()
        print('Relatório gerado com sucesso!')

    elif opcao == 2:
        catLivro = str(input("Qual a categoria do livro: (Fisico ou Digital?) ")).title().strip()
        for i in livros:
            if i['categoria'] == catLivro and relatorioCriado == False:
                print("Relatório criado com sucesso!")
                relatorio = open(f'relatorioCategoria{catLivro}.txt', 'w', encoding="utf8")
                relatorio.writelines('RELATÓRIO POR CATEGORIA'.center(50, " ") + "\n")
                relatorio.writelines(f'CATEGORIA: Livros disponíveis do tipo {catLivro}'.center(50, " ") + "\n")
                relatorioCriado = True
            if i['categoria'] == catLivro:
                relatorio.write("-*-" * 20 + "\n")
                relatorio.write(f"Livro: {i['titulo']}\n" +
                                f"Ano: {i['ano']}\n" +
                                f"Autor: {i['autor']}\n" +
                                f"Quantidade de exemplares: {i['quantidade']}\n" +
                                f"Categoria: {i['categoria']}\n" +
                                f"Tema: {i['tematica']}\n" +
                                f"O livro pode ser reservado?: {i['reservavel']}\n")
            else:
                livroExiste = False

        if livroExiste == False:
            print("Não foi encontrado livro dessa categoria! ")


    elif opcao == 3:
        temaLivro = str(input("Tema: ")).title().strip()
        for i in livros:
            if i['tematica'] == temaLivro and relatorioCriado == False:
                print("Relatório criado com sucesso!")
                relatorio = open(f'relatorioTema{temaLivro}.txt', 'w', encoding="utf8")
                relatorio.writelines('RELATÓRIO POR TEMÁTICA'.center(50, " ") + "\n")
                relatorio.writelines(F'LIVROS DA CATEGORIA: {temaLivro}'.center(50, " ") + "\n")
                relatorioCriado = True
            if i['tematica'] == temaLivro:
                relatorio.write("-*-" * 20 + "\n")
                relatorio.write(f"Livro: {i['titulo']}\n" +
                                f"Ano: {i['ano']}\n" +
                                f"Autor: {i['autor']}\n" +
                                f"Quantidade de livros existentes: {i['quantidade']}\n" +
                                f"Categoria: {i['categoria']}\n" +
                                f"Tema: {i['tematica']}\n" +
                                f"O livro pode ser reservado?: {i['reservavel']}\n")
            else:
                livroExiste = False
        if livroExiste == False:
            print("Não foram localizados livros com esse tema na Biblioteca!")
    else:
        print("Opção inválida")