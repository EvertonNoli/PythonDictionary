employee = {}
register = []

while True:

    employee["name"]=str(input('Name: ')).upper()
    employee["age"]=int(input('Age: '))
    employee["salary"]=float(input('Salary: $'))
    register.append(employee.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Do you wish to register another employee?[Y/N]')).upper().strip()
    if opt == 'N':
        break

bigger_salary = register[0]
for e in register:
    if e['salary']>bigger_salary['salary']:
        bigger_salary=e

lower_salary = register[0]
for e in register:
    if e['salary']<lower_salary['salary']:
        lower_salary=e

oldest = register[0]
for e in register:
    if e['age']>oldest['age']:
        oldest=e

youngest = register[0]
for e in register:
    if e['age']<youngest['age']:
        youngest=e

total_salary = 0
for e in register:
    total_salary +=e['salary']

average_salary = total_salary/len(register)


print('-='*30)
print('List of Employees')
for e, employee in enumerate(register, start=1):
    for k, v in employee.items():
        print(f'{k}: {v}')
    print('-'*10)
print('END!')

print(f'The employee with the highest salary is {bigger_salary["name"]} earning {bigger_salary["salary"]}')
print(f'The employee with the lowest salary is {lower_salary["name"]} earning {lower_salary["salary"]}')
print(f'The youngest employee is {youngest["name"]} that is {youngest["age"]} years old')
print(f'The oldest employee is {oldest["name"]} that is {oldest["age"]} years old')
print(f'The average salary of the company is {average_salary:.2f} and the total payment is {total_salary:.2f}')