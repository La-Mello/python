inputFile=open("C:\\Users\\Administrator\\Documents\\Python\\test1\\files\\input2","r")
outputFile=open("C:\\Users\\Administrator\\Documents\\Python\\test1\\files\\output2","w")
import time
print(inputFile,outputFile)
input("Press any key to continue")
startTime=time.asctime(time.localtime(time.time()))
print(f'started at {startTime}')

if inputFile and outputFile:
    while True:
        txt=inputFile.readline()

        if txt == "EOF":
            break

        outputFile.write(txt)
endTime=time.asctime(time.localtime(time.time()))
print(f'Finished at {endTime}')