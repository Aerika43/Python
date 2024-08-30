''''
Arbitray Arguments , *args

If you do not know how many arguments that
will be passed into your function ,
add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments,
and can access the items accordingly:
'''
def one(*a):
    print('my name is ',a[1])

one ('aerika','sumeet','rakesh')
##        0         1         2

