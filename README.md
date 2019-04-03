# SingleDampenedPendulumVisualization
Single dampened pendulum plot in python

undamped pendulum with no driving force:
>y'' + sin(y) = 0
we can reduce to first order ODE by:
let y1 = y and y2 = y1'
so
y1' = y2
y2' = -sin(y1)
to make it damped we modify with 
- mu * y2
where mu is dampening coefficient


![Phase Portrait](/phase-portrait.png)
