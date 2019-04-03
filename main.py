import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""
damped pendulum visualization in python
-------------------
undamped pendulum with no driving force:
y'' + sin(y) = 0
we can reduce to first order ODE by:
let y1 = y and y2 = y1'
so
y1' = y2
y2' = -sin(y1)
to make it damped we modify with 
- mu * y2
where mu is dampening coefficient
"""

xlimit = 10
ylimit = 5
mu = 0.1

def f(Y, t):
    y1, y2 = 
    return [y2, -(g/L)*np.sin(y1) - mu * y2] #for without driving force use -np.sin(y1) - mu * y2

y1 = np.linspace(-3.0, xlimit, 20)
y2 = np.linspace(-3.0, ylimit, 20)

Y1, Y2 = np.meshgrid(y1, y2)

t = 0

u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

NI, NJ = Y1.shape

for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = f([x, y], t)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
     
Q = plt.quiver(Y1, Y2, u, v, color='r')

#angle between -pi and pi
angle = np.pi/3

#consider values y2(0) = [0, 0.5, 1, 1.5, 2, 2.5, 3.0] so some angular velocity
for y20 in [0, 0.5, 1, 1.5, 2, 2.5, 3.0]:
    tspan = np.linspace(0, 50, 200)
    y0 = [angle, y20]
    ys = odeint(f, y0, tspan)
    plt.plot(ys[:,0], ys[:,1], 'b-') # path
    plt.plot([ys[0,0]], [ys[0,1]], 'o') # start
    plt.plot([ys[-1,0]], [ys[-1,1]], 's') # end
    
plt.xlabel('$y_1 (angle)$')
plt.ylabel('$y_2 (velocity)$')
plt.xlim([-3.0, xlimit])
plt.ylim([-3.0, ylimit])
plt.savefig('phase-portrait.png')
plt.show()

"""
from figure we can see that for starting points near origin and small velocites the pendulum
goes into a spiral straightaway, for others it keeps going right until also going into a spiral.
"""
