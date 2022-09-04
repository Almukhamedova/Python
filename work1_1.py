x = int(input('Enter X:'))
y = int(input('Enter Y:'))
if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('IV')
elif x == 0:
    print('Тoчка лежит на оси Y')
elif y == 0:
    print('Тoчка лежит на оси X')