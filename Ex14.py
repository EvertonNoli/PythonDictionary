#Cadastre filmes com: nome, diretor e genero. Depois,
# organize todos os filmes agrupados por
#genero usando setdefault().


movie = {}
register = []
group = {}

while True:

    movie['name']=str(input('Name: ')).upper()
    movie['director']=str(input('Director: ')).upper()
    movie['gender']=str(input('Gender: ')).upper()
    register.append(movie.copy())

    opt = ' '
    while opt not in 'YN':
        opt=str(input('Do you want to make another register?[Y/N]')).upper().strip()
    if opt == 'N':
        break


print('-='*30)
print('VIDEO STORE')
print('-'*10)
for i, movie in enumerate(register, start=1):
    for k, v in movie.items():
        print(f'{k}: {v}')
    print('-'*10)


print('-='*30)
print('GROUPING BY DIRECTOR')
print('-')

#criar uma variável pra percorrer a lista de filmes
#pegar o valor de "genero" cada vez que a variável percorrer os dicionários de filmes
#usar o setdefault pra garantir a existência do gênero

for film in register:
    gender = film['gender']
    group.setdefault(gender, []).append(film)

for gender, movie in group.items():
    print(f'\nGender: {gender}')
    for m in movie:
        print(f"{m['name']} - {m['director']}")