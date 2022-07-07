'''
used to repeat instructions a specified number of times
'''

# for...loop
# prints 1-5
from turtle import end_fill


for i in range(5):
    print(f'{i+1}',end=" ")

print("\n")

# can be used to iterate over lists/objects
l=[10,20,30,40,50]
for i in l:
    print(f'{i}',end=" ")

print("\n")
# works same as the first one but uses indexes
for i in range(len(l)):
    print(f'Index:{i} element{l[i]}')

# nested for loops prints a multiplication table
for i in range(5):
    for j in range(5):
        if i==0 or j==0:
            continue
        else:
            print(f'{i*j}',end=" ")
    print("\n")

# while loops
x=0
print(f'x is {x}')

while x<10:
    x+=1

print(f'x is {x}')

