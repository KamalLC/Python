# *args - allows you to pass an arbitrary number of arguments to a function. args is a tuple.
def sum(*args):
    sum=0
    for num in args:
        sum+=num
    print(type(args))
    print(f'sum={sum}')

sum(3,5,6,7)