pessoa = {}
cadastro = []

while True:

    pessoa['nome']=str(input('Digite o nome:')).upper().strip()
    pessoa['idade']=int(input('Digite a idade:'))
    cadastro.append(pessoa.copy())

    menor18 = 0
    for p in cadastro:
        if p['idade']<18:
            menor18+=1

    percentual = (menor18/len(cadastro))*100

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-'*30)
print('Cadastro de Pessoas')

for i, pessoa in enumerate(cadastro, start=1):
    for k, v in pessoa.items():
        print(f'{k}:{v}')
    print('-'*10)

print(f'Foram cadastradas {menor18} menores de 18 anos um percentual de {percentual:.2f}% dos cadastros')