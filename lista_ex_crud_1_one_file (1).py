l_nomes = []        # Lista vazia, variável global (todas as funções usam)
def menu():
    print('[c] - Create')
    print('[r] - Read')
    print('[u] - Update')
    print('[d] - Delete')
    print('[e] - Exit')
    opcao = input('Opção: ')
    return opcao
def create():
    nome = input('Inserir - Nome: ')
    l_nomes.append(nome)
def read():
    print("Valores da lista na horizontal:")
    print(l_nomes)                # Na horizontal
def update():
    indice = int(input("Atualizar - Qual posição (índice): "))
    novo_nome = input("Atualizar - Novo nome: ")
    # Usando notação de vetor:  Sintaxe: nome_lista[indice] = novo_nome
    l_nomes[indice] = novo_nome          # Solução 1, notação vetor.
    # l_nomes.pop(indice)                # Solução 2, funções de lista.
    # l_nomes.insert(indice, novo_nome)  # Solução 2
def delete():
    nome = input("Remover - Nome: ")
    l_nomes.remove(nome)
if __name__ == '__main__':  # Atalho: mai <tab>
    while True:  # Solução 2
        op = menu()  # A variável op recebe o valor da função menu
        if op == 'c':
            create()  # Chama a função create
        elif op == 'r':
            read()  # Chama a função read
        elif op == 'u':
            update()  # Chama a função update
        elif op == 'd':
            delete()  # Chama a função delete
        else:
            break

"""
def create():                             # Original
    n = input('Nome: ')
    lista.append(n)

- Alteração a função create:
- Permitir que o usuário digite vários nomes, digite a tecla "enter" para
sair do create
- Dica: estrutura de repetição.

--- Dicas:

def create():
    while True:
        n = input('Nome: ')
        if n == "":             # Enter
            break
        l_nomes.append(n)

---

    # - Solução 2:
    funcao = {'c': create, 'r': read, 'u': update, 'd': delete}  # Dicionário
    while True:
        op = menu()             # A variável op recebe o valor da função menu
        if op in ('c', 'r', 'u', 'd'):
            funcao[op]()
        else:
            break

"""
