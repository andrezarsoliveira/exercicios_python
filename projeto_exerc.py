# Quero opção de:
# Adicionar doce
# Exibir detalhe de um doce
# Atualizar doce
# Apagar doces
# Exibir a lista de todos os doces

#import time Foi removido pois está relacionado a tempo, como medir, manipular etc.

lista_produtos = [{'id': 3, 'nome': 'asdasdas', 'preço': 32.0}, {'id': 2, 'nome': 'asd', 'preço': 2.0}, {'id': 1, 'nome': 'a', 'preço': 1.0}, {'id': 4, 'nome': '23123', 'preço': 13123.0}]

#def para definir funções, em que se realiza uma tarefa específica e pode ser reutilizada 
id_produto = 1
def menu():   
    while True:
        print("\n ** MENU LOJA REPROGRAMA **\n")
        print("1 - Adicionar")
        print("2 - Exibir detalhes")
        print("3 - Atualizar")
        print("4 - Apagar")
        print("5 - Exibir todos")
        print("0 - Sair")

        opcao = input("Escolha a opção desejada:\n")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            exibir_detalhes()
        elif opcao == "3":
            atualizar_produto()
        elif opcao == "4":
            delete()
        elif opcao == "5":
            listar_todos()
        elif opcao == "0":
            break
        else:
            print("Opção inválida, por favor escolha uma opção do menu")
#break para parar o loop

def gerar_id_produto():
    if len(lista_produtos) == 0:
        return 1
    lista_produtos.sort(key=lambda produto: produto.get("id"), reverse=True)
    novo_id = lista_produtos[0].get("id") + 1

#lambda é uma função simples
#reverse inverte a ordem dos elementos

    return novo_id
def adicionar_produto():
    nome_produto = input("Digite o nome do produto:\n")
    preco_produto = input("Digite o preço do produto:\n")

    produto = {
        "id": gerar_id_produto(),
        "nome": nome_produto,
        "preço": float(preco_produto),
    }
    lista_produtos.append(produto)

    print(lista_produtos)

#float está sendo usado pois o preço do produto pode ser um número real


def atualizar_produto():
    id_produto = input("Digite o ID do produto para atualizar:\n")

    for index in range(len(lista_produtos)):
        if lista_produtos[index].get("id") == int(id_produto):
            novo_valor = input("Digite o novo valor do produto:\n")
            lista_produtos[index]["preço"] = float(novo_valor)
            print(f"O produto foi atualizado com sucesso! {lista_produtos[index]}")
            #print(f"...") Dentro do texto para aparecer o valor da variável
            #get Para buscar no dicionário


def listar_todos():
    for index in range(len(lista_produtos)):
        print(f"{lista_produtos[index]}\n")


def exibir_detalhes():
    exibir_item = int(input("Digite a id:"))
    
    for index in lista_produtos:  
        if exibir_item == index.get("id"): 
           print(f"{index}")
      
def delete():
    deletar_produto = int(input("Digite id que deseja deletar:"))

    for index in range(len(lista_produtos)): 
        if index < len(lista_produtos):     
            if lista_produtos[index].get("id") == deletar_produto:
                lista_produtos.pop(index)   
                print("O produto foi excluído com sucesso!")       

#range número de vezes que o for vai rodar
#len igual a quantidade/tamanho
#index preenche com o tamanho da lista e encontra dentro da lista a "id"
#pop para deletar o item digitado

menu()