print('MARKSHEET')
print('Enter your Marks...')
print()

a=int(input('Biology: '))
b=int(input('Maths: '))
c=int(input('Science: '))
d=int(input('Physics: '))
e=int(input('Chemistry: '))

total=a+b+c+d+e

print()
print('Obtained Marks: ',total)
print('Total Marks: 500')

percentage=total/5

print()
print('Percentage: ',percentage,'%')
print('Grade :')
if(percentage>90 and percentage<=100):
    print('A+')
elif(percentage>80 and percentage<=90):
    print('A')
elif(percentage>70 and percentage<=80):
    print('B')
elif(percentage>60 and percentage<=70):
    print('C')
elif(percentage>50 and percentage<=60):
    print('D')
else:
    print('Fail')
