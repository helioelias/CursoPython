for i in range(10):
    print(i)

for i in range(1, 100, 7):
    print(i)

for i in range(20, 0, -3):
    print(i)

produto = {
    'nome': 'Caneta',
    'preco': 8.80,
    'desc': 0.5
}

for atrib in produto:
    print(atrib, produto[atrib])

for valor in produto.values():
    print(valor, end= ' ')

for valor in produto.keys():
    print(valor, end= ' ')