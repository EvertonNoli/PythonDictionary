#Cadastre varios jogadores com: nome, posicao, time. Depois, peca ao usuario um nome e procure
#por esse jogador na lista. Se encontrar, mostre todos os dados dele. Se nao, informe que nao foi
#encontrado.

player = {}
register = []

while True:

    player['name']=str(input('Name: ')).upper()
    player['position']=str(input('Position: ')).upper()
    player['club']=str(input('Club: ')).upper()
    register.append(player.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Do you wish to make another register?[Y/N]')).upper().strip()
    if opt == 'N':
        break

print('-='*30)
print('PLAYERS REGISTERED')
for i, player in enumerate(register, start=1):
    for k, v in player.items():
        print(f'{k}: {v}')
    print('-'*10)

found = False
while found != True:
    searchPlayer = str(input('Type the name of player: ')).upper()
    for p in register:
         if p['name']==searchPlayer:
             print(f'\nPlayer found!')
             for k, v in p.items():
                 print(f'{k}: {v}')
             found = True
             break

    if not found:
        print('Player not found!')


found = False
while not found:
    searchClub = str(input('Type the name of the club: ')).upper()
    for p in register:
        if p['club']==searchClub:
            print(f'\nClub found!')
            for k, v in p.items():
                print(f'{k}: {v}')
            found = True

    if not found:
        print('Club not found!')