#Cadastre varias pessoas com: nome e idade. Agrupe todas em 3 faixas:
#Menores de 18
#De 18 a 59
#Maiores de 60
#E mostre quantas pessoas ha em cada faixa

person = {}
register = []
u18 = []
u59 = []
greater60 = []

while True:

    person['name']=str(input('Name: ')).upper()
    person['age']=int(input('Age: '))
    register.append(person.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Do you wish to register another person?[Y/N]')).upper().strip()
    if opt == 'N':
        break

for p in register:
    if p["age"]<18:
        u18.append(p.copy())
    elif p["age"]>=18 and p["age"]<60:
        u59.append(p.copy())
    else:
        greater60.append(p.copy())


print('-='*30)
print('List of People')
for i, p in enumerate(register, start=1):
    for k, v in p.items():
        print(f'{k}: {v}')
    print('-'*10)

print('-='*30)
print('Underage')
for p in u18:
    print(f'{p["name"]}: {p["age"]}')
print(f'There were registered {len(u18)} underage people')
print('-'*20)

print('Adults')
for p in u59:
    print(f'{p["name"]}: {p["age"]}')
print(f'There were registered {len(u59)} adults')
print('-'*20)

print('Elderly')
for p in greater60:
    print(f'{p["name"]}: {p["age"]}')
print(f'There were registered {len(greater60)} old people')
print('-'*20)