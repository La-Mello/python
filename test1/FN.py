def add(x, y):
    '''Function to add two integer values'''
    try:
        sum = x + y
    except:
        return "Invalid"
    else:
        return sum


def min(x, y):
    try:
        if x > y:
            return x - y
        else:
            return y - x
    except:
        return "Invalid arguments"

print(add(2, "br"))
print(min("hello", 2))
print(add(20,-20))
print(min(10,-100))

x = 10;


def inc(x):
    x += 1


print(x)
inc(x)
print(x)
