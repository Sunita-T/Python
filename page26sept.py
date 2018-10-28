'''decorator example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_whee():
    print("Whee!")
say_whee()



try catch block example didvisible error:
    try:
   a=4
   b=2
   c=a/b
except:
        print 'divisible error'
else: 
            print c
finally:
                print 'done'




def hello_say(f):
    def hi_say():
        print("hi this is hi")
        f()
        print("hi this is f function")
        return hi_say
@hello_say
def fun_say():
        print("wow")
fun_say()



with open('file1.txt','r') as f:
    s=f.read()
    print s'''


'''words = 'the fox jumped over the lazy dog and over the bear'.split()
seen = set()
dups = set()
for word in words:
        if word in seen:
            if word not in dups:
                print(word)
                dups.add(word)
        else:
            seen.add(word)'''





print'even numbers'
print range(22,100,2)
