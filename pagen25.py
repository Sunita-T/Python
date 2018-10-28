# -*- coding: cp1252 -*-
''''l=range(10)
def gen():
    for x in l:
        yield x*x
obj=gen()
print next(obj)
print next(obj)
print next(obj)
print next(obj)
print next(obj)
print obj.next()
print obj.next()
print obj.next()
print obj.next()
print obj.next()

imp
https://realpython.com/primer-on-python-decorators/'''

'''def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@dec
def say_whee():
    print("Whee!")'''




'''exception handling:
    try:
    with open('file1.txt','r') as f:
        s=f.read()
except:
            print 'this file not found'
else:
                print s
finally:
                    print 'done'''


'''def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
  yield n

    n += 1
    print('This is printed at last')
    yield n

# Using for loop
for item in my_gen():
    print(item) '''   

'''def fun(f):
    def fun1():
        print 'hello......'
        f()
        print 'hiiiii'
        return fun1
    def get():
        print 'hhhhh'
        get=fun(get)
        print get()'''


'''def hello1_say():
    print("hello")
    
    def hii_say():
        print("hiiii")
        
return hii_say
    
return hellol_say'''
        

'''def say_hello():
  print("Hello")
  
  def say_hi():
    print("Hi")
    
  say_hi()  
    
say_hello() '''


'''def getPrimes(n):
    prime=True
    i=2
    while(i<n):
        for a in range(2,i):
            if(i%a==0):
                prime=False
                break
        if(prime):    
            yield i'''


'''def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_whee():
    print("Whee!")
say_whee()'''







'''def deco(f):
    def deco1():
        print("this is dcorator1")
        f()
        print("decorator2")
        return deco1
@deco
def say_whee():
        print("hi this is decorator say")
say_whee()
'''

'''x=open('file22.txt','r')
s=x.read()
for each in s:
   print each
x.close'''

'''with open('file1.txt', 'r') as file: 
   data = file.readlines() 
for line in data: 
    word  = line.split() 
print word '''

'''with open('file1.txt','r') as f:
    x=f.readlines()
    for esch in x:
        s=esch.split()
        print s'''




'''fileleName = input("Enter the file to check: ").strip()'''

infile = open('file1.txt', 'r')


vowels = set("A E I O U a e i o u")
cons = set("b c d f g h j k l m n p q r s t v w x y z B C D F G H J K L M N P Q R S T V W X Y Z")

text = infile.read().split()


countV = 0
for V in text:
    if V in vowels:
        countV += 1

countC = 0
for C in text:
    if C in cons:
        countC += 1

print countV
print countC


