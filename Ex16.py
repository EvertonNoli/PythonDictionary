#cadastro de carros
#marca, preço, cor, ano

car = {}
register = []

while True:

    car['brand']=str(input('Brand: ')).upper()
    car['price']=float(input('Price: '))
    car['color']=str(input('Color: ')).upper()
    car['year']=str(input('Year: '))
    register.append(car.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Do you wish to make another register?[Y/N]')).upper().strip()
    if opt == 'N':
        break


print('-='*30)
print('List of Vehicles')
for c, car in enumerate(register, start=1):
    for k, v in car.items():
        print(f'{k}: {v}')
    print('-')

#count yellow fiat

countYF = 0
for c in register:
    if c['color']== 'YELLOW' and c['brand']== 'FIAT':
        countYF+=1

averagePrice = total = 0
expensive = cheap = register[0]
for c in register:
    if c['price']>expensive['price']:
        expensive=c
    if c['price']<cheap['price']:
        cheap=c
    total+=c['price']
averagePrice = total/len(register)



print(f'We count {countYF} yellow Fiats')
print(f'The most expensive vehicle is: {expensive["brand"]} costing: ${expensive["price"]}')
print(f'The cheapest vehicle is: {cheap["brand"]} costing: ${cheap["price"]}')
print(f'Amount total of sales: ${total:.2f}')
print(f'Average of sales: ${averagePrice:.2f}')