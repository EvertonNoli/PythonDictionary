#cadastro de patinadoras
#mais velha e mais nova
#média de idade
#listar por país

skater = {}
register = []
countM = countF = 0

while True:

    skater['name']=str(input('Name: ')).upper()
    skater['age']=int(input('Age: '))
    skater['country']=str(input('Country: ')).upper()
    gender = ' '
    while gender not in 'MF':
        gender = str(input('Gender: ')).upper().strip()
    skater['gender'] = gender
    register.append(skater.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Do you wish to make another register?[Y/N]')).upper().strip()
    if opt == 'N':
        break

print('-='*30)
print('List of ice skaters')
for s, skater in enumerate(register, start=1):
    for k, v in skater.items():
        print(f'{k}: {v}')
    print('-'*10)

found = False
while not found:
    searchSkater = str(input('Type figure skater name: ')).upper()
    for s in register:
        if s['name']==searchSkater:
            for k,v in s.items():
                print(f'{k}: {v}')
            found = True
            break
    if not found:
        print('Figure skater not found!')

oldest = youngest = register[0]
avgAge = total  = 0
for s in register[1:]:
    if s['age']>oldest['age']:
        oldest=s
    if s['age']<youngest['age']:
        youngest=s
    total+=s['age']
avgAge = total/len(register)

for s in register:
    if s['gender']=='M':
        countM+=1
    if s['gender']=='F':
        countF+=1

print('-'*10)
print(f'The youngest figure skater is {youngest["name"]} that is {youngest["age"]} years old')
print(f'The oldest figure skater is {oldest["name"]} that is {oldest["age"]} years old')
print(f'There are {countM} men and {countF} women registered')
print(f'Average age: {avgAge:.2f}')

print('-='*30)
print('Figure Skaters Grouped by Country')
countries = {}

for skater in register:
    country = skater['country']
    countries.setdefault(country, []).append(skater['name'])

for country, names in countries.items():
    print(f'{country}: {"," .join(names)}')
