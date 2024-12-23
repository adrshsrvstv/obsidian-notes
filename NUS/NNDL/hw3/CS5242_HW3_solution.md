---
title: CS5242_HW3_solution
subtitle: 
author:
  - Adarsh Srivastava (A0254358X)
date: 12 September, 2022
tags:
---
**Question 1:**
1. In the plot of loss vs. epoch number (as shown on the left), why does the loss increase for a very high learning rate (yellow curve)?
 ![graph | center | 200 ](attachments/Screen%20Shot%202022-09-10%20at%206.11.59%20PM.png)

**A.** For a very high learning rate, the "steps" taken during each gradient descent step are too large - the gradient gets multiplied by a very large number, the update to params is large, and the jump in the direction opposite the slope is too large. For a convex function, that would typically mean going over the convergence point to the other "arm" of the function.
	
Further, if the learning rate (and therefore the jump) is large enough, the slope at the new point is going to be higher than the earlier slope. That would mean a still greater "step" in the opposite direction - thus, with each step, we land further and further away from the optima, alternating on opposite sides of the optimal point. Therefore, the loss also keeps increasing with each step - (aka explodes), since with each step we are further away from the point of minimum loss.

1. Why the schedule of learning rate as in the figure below for some training and what are the advantages of such a schedule.
![ lr graph | center | 250](attachments/Screen%20Shot%202022-09-10%20at%206.32.54%20PM.png)
	**A.** A large learning rate means larger steps, and therefore faster "descent" on the slope. A smaller learning rate has the advantage of being able to better optimize the loss function by taking smaller steps around the optima.
	Therefore, to have the advantage of both, we start with a large learning rate, and step decrease it along the way as the loss starts plateauing. This has the advantage of faster descent during initial steps due to a large LR, and as we get closer to the optima, successively smaller steps, which makes sure we reach a lower loss and stop closer to the true optimum.

**Question 2:** 
You are presented with the following four activation functions:
1. $f(x)=\max (x, 0)+\min (x, 0) * 0.1$
2. $f(x)=\ln \left(e^{3 x}+1\right)$
3. $f(x)=\ln \left(e^{3x+1}\right)$
Which one is not suitable as an activation function? Which one is prone to gradient vanishing?

**A**
1. $f(x)=\max (x, 0)+\min (x, 0) * 0.1$
	Rewriting: 
	$f(x)=\left\{\begin{aligned} x & \text { if } x \geq 0 \\ 0.1x & \text { if } x<0 \end{aligned}\right.$
	This is a parametric ReLU with $\alpha = 0.1$. The derivative of this is given by:
	$f'(x)=\left\{\begin{aligned} 1 & \text { if } x > 0 \\ 0.1 & \text { if } x<0 \end{aligned}\right.$
	Thus, the function is non-linear, continuous everywhere, but non-differentiable at $x=0$, which would make it not suitable as an activation function for NNs on its own. However, if we additionally assign $f'(0) = 0.1$, the function has a valid gradient at all values of $x$ and can be used as an activation function. Further, this does not suffer from vanishing gradients problem as the derivative is always either $1$ or $0.1$.
2. $f(x)=\ln \left(e^{3 x}+1\right)$
	This function is non-linear, continuous, and differentiable everywhere. The derivative is given by

$$
f'(x)= \frac{3}{(1+e^{-3x})}
$$

 which takes values from $(0,3) \space \forall \space x \in \mathbb{R}$ , and is close to 0 only for larger negative values of $x$, and thus also does not suffer from vanishing gradients. Therefore, this function is suitable as an activation function. 
3. $f(x)=\ln \left(e^{3 x + 1}\right)$ 
	This function can be simplified to $f(x)= 3x+1$ which is a linear function and hence not suitable as an activation function for NNs. This has a constant gradient of $3$.

**Question 3:**
You are presented with the computational graph on the below. Suppose that $a = -1$ and $b = 4$.
1) calculate the gradient $dc/da$ 
2) What is the gradient component of $dc/da$ at location $(1)$ and $(2)$?
![|center | 200](attachments/Screen%20Shot%202022-09-10%20at%209.13.59%20PM.png)
**A**
1. Writing individual functions,
	Let $v(a) = a^2$, $u(a,b)=a+b$ , then

$$
c(a,b) = v \times u
$$

$$
\Rightarrow \frac{dc}{da}= \frac{dc}{dv} \times \frac{dv}{da} + \frac{dc}{du} \times \frac{du}{da}
$$

$$
\Rightarrow \frac{dc}{da}= u \times \frac{dv}{da} + v\times \frac{du}{da}
$$

$$
\Rightarrow \frac{dc}{da}= (a+b) \cdot 2a + a^2 \cdot 1 = 3a^2 +2ab
$$

So, at $a=-1$ and $b=4$, 

$$
 \frac{dc}{da} = 3(-1)^2 + 2(-1)(4)= -5
$$

2. At $(1)$, the gradient component is 

$$
 \frac{dc}{dv}\times \frac{dv}{da} = u \times \frac{dv}{da}= (a+b) \cdot 2a = (-1+4)2(-1)=-6
$$

At $(2)$, the gradient component is  

$$
 \frac{dc}{du}\times \frac{du}{da} = v \times \frac{du}{da}= a^2 \cdot 1 = (-1)^2(1)=1
