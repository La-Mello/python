'''
blocks of code that can be re used
'''
# takes parameters returns a value
def add(x,y):
    return x+y

print(add(2,3))


# takes parameters no return value
def sayHi(name):
    print(f'Hello, {name}')

sayHi("Brian")

# no parameters returns a value
def getNum():
    return 1

print(getNum())

# recursive functions
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))
