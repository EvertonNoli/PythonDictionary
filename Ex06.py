livros = {}
biblioteca = []

while True:

    livros['nome']=str(input('Digite o nome: ')).upper()
    livros['autor']=str(input('Digite o autor: ')).upper()
    livros['genero']=str(input('Digite o gênero: ')).upper()
    biblioteca.append(livros.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc=='N':
        break


print('-'*30)
print('BIBLIOTECA')
for l, livros in enumerate(biblioteca, start=1):
    for k, v in livros.items():
        print(f'{k}: {v}')
    print('-'*10)

busca = str(input('Qual gênero deseja retornar?: ')).upper().strip()
encontrado = False
for l in biblioteca:
    if l['genero']==busca:
        print(f'{l["nome"]}: {l["autor"]}')
        encontrado = True
if not encontrado:
    print('Gênero não encontrado!')