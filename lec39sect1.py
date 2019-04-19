#Task 1, arduino serial
import serial
import matplotlib.pyplot as plt

ser = serial.Serial('COM3', 9600)
n = 0
dataLst = []
while n<200:
    print(ser.readline())
    dataPoint = ser.readline()
    dataPoint = int(dataPoint)
    dataLst.append(dataPoint)
    n+=1

ser.close()
plt.plot(dataLst)
plt.show()
f=open("serialData.dat", "w")
f.write(str(dataLst))
f.close()
f=open('serialData.dat', 'r')
print(f.read())
