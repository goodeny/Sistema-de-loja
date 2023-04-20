class Produto:
    produtos = []
    def __init__(self):
        pass
    
    def add_produto(self, nome, descricao, preco):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

        Produto.produtos.append([self.nome, self.descricao, self.preco])
        print(f"Produto adicionado! Nome: {self.nome}")
    
    def listar_produtos(self):
        if Produto.produtos == []:
            print("Nenhum produto adicionado!")
        else:
            self.atualizar_produtos()

    def deletar_produto(self, id):
        if Produto.produtos == []:
            print("Nenhum produto adicionado!")
        else:
            try:
                print(f"Produto removido! ID: {id} Nome: {Produto.produtos[id-1][0]}")
                Produto.produtos.pop(id-1)
                self.atualizar_produtos()
            except:
                print("ID do produto não encontrado!")

    def atualizar_produtos(self):
        id = 0
        for i in Produto.produtos:
            id += 1
            print(f"ID: {id}", f"\nNome do produto: {i[0]}", f"\nDescrição do produto: {i[1]}", f"\nPreco: R$: {round(i[2],2)}" )

    def renomear_nome_produto(self, id):
        try:
            nome = input("Digite o novo nome do produto: ")
            Produto.produtos[id-1][0] = nome
        except:
            print("Produto não encontrado!")
    
    def renomear_descricao_produto(self, id):
        try:
            descricao = input("Digite a nova descrição do produto: ")
            Produto.produtos[id-1][1] = descricao
        except:
            print("Produto não encontrado!")

    def renomear_preco_produto(self, id):
        try:
            preco = float(input("Digite o novo preço do produto: "))
            Produto.produtos[id-1][2] = preco
        except:
            print("Produto não encontrado!")
class Pedido:
    def __init__(self):
        valortotal = 0
        for i in Carrinho.itens:
            valortotal += i[2]
        print(f"O valor total do seu carrinho é: {valortotal}")

class Carrinho:
    itens = []
    def __init__(self):
        pass

    def adicionar_carrinho(self, id):
        try:
            Carrinho.itens.append(Produto.produtos[id-1])
        except:
            print("Produto não encontrado")
    
    def mostrar_carrinho(self):
        if Carrinho.itens == []:
            print("Carrinho vazio!")
        else:
            for i in Carrinho.itens:
                print(i)
    
    def esvaziar_carrinho(self):
        if Carrinho.itens == []:
            print("Você não adicionou nenhum produto ainda!")
        else:
            Carrinho.itens.clear()

class Sistema:
    def __init__(self):
        import os
        self.produto1 = Produto()
        self.carrinho = Carrinho()
        while(True):
            print("Adicionar produto [1] - Fazer pedido [2]\nFinalizar Compra [3] - Deletar produto [4]\nEditar produtos [5]" )
            res = int(input("Opção: "))
            if res == 1:
                os.system("cls")
                nome = input("Nome do produto: ")
                descricao = input("Descricao do produto: ")
                preco = float(input("Preço do produto: "))
                self.produto1.add_produto(nome, descricao, preco)
            elif res == 2:
                print("Listar produtos [1] - Adicionar ao carrinho [2]\nMostrar Carrinho [3] - Esvaziar Carrinho [4]")
                res = int(input("Opção: "))
                if res == 1:
                    self.produto1.listar_produtos()
                elif res == 2:
                    id = int(input("ID do produto: "))
                    self.carrinho.adicionar_carrinho(id)
                    self.carrinho.mostrar_carrinho()
                elif res == 3:
                    self.carrinho.mostrar_carrinho()
                elif res == 4:
                    self.carrinho.esvaziar_carrinho()
            elif res == 3:
                Pedido()
            
            elif res == 4:
                id = int(input("ID do produto: "))
                self.produto1.deletar_produto(id)
            
            elif res == 5:
                if Produto.produtos == []:
                    print("Nenhum produto adicionado!")
                else:
                    print("Editar nome do produto [1] - Editar descrição do produto [2]\nEditar preço do produto [3]")
                    res = int(input("Opção: "))
                    if res == 1:
                        id = int(input("ID do produto: "))
                        self.produto1.renomear_nome_produto(id)
                    elif res == 2:
                        id = int(input("ID do produto: "))
                        self.produto1.renomear_descricao_produto(id)
                    elif res == 3:
                        id = int(input("ID do produto: "))
                        self.produto1.renomear_preco_produto(id)

if __name__ == "__main__":
    Sistema()

