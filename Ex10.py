animals = {}
register = []

while True:

    animals['name']=str(input('Name: ')).upper()
    animals['specie'] = str(input('Specie: ')).upper()
    animals['age']=int(input('Age: '))
    animals['weight']=float(input('Weight: '))
    register.append(animals.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Wish to make another register?[Y/N]')).upper().strip()
    if opt == 'N':
        break

heavier = register[0]
for a in register:
    if a['weight']>heavier['weight']:
        heavier=a

oldest = register[0]
for a in register:
    if a['age']>oldest['age']:
        oldest=a

lightest = register[0]
for a in register:
    if a['weight']<lightest['weight']:
        lightest=a

youngest = register[0]
for a in register:
    if a['age']<youngest['weight']:
        youngest=a

print('-='*30)
print('LIST OF ANIMALS')
for i, animal in enumerate(register, start=1):
    print(f'Animal {i}')
    for k, v in animal.items():
        print(f'{k}: {v}')
    print('-'*10)

print(f'The heaviest animal is {heavier["name"]} with {heavier["weight"]} KG')
print(f'The lightest animal is {lightest["name"]} with {lightest["weight"]} KG')
print(f'The oldest animal is {oldest["name"]} that is {oldest["age"]} years old')
print(f'The youngest animal is {youngest["name"]} that is {youngest["age"]} years old')