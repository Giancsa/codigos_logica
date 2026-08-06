produtos = [{"nome": "queijo",
           "codigo": "1234",
           "quantidade": "10",
           "preco": "10.99",
           "categoria":"frios",
           },
           {"nome": "camisa",
           "codigo": "12345",
           "quantidade": "15",
           "preco": "19,99",
           "categoria":"vestuario",
           },
           {"nome": "arroz",
           "codigo": "123456",
           "quantidade": "20",
           "preco": "4,99",
           "categoria":"nao_pereciveis",
           },]
print(produtos[1])

for produto in produtos:
    print(f"{produto["nome"]} - R${produto["preco"]}")