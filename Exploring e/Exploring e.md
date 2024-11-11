# Exploring [[Euler's Number]] $\large{e}$

## Project Proposal
%%[[2024-09-19]] @ 16:54%%

I'm currently watching [What's so special about Euler's number e? | Chapter 5, Essence of calculus](https://www.youtube.com/watch?v=mnMIpDrF7Es) by 3Blue1Brown. I want to play around with some numbers to get a feel for it.

## Relating Exponential functions with their derivatives
%%[[2024-09-19]] @ 16:59%%

Taking the set of functions that take the form $M(t) = n^{t}$, derivatives can be written as:
$$\frac{dM}{dt}(t) =\lim_{d \to 0} \ \frac{n^{t+dt} - n^{t}}{dt} $$
and as $n^{t+dt} = n^{t} \cdot n^{dt}$ this can be rewritten as:

$$\frac{dM}{dt}(t) =\lim_{d \to 0} \ n^{t} \left(\frac{n^{dt} - 1}{dt} \right)$$

This begs the question what is: $$k(n) = \frac{M(n,t)dt}{M(n,t)} = \lim_{d \to 0} \ \frac{n^{dt} - 1}{dt}$$
In other words what is the constant relating functions in the set to their derivative?

```functionplot
---
title: k(n)
xLabel: n
yLabel: k
bounds: [0,10,-4,4]
disableZoom: false
grid: true
---
f(x) = log (x)
```

And for what value $n$ is $k(n) = 1$ or what base makes an exponential function equal to its derivative?

This value is of course $e$ [[Euler's Number]] $\approx 2.71828...$ 