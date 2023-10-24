def calculator(a=None, action=None, b=None):
    if a is None or b is None or action is None:
        a = int(input('Enter first number: '))
        action = input('Choose + or - or * or / ')
        b = int(input('Enter second number: '))
    if action == '+':
        return print('result:',a+b)
    elif action == '-':
        return print('result:',a-b)
    elif action == '*':
        return print('result:',a*b)
    elif action == '/':
        if b != 0:
            return print('result:',a/b)
        else:
            return print('Warning! b = 0. Division is impossible')

calculator(3,'+',0)
print('\n')
calculator(3,'-',0)
print('\n')
calculator(3,'*',0)
print('\n')
calculator(3,'/',0)
print('\n')
calculator(3,'/',2)
print('\n')
calculator()
