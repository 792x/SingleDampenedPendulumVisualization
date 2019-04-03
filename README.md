# SingleDampenedPendulumVisualization
Single dampened pendulum plot visualization in python

Undamped pendulum with no driving force is defined as:

`y'' + sin(y) = 0`

We can reduce to first order ODE by:

`let y1 = y and y2 = y1'`

So:

`y1' = y2`

`y2' = -sin(y1)`

To make it damped we modify with:

`- mu * y2`

where mu is dampening coefficient


![Phase Portrait](/phase-portrait.png)

From figure we can see that for starting points near origin and small velocites the pendulum
goes into a spiral straightaway, for others it keeps going right until also going into a spiral.
