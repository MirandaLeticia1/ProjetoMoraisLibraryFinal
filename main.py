import json
from time import sleep
import Biblioteca
import os.path
from Interface import *

with open('livros.json', 'r', encoding='utf8') as json_file:
    objeto = json.loads(json_file.read())
    for i in objeto:
        Biblioteca.livros.append(i)
#LOGIN: admin
#SENHA: admin
Login = Biblioteca.loginSistema()
while True:
    if Login == True:
        print("Acessando a Morais Library...")
        break
    else:
        print("Login ou senha inválidos")
        Login = Biblioteca.loginSistema()

while True:
    resposta = menu(['Gerar Relatórios','Cadastro de novos livros', 'Remover Livros', 'Buscar Livros',
                     'Verificar Status do Livro', 'Importar dados', 'Atualizar quantidade de livros', 'Sair'])
    # Opção de relatório de livros
    if resposta == 1:
        Biblioteca.relatorios()
        
    #Opção para cadastrar um novo livro
    elif resposta == 2:
        cabeçalho('CADASTRO DE NOVOS LIVROS')
        Biblioteca.livros.append(Biblioteca.cadastroLivros())

        with open('livros.json', 'w', encoding='utf-8') as json_file:
            json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)
            print(linha())
            print('LIVRO CADASTRADO COM SUCESSO!')

    #Opção para Remover exemplares
    elif resposta == 3:
        cabeçalho('REMOVER LIVROS')
        opcoes(['Remover por Título','Remover por Ano'])
        tipoRemocao = str(input())
        if tipoRemocao == '1':
            Biblioteca.removerLivrosTitulo()
            with open('livros.json', 'w', encoding='utf-8') as json_file:
                json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)

        elif tipoRemocao == '2':
            Biblioteca.removerLivrosAno()
            with open('livros.json', 'w', encoding='utf-8') as json_file:
                json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)

    #Opção para Buscar livros
    elif resposta == 4:
        Biblioteca.buscarLivros()

    #Opção para verificar status do livro
    elif resposta == 5:
        cabeçalho('VERIFICAR STATUS DO LIVRO')
        Biblioteca.statusLivro()

    #Opcão para importar dados
    elif resposta == 6:
        cabeçalho('IMPORTAR DADOS')
        Biblioteca.importLivros()
        Biblioteca.livros.pop(len(Biblioteca.livros) - 1)

    #Opção para atualizar a quantidade de livros
    elif resposta == 7:
        cabeçalho('ATUALIZAR QUANTIDADE DE LIVROS')
        Biblioteca.atualizarQnt()
        with open('livros.json', 'w', encoding='utf-8') as json_file:
            json.dump(Biblioteca.livros, json_file, indent=1, ensure_ascii=False)

    elif resposta == 8:
        print('Saindo do sistema...')
        break
    else:
        print('ERRO! Digite uma opção válida!')
    sleep(2)
