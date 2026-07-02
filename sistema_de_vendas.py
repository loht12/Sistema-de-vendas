estoque_produtos = {
    1 : {"nome":"Biquini cortininha com calcinha lateral larga","preco": 145.00,"quantidade": 60},
    2 : {"nome":"Biquini Cortininha com calcinha fio","preco": 145.00,"quantidade": 60},
    3 : {"nome":"Biquini Cortininha com calcinha basica","preco": 145.00,"quantidade": 60},
    4 : {"nome":"Biquini Cortininha com calcinha asa delta","preco": 145.00,"quantidade": 60},
    5 : {"nome":"Biquini meia taca com calcinha lacinho","preco": 295.00,"quantidade": 45},
    6: {"nome": "Biquini meia taca com calcinha asa delta", "preco": 295.00, "quantidade": 45},
    7 : {"nome":"Biquini meia taca com calcinha lateral larga","preco": 295.00,"quantidade": 45},
    8 : {"nome":"Biquini meia taca com calcinha basica","preco": 295.00,"quantidade": 45},
    9 : {"nome":"Biquini top com calcinha basica","preco": 195.00,"quantidade": 60},
    10 : {"nome":"Biquini top com calcinha lateral larga ","preco": 195.00,"quantidade": 60},
    11 : {"nome":"Biquini top com calcinha fio","preco": 195.00,"quantidade": 60},
    12 : {"nome":"Biquini top com calcinha lacinho","preco": 195.00,"quantidade": 60},
    13: {"nome": "Biquini marquinha com calcinha fio", "preco": 160.00, "quantidade": 40},
}
carrinho = []

while True:
    print("*" * 30)
    print("Seja bem vindo a Biquinis da Loh")
    print("*" * 30)
    print("[1] Vizualizar estoque.")
    print("[2] Adicionar item ao carrinho.")
    print("[3] Vizualizar Carrinho.")
    print("[4] Finalizar compra.")
    print("[5] Sair do sistema.")

    opcao = int(input("Escolha uma opcão:"))

    if opcao == 1:
        print("Vizualisar estoque!")
        for chave, valor in estoque_produtos.items():
            print(f"{chave}:{valor}")
    elif opcao == 2:
        print("Adicionando itens ao carrinho!")
        id_produto= int(input("Digite o id do produto:"))
        if id_produto in estoque_produtos:
            qtd_produto = int(input("Quantas unidades:"))
            if qtd_produto <= 0:
             print("Quantidade invalida!")
            elif qtd_produto <= estoque_produtos[id_produto]["quantidade"]:
             item = {
                "qtd" : qtd_produto,
                "nome" : estoque_produtos[id_produto]["nome"],
                "preco" : estoque_produtos[id_produto]["preco"],
                "preco_total" : qtd_produto * estoque_produtos[id_produto]["preco"],
            }
            carrinho.append(item)
            estoque_produtos[id_produto]['quantidade'] -= qtd_produto
    elif opcao == 3:(
         print("Vizualisando carrinho!"))
    elif opcao == 4:
        print("Finalizando compra!")
    elif opcao == 5:
        print ("Saindo do sistema!")
        break
    else:
        print ("ERRO, opcao inexistente!")


