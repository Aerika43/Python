a = int(input('Enter age: '))

#  >      Greater than
#  >=     Greater than Equal to
#  <       Less than
#  <=     Less than Equal to    
#  =       Equal to
#  !=      Not Equal to


##if(a>18):
##    print("You Are Eligible")
##else:
##    print("You Are Not Eligible")


if(a>18):
    print("You Are Eligible")
elif(a==18):
    print("Next Year")
else:
    print("You Are Not Eligible")

b = int(input('Enter age: '))

print('For  AND condition')
if(b>10 and b<20):
    print("School")
else:
    print("College")

print('For  OR condition')
if(b>10 or b<20):
    print("School")
else:
    print("College")    
