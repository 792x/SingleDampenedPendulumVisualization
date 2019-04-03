# SingleDampenedPendulumVisualization
Single dampened pendulum visualization with phase plot in python

Undamped pendulum with no driving force is defined as:

`y'' + sin(y) = 0`

Damped pendulum with driving force is defined as:

`y'' + mu*y'+ (g/l)*sin(y) = 0`

We can reduce to first order ODE like so:

`let y1 = y and y2 = y1'`

So:

`y1' = y2`

`y2' = -(g/l)*sin(y1) - mu * y2`

Where g is gravitational accelleration, l is length of pendulum, mu is dampening coefficient.

![Phase Portrait](/phase-portrait.png)

From the output figure (example without driving force) we can see that for starting points near the origin and with small velocites the pendulum goes into a spiral straightaway, for others it keeps going right until also going into a spiral.
