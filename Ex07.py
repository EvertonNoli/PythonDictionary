#Cadastre varios jogadores com: nome, posicao, time. Depois, mostre os jogadores separados por
#time
jogador = {}
cadastro = []
grupo = {}

while True:

    jogador['nome']=str(input('Nome: ')).upper()
    jogador['posicao']=str(input('Posição: ')).upper()
    jogador['time']=str(input('Time: ')).upper()
    cadastro.append(jogador.copy())

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break


print('-='*30)
print('CADASTRO DE JOGADORES')
for j, jogador in enumerate(cadastro, start=1):
    for k, v in jogador.items():
        print(f'{k}: {v}')
    print('-'*10)

for jogador in cadastro:
    time = jogador['time']
    grupo.setdefault(time, []).append(jogador)

for time, jogador in grupo.items():
    print(f'\nTime: {time}')
    for j in jogador:
        print(f"{j['nome']} - {j['posicao']}")