from funct import fact
print('Start work')
while True:
    a = float(input())
    b = float(input())
    op = input()
    if op == '+':
        print(a + b)
    elif op == '-':
        print(a - b)
    elif op == '*':
        print(a * b)
    elif op == '/':
        print(a / b)
    elif op == 'mod':
        print(a % b)
    elif op == 'div':
        print(a // b)
    elif op == 'sqrt': #(from a)
        print(a ** 1 / b)
    elif op == '^':
        print(a ** b)
    elif op == '!':  # (use only a)
        print(fact(a))
    else:
        print('operator not found')
    if input('Enter "end" to finish work ').lower() == 'end':
        break
print('Finish work')
