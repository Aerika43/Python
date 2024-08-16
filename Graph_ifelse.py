a = int(input('Enter a  Number: '))
b = int(input('Enter a  Number: '))

if(a>0 and b>0):
    print('First Quadrant')
elif(a<0 and b>0):
    print('Second Quadrant')
elif(a<0 and b<0):
    print('Third Quadrant')
else:
    print('Fourth Quadrant')
    
