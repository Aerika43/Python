def show():
    print('APPLE')
    print('APPLE')
    print('APPLE')
    print('APPLE')
    print('APPLE')
show()        # 5 APPLE
show()        # 5 APPLE      ## Total 10 APPLE will be printed


def show(a='india'):
    print('My Country Name is ',a)
show()

def show(a='india'):
    print('My Country Name is ',a)
show('Nepal')
show()

def show(a, b):
    print(b,'MY country name is',a)
show(a='India',b='Nepal' )
