# # class dog:
# #
# #     def __init__(self):
# #         return
# #
# #     def dog(self):
# #         return
# #
# #
# # if __name__ == '__main__':
# #     myDog=dog()
# #     print(myDog)
#
# str = "very long long string"
#
# for i in range(len(str)):
#     pass
#     # print(str[i])
#
# print(str[0:4])
#
#
# def revstr(inStr):
#     newstr = ""
#     le = len(inStr)
#     i = le - 1
#     while i >= 0:
#         newstr += inStr[i]
#         i -= 1
#     return newstr
#
#
# print(revstr(str))
# print(str[len(str) - 1:0])
#
# mylist = [2, 3, 4, 5, 6, 0]
# print(mylist)
# mylist.sort()
# print(mylist)
# mylist.clear()
# try:
#     newlist = [i for i in range(10)]
# except:
#     print("An error occured")
#     exit(1)
# else:
#     print(f'New list : {newlist}')
#
# mytuple=(1,2,3,6)
# print(mytuple)
# for m in mytuple:
#     print(m)

myDict = {
    "1": {
        "name": "brian",
        "age": 20
    },

    "2": {
        "name": "ben",
        "age": 15
    }
}

for id in myDict:
    for obj in id:
        # print(f'_id:{id}\n\t')
        pass

x = 20
y = 2
# exponent operator or to the power of
'''
print(x**y)

print(x/3)
print(x//3)

x=-20
#performs math floor on the result
print(x//3)

myl=[2,3,4,5,6]

# x=eval(input())


if x not in myl:
    print("not found")
else:
    print("found")
'''

name="nr"
# format specifiers
print("%s"%name)
name='b'
print("%c"%name)

def printL(l):
    for el in l:
        print(el,end=" ")
    print("\n")

myl = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
printL(myl)
print(len(myl))
del myl[0]
printL(myl)
print(len(myl))

myl.remove(0)
printL(myl)
print(len(myl))

data={
    "name":"brian",
    "age":20
}

data2={
    "name":"brian",
    "age":20
}

print(str(data))

for dt in data:
    pass
    #print(type(data[dt]))
datac=data.copy()
data.clear()

print(data)
print(datac)
print(datac.keys())
#print(type(x))

