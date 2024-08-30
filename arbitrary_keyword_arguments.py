''''
Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments
that will be passed into your function,
add two asterisk: ** before the parameter name in
the function definition.

This way the function will receive a dictionary of
arguments, and can access the items accordingly:
'''

def one(**a):
    print('my name is ',a['c'])

one (a='aerika' , b='bunny' , c='sumeet' , d='rakesh')    
