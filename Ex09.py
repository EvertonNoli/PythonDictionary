#Cadastre produtos com: nome, preco e quantidade vendida. Ao final, calcule:
#O produto com maior faturamento (preco * quantidade)
#O total vendido
#A media de faturamento por produto

produtos = {}
cadastro = []

while True:

    produtos["nome"]=str(input('Nome: ')).upper()
    produtos["preco"]=float(input('Preço: '))
    produtos["vendas"]=int(input('Quantidade venidade: '))
    cadastro.append(produtos.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja cadastrar outro produto?[S/N]')).upper().strip()
    if opc == 'N':
        break

    maior_faturamento = cadastro[0]["preco"]*cadastro[0]["vendas"]
    produto_mais_caro=cadastro[0]
    total = 0
    for p in cadastro:
        faturamento = p["preco"]*p["vendas"]
        if maior_faturamento>faturamento:
            maior_faturamento = p["preco"]*p["vendas"]
            produto_mais_caro = p
        total+=p["preco"]




print('-='*30)
print('PRODUTOS')
for p, produtos in enumerate(cadastro, start=1):
    for k, v in produtos.items():
        print(f'{k}: {v}')
    print('-'*10)

print('FIM DA LISTA')

print(f'O produto com maior faturamento foi {produto_mais_caro["nome"]} com faturamento de R${maior_faturamento:.2f}')
print(f'Total vendido: {total:.2f}')