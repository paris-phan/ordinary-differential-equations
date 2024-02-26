import numpy as np

t = 0
y = 2
h = 0.05
while(t <= 0.2):
    k1 = 5*t -3*np.sqrt(y)
    k2 = 5*(t + h/2) - 3*np.sqrt(y + (h/2)*k1)
    k3 = 5*(t + h/2) - 3*np.sqrt(y + (h/2)*k2)
    k4 = 5*(t + h) - 3*np.sqrt(y + h*k3)
    y = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
    print("k1 = ", k1, "k2 = ", k2, "k3 = ", k3, "k4 = ", k4, "y = ", y)