$$

**Question 4:**
You have a binary classification problem with input $x \in \mathbb{R}^{100 \times 1}$. You consider designing a multi-layer perceptron (MLP) with two hidden layers and one output layer. Each hidden layer perceptron unit has no bias and uses a ReLU activation function. The output layer perceptron uses logistic regression, again with no bias.
1) MLP A has 100 units in the first hidden layer, 20 units in the second hidden layer.
2) MLP B has 20 units in the first hidden layer, 100 units in the second hidden layer.
How many parameters does each MLP have?
**A.** 
Given $x \in \mathbb{R}^{100 \times 1}$, the input layer has $100$ neurons for $100$ features, and given that this is a binary classification problem, the output layer has $2$ neurons, each outputting the probability of $y$ belonging to class $0$ or $1$. Further, with no bias terms, we only have the weights as the parameters of the network. If $w_i$ is the weights matrix between layer $L_i$ and $L_{i+1}$ (with input layer being $L_0$), the dimensions of each and the total number of parameters are:

| MLP (input layer $100$, output layer $2$)  | $dim(w_0)$  | $dim(w_1)$ | $dim(w_2)$ |  $\text{Total number of params}$  |
| ------------------------------------- | -------- | ------ | ------ |--------|
| With 100 units, 20 units hidden layers| $100 \times 100$  | $100 \times 20$ | $20 \times 2$  | $12,040$ |
| With 20 units, 100 units hidden layers| $100 \times 20$   | $20 \times 100$ | $100 \times 2$ |$4,200$ |

**Question 5**

The diagram below shows a plot of a function $f$ and gradient descend is applied to minimize the function at the point $O$. there is a bump a distance $L$ away with bump dimensions given as $h \times 2 h$. Let $L=1, a=0.3$ and $h>a$ where $a$ is the learning rate. 

![fn|center|350](attachments/Screen%20Shot%202022-09-11%20at%2012.26.05%20AM.png)
1. What is the lowest value f could reach in 1000 steps of standard gradient descend? Please show your explanation.
2. If you apply Adam optimizer with parameters given in the following figure, what is the max height h of the bump in which the Adam optimizer will escape the local min at x? use ε = 0 instead of ε = 1e − 8 in your calculations. (You can also write code to calculate the answer. If so please attach your code when submit.)

**A.**
1. As mentioned on clarifications on slack, assuming the bump is an isosceles triangle. In that case, the function can be written as:

$$
f(x)=\left\{\begin{array}{cl} -x+1, \quad x \leq 1 \\ x-1, \quad 1<x \leq 1+h \\ -x+(1+2h), \quad 1+h < x \leq 1+2h \\ \text{some unknown linear function} , \quad x>1+2h \end{array}\right. 
$$

We are starting at $O$ with $x=0$. The parameter here is $x$ and the gradient is $f'$. Here, the gradients are $-1$, $1$, and $-1$ for the first three sections of the function respectively. Running through the first few steps of GD, with $x_{i}$ being the value of $x$ after $i$th iteration, and $x_0 = 0$:

$$
x_{i+1} := x_i - a(f'(x)|_{x_i})
$$

$$
\Rightarrow x_1 := 0 - (0.3)*(-1) = 0.3
$$

$$
\Rightarrow x_2 := 0.3 - (0.3)*(-1) = 0.6
$$

$$
\Rightarrow x_3 := 0.6 - (0.3)*(-1) = 0.9
$$

$$
\Rightarrow x_4 := 0.9 - (0.3)*(-1) = 1.2
$$

At this point, $x>1$, so using the appropriate definition while calculating gradient:

$$
\Rightarrow x_5 := 1.2 - (0.3)*(1) = 0.9
$$

Thus, we are back to $x=0.9$. Further iterations with the same learning rate will simply oscillate between $x_3 = 0.9$ and $x_4 = 1.2$.
So,

$$
f(0.9) = 0.1
$$

 and, given that $h>0.3$,

$$
f(1.2)= 0.2
$$

Therefore, for the given learning rate of $0.3$, the minimum value achieved in $\geq 3$ iterations is $0.1$.
2. The code for the computation is:

```python
import math

x = 0
L = 1

beta1 = 0.9
beta2 = 0.999
e=0
m=0
v=0
t=0
alpha=0.001

def get_grad(x):
    if x <= L:
        return -1
    if x>L:
        return 1
    
def do_gd_step(t, alpha, x, beta1, beta2, m, v, L):
    t=0
    ex=list()
    while t< 1000000:
        t+=1
        grad = get_grad(x)
        m = beta1*m + (1-beta1)*grad
        v = beta2*v + (1-beta2)*(grad*grad)
        m_cap = m / (1 - pow(beta1, t))
        v_cap = v / (1 - pow(beta2, t))
        x = x - alpha * (m_cap/math.sqrt(v_cap))
        ex.append(x)
    print(max(ex))
    return ex

do_gd_step(t, alpha, x, beta1, beta2, m, v, L)
```

The above code block outputs `1.0024340620000007` as the max value that $x$ reaches for `alpha=0.001` before converging. Thus, if $h< 0.0024340620000007$, GD with Adam optimizer will escape the local optimum.

Note that the value is $h< 0.410184295129966$ for `alpha=0.3` 