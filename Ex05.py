produtos = {}
cadastro = []

while True:

    produtos['nome'] = str(input('Digite o nome: ')).upper()
    produtos['preco'] = float(input('Digite o preço: '))
    cadastro.append(produtos.copy())

    barato = caro = cadastro[0]
    for p in cadastro:
        if p['preco']>caro['preco']:
            caro=p
        if p['preco']<barato['preco']:
            barato = p

    for p in cadastro:
        total = sum(p['preco'] for p in cadastro)


    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-'*30)
print('Cadastro de Produtos')

for i, produtos in enumerate(cadastro, start=1):
    for k, v in produtos.items():
        print(f'{k}:{v}')
    print('-'*10)

print(f'O produto mais caro é {caro["nome"]} custando {caro["preco"]}R$ e o mais barato é {barato["nome"]} custando {barato["preco"]} R$')
print(f'Total vendido: R${total:.2f}')