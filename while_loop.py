i=1
while(i<=10):
    print(i)
    i=i+1
##OUTPUT :
##1
##2
##3
##4
##5
##6
##7
##8
##9
##10    

i=10
while(i>=1):
    print(i)
    i=i-1
##OUTPUT :
##10
##9
##8
##7
##6
##5
##4
##3
##2
##1


##i=1
##while(i<=10):
##   print(i)
## OUTPUT :
## infinite loop of 1

##i=1
##while(i<=10):
##    print(i)
##    i=i-1
## OUTPUT :
## infinte loop of all Negative Numbers....    


##i=10
##while(i>=1):
##    print(i)
##    i=i+1
## infinte loop of all Postive Numbers.... 

h=0
while True:
    a=int(input('Enter number: '))
    if(a==0):
        break
    h=h+a
print('Total: ',h)

