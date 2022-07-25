from ctypes.wintypes import FLOAT
import matplotlib.pyplot as plt
import serial
ser = serial.Serial('COM3',9600)
fig = plt.figure(figsize=(7,3))
ax = fig.add_subplot()

fig.show()
x= []
i=0
l=200
ser.close()
ser.open()
z=[]

for i in range(l):
    ser1 = ser.readline().decode('ascii')
    z= ser1
    z= z.split()
    print(z)
    ser2 = float(z[11])
    z.clear()
    x.append(ser2)
    ax.plot(x,color='b')
    fig.canvas.draw()
    ax.set_xlim(left=max(0,i-30),right=i+60)
    plt.pause(0.0001)

plt.show