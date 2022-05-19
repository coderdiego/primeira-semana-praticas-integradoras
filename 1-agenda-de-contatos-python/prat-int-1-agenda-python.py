              #     DIEGO ARAUJO BORGES - SYSOPS - DESCOMPLICA

# Prática Integradora [1]
# Desenvolvimento de um script em Python para a criação de uma agenda de contatos.

def inserir(contatos):
    nome = str(input('Informe o nome: '))
    tel = str(input('Informe o telefone: '))
    email = str(input('Informe o email: '))
    contatos.append((nome, tel, email))

def ordenar(contatos):
    contatos.sort()
    print('Em ordem alfabética ')

def listar(contatos):
    if len(contatos) > 0:
        posicao = int(input('Em qual posição da lista voce quer pesquisar?: '))
        print(contatos[posicao - 1])
    else:
        print('Lista está vazia ...')

def listar_todos(contatos):
    if len(contatos) > 0:
        for x in (contatos):
            print(f'Contato: {x}')
    else:
        print('Lista está vazia ...')

def alterar(contatos):
    if len(contatos) > 0:
        posicao = int(input('Qual posição da lista voce quer alterar? '))
        contatos.pop(posicao - 1)
        nome = str(input('Insira um novo nome: '))
        tel = str(input('Insira um novo telefone: '))
        email = str(input('Insira um nome email: '))
        contatos.append((nome, tel, email))
        print('Contato alterado!')
    else:
        print('Lista está vazia ...')

def excluir(contatos):
    if len(contatos) > 0:
        for x in (contatos):
            print(f'Contato: {x}')
        posicao = int(input('Qual posição da lista voce quer excluir? '))
        contatos.pop(posicao - 1)
        print('Contato foi excluido !!')
    else:
        print('lista está vazia ...')

def excluir_todos(contatos):
    contatos.clear()
    print('Todos os contatos foram excluidos !!')

def exibir_menu():
    print(f''' \n{'='*13} AGENDA DE CONTATOS {'='*13}\nSuas opções
     1. Inserir contato.
     2. Ordenar contatos.
     3. Listar um contato.
     4. Listar todos os contatos.
     5. Alterar um contato.
     6. Excluir um contato.
     7. Excluir todos os contatos.
     8. Sair. \n''')

def main():
    contatos = []
    flag = True
    while flag:
        exibir_menu()
        try:
            opcao = int(input('Escolha uma das opções: '))

            if opcao == 1:
                inserir(contatos)

            elif opcao == 2:
                ordenar(contatos)

            elif opcao == 3:
                listar(contatos)

            elif opcao == 4:
                listar_todos(contatos)

            elif opcao == 5:
                alterar(contatos)

            elif opcao == 6:
                excluir(contatos)

            elif opcao == 7:
                excluir_todos(contatos)

            elif opcao == 8:
                print('Fechando programa ...')
                flag = False
        except ValueError:
            print('Favor digitar somente * NÚMEROS * no campo OPÇÕES')

main()