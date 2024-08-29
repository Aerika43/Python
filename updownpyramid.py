for i in range(1, 6):   
    for j in range(5 - i):     
         print("   ", end=" ")
    for k in range(1, 2*i):    
         print(" * ", end=" ")
    print()
    
for i in range(7,1,-1):      
    for j in range(0, 7-i):     
         print("   ", end="")                      
    for k in range(i,2*i-1): 
         print(" * ", end="")
    for l in range(1, i-1):
        print(" * ",end="")
    print()
