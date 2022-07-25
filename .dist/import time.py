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
c=list()
ser = serial.Serial('COM3',9600)
ser.close()
ser.open()
while True:
    plt.show()
    data = ser.readline()
    print(data.decode())
    y.append(data.decode())

    x.append(z[3])
    print(x)
    z.clear()
    plt.plot(i,float(x[i]))
    plt.tight_layout()
    plt.show()
    time.sleep(0.01 )
    if i == 50:
        break
