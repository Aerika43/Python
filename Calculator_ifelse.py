a = int(input('Enter a  Number: '))
b = int(input('Enter a  Number: '))

c= int(input("Enter a Operator 1.Addition 2.Subraction 3.Multiplication 4.Division : "))

if(c == 1):
    print("Addition is : ",a+b)
elif(c == 2):
    print("Subraction is : ",a-b)
elif(c == 3):
    print("Multiplication is : ",a*b)
elif(c == 4):
    print("Division is : ",a/b)
else:
    print('Invalid Input')
