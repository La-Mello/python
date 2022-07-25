# you have an n size tuple and would like to unpack it to individual items
t = (2, 3, 4, 5)
a, b, c, d = t
print(a,end=" "); print(b,end=" "); print(c,end=" "); print(d,end=" ");

l=[1,2,3]
e,f,g=l
print("\n")
print(e,end=" "); print(f,end=" "); print(g,end=" ");

dt={
    "name":"brian",
    "age":20
}

name,age=dt.values()
print("\n")

print(name,end=" "); print(age,end=" ")

# using the star operator to unpack
details=("brian",20,70,77,89,50,"p101")

print("\n")
name,age,*grades,code=details
print(name,end=" "); print(age,end=" "); print(code,end=" ");
print(f'\n{grades}')


def grt(x,y):
    return x>y if x else y

print(grt(-12,3))
