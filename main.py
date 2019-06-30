import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

"""
damped pendulum visualization with phase plot in python
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
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

xUpperLimit = 25
xLowerLimit = -3.0
yUpperLimit = 5
yLowerLimit = -3.0
mu = 0.1

def f(Y, t):
    y1, y2 = Y
    return [y2, -np.sin(y1)] #for without dampening use [y2, -np.sin(y1)]

y1 = np.linspace(xLowerLimit, xUpperLimit, 20) #our x axis
y2 = np.linspace(yLowerLimit, yUpperLimit, 20) #our y axis


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
plt.xlim([xLowerLimit, xUpperLimit])
plt.ylim([yLowerLimit, yUpperLimit])
plt.savefig('phase-portrait.png')
plt.show()

"""
from figure we can see that for starting points near origin and small velocites the pendulum
goes into a spiral straightaway, for others it keeps going right until also going into a spiral.
"""
