from matplotlib import animation
import serial
import matplotlib.pyplot as plt
import numpy as np
import time
import pandas as pd

plt.ion()
fig = plt.figure()

i=0
x=list()
y=list()
z=list()
ser = serial.Serial('COM3',9600)
ser.close()
ser.open()
fig = plt.figure()
ax = fig.add_subplot()
fig.show()
while True:
    data = ser.readline()
    print(data.decode())
    x.append(i)
    y.append(data.decode())
    z= data.decode().split()
    x.append(z[3])
    z.clear()
    plt.cla()
    plt.plot(x[i],i)
    i+=1
    plt.show()
    plt.pause(0.01)
