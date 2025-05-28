pessoa = {}
cadastro = []

while True:

    pessoa['nome']=str(input('Digite o nome:')).upper()
    pessoa['idade']=int(input('Digite a idade:'))
    cadastro.append(pessoa.copy())

    mais_velha=cadastro[0]

    for pessoa in cadastro[1:]:
        if pessoa['idade']>mais_velha['idade']:
            mais_velha=pessoa['idade']

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-'*30)
print('Cadastro de Pessoas')

for i,pessoa in enumerate(cadastro, start=1):
    for k, v in pessoa.items():
        print(f'{k}:{v}')
    print('-'*10)

print(f'A pessoa mais velha é {mais_velha['nome']} com {mais_velha['idade']} anos')