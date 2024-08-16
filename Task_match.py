print('1 = Positive Negative Numbers.')
print('2 = Graph Quadrant')
print('3 = Calculator')
print('4 = Voting')
print('5 = Marksheet')
print('6 = Vowel and Consonant')
print('7 = Swap Numbers')
a=int(input('Enter a Number Between 1-7: '))
match a:
    case 1:
         num = int(input('Enter a Number : '))
         if(num>0):
             print('Postive Number')
         elif(num==0):
             print('Zero')
         else:
             print('Negative Number')
    case 2:
        c = int(input('Enter Number 1 : '))
        d = int(input('Enter Number 2 : '))
        if(c>0 and d>0):
            print('First Quadrant')
        elif(c<0 and d>0):
            print('Second Quadrant')
        elif(c<0 and d<0):
            print('Third Quadrant')
        elif(c==0 and d==0):
            print('Center')
        else:
            print('Fourth Quadrant')
    case 3:
        num1 = int(input('Enter a Number: '))
        num2 = int(input('Enter a Number: '))
        print('1 = Addtion (+)')
        print('2 = Subraction (-)')
        print('3 = Multiplication (*)')
        print('4 = Division (/)')
        o = int(input('Choose the Operation...'))
        match o:
                case 1:
                    print('Sum is: ',num1+num2)
                case 2:
                    print('Difference is: ',num1-num2)
                case 3:
                    print('Product is: ',num1*num2)
                case 4:
                    print('Quotient is: ',num1/num2)
    case 4:
        age = int(input('Enter your  Age: '))
        if(age>18):
            print('You Can Vote')
        elif(age==18):
            print('Better Luck Next Time')
        else:
            print('You Cannot Vote')
    
    case 5:
        print('Enter your Marks...')
        print()
        bio=int(input('Biology: '))
        mat=int(input('Maths: '))
        sci=int(input('Science: '))
        py=int(input('Physics: '))
        chem=int(input('Chemistry: '))
        print()
        t=bio+mat+sci+py+chem
        print('Obtained Marks: ',t)
        print('Total Marks: 500')
        percent=t/5
        print()
        print('Percentage: ',percent)
   
        if(percent>90 and percent<=100):
            print('GradeA+')
        elif(percent>80 and percent<=90):
            print('A')
        elif(percent>70 and percent<=80):
            print('B')
        elif(percent>60 and percent<=70):
            print('C')
        elif(percent>50 and percent<=60):
            print('D')
        else:
            print('Fail')

    case 6:
        str=input("Enter A Letter")
        if(str=='a' or str=='e' or str=='i' or str=='o' or str=='u' or str=='A' or str=='E' or str=='I' or str=='O' or str=='U'):
            print('Its Vowels')
        else:
            print('Its Consonant')
    case 7:
        n = int(input('Enter a Number: '))
        m = int(input('Enter a Number: '))
        swap = n
        n = m
        m = swap
        print('After Swapping...')
        print(n)
        print(m)




    
