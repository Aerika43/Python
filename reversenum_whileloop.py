a = int(input('Enter a Number: '))
rev = 0
while (a != 0):
    digit = a % 10
    rev = rev * 10 + digit
    a //= 10
print('Reverse Number : ',rev)
    
