s1= int(input('Enter a Number:'))
s2= int(input('Enter a Number:'))

print('1 = +')
print('2 = -')
print('3 = *')
print('4 = /')

a= int(input('Enter a Number for Operator :'))
match a:
    case 1:
        print('Addition is: ',s1+s2)
    case 2:
        print('Subraction is: ',s1-s2)
    case 3:
        print('Multiplication is: ',s1*s2)
    case 4:
        print('Division is: ',s1/s2)
    case _:
        print('Invaild Input')
        
