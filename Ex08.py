#Cadastre varios livros com: titulo, autor e genero. Em seguida, agrupe os livros por autor e mostre
#quais livros cada autor escreveu.

livro = {}
biblioteca = []
grupo = {}

while True:

    livro['titulo']=str(input('Título: ')).upper()
    livro['autor']=str(input('Autor: ')).upper()
    livro['genero']=str(input('Gênero: ')).upper()
    biblioteca.append(livro.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja fazer outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('-='*30)
print('BIBLIOTECA')
for l, livro in enumerate(biblioteca, start=1):
    for k,v in livro.items():
        print(f'{k}: {v}')
    print('-'*10)

print('-='*30)
print('AGRUPAMENTO POR AUTOR')

for livro in biblioteca: #variável livro percorre a lista biblioteca
    autor = livro['autor'] #pega o valor da chave autor de cada vez que a variável livro percorrer a lista biblioteca
    #usa setdefault para garantir a existência do autor na lista do dicionário grupo
    grupo.setdefault(autor, []).append(livro)#se não existir ele cria grupo[autor] e adiciona o livro na lista

for autor, livros in grupo.items(): #grupo é um dicionário onde chave é o nome do autor e valor lista de livros escritos por ele
    #for pecorre cada autor e sua lista de livros
    print(f'\nAutor: {autor}') #imprime o nome do autor atual
    for l in livros: #percorre a lista de livros daquele autor
        print(f"{l['titulo']} - {l['genero']}")