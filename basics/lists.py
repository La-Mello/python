'''
store multiple elements of same or different datatypes
'''
l=["ben",1,2,3,4,3.14]
print(l)

# list comprehension
l2=[i+1 for i in range(10)]
print(l2)

# list methods

print(l2.count(1))# returns amount if 1's in the list

print(f'size is {len(l2)}')

# copies one list to another
l3=l2.copy()
print(l3)
l3.clear()

