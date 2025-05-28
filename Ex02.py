#Faca um programa que cadastre varias pessoas. Cada pessoa deve ser um dicionario com nome e
#idade. Guarde esses dicionarios em uma lista. Ao final, mostre todos os cadastros.

pessoa = {}
cadastro = []

while True:

    pessoa['nome']=str(input('Digite o nome:')).upper()
    pessoa['idade']=str(input('Digite a idade:'))
    cadastro.append(pessoa.copy())


    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja reralizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-'*30)
print('Cadastro de Pessoas')

for i, pessoa in enumerate(cadastro, start=1):
    for k, v in pessoa.items():
        print(f'{k}:{v}')
    print('-'*10)
