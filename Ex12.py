student = {}
register = []
approved = []
failed = []

while True:

    student['name']=str(input('Name: ')).upper().strip()
    student['grade1']=float(input('First grade: '))
    student['grade2']=float(input('Second grade: '))
    student['average']=(student['grade1']+student['grade2'])/2
    register.append(student.copy())

    opt = ' '
    while opt not in 'YN':
        opt = str(input('Do you wish to registrate another student?[Y/N]')).upper().strip()
    if opt == 'N':
        break

for s in register:
    if s["average"]>=7:
        approved.append(s.copy())
    else:
        failed.append(s.copy())


print('='*30)
print('Class Grades')
for i, s in enumerate(register, start=1):
    for k, v in s.items():
        print(f'{k}: {v}')
    print('-'*10)

print('='*30)
print('Approved Students')
for s in approved:
    print(f"{s['name']}: {s['average']}")
print('-'*10)
print('Failed Students')
for s in failed:
    print(f"{s['name']}: {s['average']}")