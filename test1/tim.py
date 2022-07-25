import time

myTime=time.localtime()

print(myTime)
print("Date")
print(myTime.tm_year,end="/")
print(myTime.tm_mon,end="/")
print(myTime.tm_mday,end="")


print("\nTime")
def formatTime(T):
    print(T.tm_hour,end=" : ")
    print(T.tm_min,end=" : ")
    print(T.tm_sec,end="")
    print("\n")

formatTime(myTime)
print(">..................................<")
'''
while True:
    tempsec=myTime.tm_sec
    #if(myTime.tm_sec):
    myTime=time.localtime()
    formatTime(myTime)
'''
t=time.clock()
print(t)
