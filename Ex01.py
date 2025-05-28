#Crie um programa que leia o nome, idade e cidade de uma pessoa
# e armazene essas informações em um dicionário. Depois, mostre os dados.

pessoa = {}
cadastro = []

while True:

    pessoa['nome'] = str(input('Digite o nome:')).upper()
    pessoa['idade']=int(input('Digite a idade:'))
    pessoa['cidade']=str(input('Digite a cidade:')).upper()
    cadastro.append(pessoa.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break


print('-'*30)
print('Cadastro de pessoas')
for p, pessoa in enumerate(cadastro, start=1):
    for k, v in pessoa.items():
        print(f'{k}:{v}')
    print('-'*30)