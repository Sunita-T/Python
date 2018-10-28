'''21/9

map:
n=range(10)
print map(lambda x:x+x,n)


filter:
l=range(10)
print filter(lambda x:x%2==0,l)
op:[0, 2, 4, 6, 8]

reduce
l=range(10)
print reduce(lambda x,y:x+y,l)
op:45  it adds the numbers

l=xrange(10)
print(l)


l=range(10)
print(l)

s=raw_input('what is your name: ')
print s

f=lambda x:x*x
print f



pwd='apple
if pwd == 'apple':
    print('Logging on ...')
else:
    print('Incorrect password.')

x=-10
if x<0:
    print('x is nagative')
else:
    print('x is positive')

limited arguments example
def get(x,y):
    return(x+y)
print get(10,20)

default argumnet example
def get(x=10,y):
return x+y           it throw an error
print get(10)


def get(x,y=10):
    return x+y
print get(10)
                           op:20


def get(x,y=10,z=30):
    return x+y+z           op:60
print get(10,20,30)


def get(x=10,y,z=30):
    return x+y+z            op:throw an error
print get(10,20,30)


def get(x=10,y,z):
    return x+y+z            op:error
print get(10,20,30)


def get(*x):
    return x
print get(10)
print get(10,20)
print get(10,20,30)

                           tuple formate op:
                              (10,)
                              (10, 20)
                              (10, 20, 30)

def get(**args):
    return args
print get(a=10)
print get(a=10,b=20)
print get(a=10,b=40,c=30)

                          dictionary formate op:
                          {'a': 10}
                          {'a': 10, 'b': 20}
                          {'a': 10, 'c': 30, 'b': 40}

l=raw_input('what is your name:')
print l
                             op:it gives the output in string

lambda function examples
f=lambda x,y:x+y
print f(10,20)

l=lambda x:x+x
print l(10)'''

'''l=range(10)
print reduce(lambda x,y:x*y,l)'''

'''l=range(10)
def gen():
    for x in l:
        yield x*x
        obj=gen()
        print obj.next()'''

                             
