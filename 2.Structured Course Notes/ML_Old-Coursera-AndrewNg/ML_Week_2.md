---
title: Machine Learning Notes
subtitle: Week 2
author:
  - Adarsh Srivastava
date: 17 November, 2021
tags:
---

## Multiple features in Linear Regression

- Consider house price prediction - can be done with multiple features
	- Area ($x_1$), no of bedrooms ($x_2$), no of floors ($x_3$), age in years ($x_4$), price ($y$)
	- Let:
		- $n$ = number of features
		- $x^{(i)}$ = input feature vector of $i^{th}$ training example
		- $x^{(i)}_j$ = value of $j^{th}$ feature for $i^{th}$ example

- New hypothesis function - again a linear function - a line in $n$ dimensions:

$$
h_\theta(x)= \theta_{0}+ \theta_{1}x_1+ \theta_{2}x_{2} + \cdots + \theta_{n}x_{n} \tag{1}
$$

- If we write: $x^{(i)}=\left[\begin{array}{c}x_{0}^{(i)} \\ x_{1}^{(i)} \\ x_{2}^{(i)} \\ \vdots \\ x_{n}^{(i)}\end{array}\right] \in \mathbb{R}^{n+1}$ (taking $x_0^{(i)}=1$ ) and $\theta=\left[\begin{array}{c}\theta_{0} \\ \theta_{1} \\ \theta_{2} \\ \vdots \\ \theta_{n}\end{array}\right] \in \mathbb{R}^{n+1}$ , then, we can write the above function as

$$
h_{\theta}(x)=\left [\begin{array}{llll}\theta_{0} & \theta_{1} & \cdots & \theta_{n}\end{array}\right] \left [\begin{array}{c}
x_{0} \\
x_{1} \\
\vdots \\
x_{n}
\end{array}\right]=\theta^{T}x \tag{2}
$$

- This is called multivariate linear regression.
- In $(2)$, remember that $x^{(i)}$ is a single column vector of $(n+1)\times1$. You may want to transpose and collate all such column vectors into one single matrix of size $m\times(n+1)$ of the form:

$$
X=\left[\begin{array}{c} \cdots (x^{(1)})^T \cdots \\ \cdots (x^{(2)})^T \cdots \\\cdots (x^{(3)})^T \cdots \\ \vdots \\ \cdots (x^{(m)})^T \cdots\end{array}\right] \tag{3}
$$
 ^e3c6bc

- In this case, the hypothesis function will take the form:

$$
 h_\theta(X)=X\theta
$$

## Gradient Descent for Linear Regression in Multiple Variables

- Parameters of the model: $\theta = \theta_{0}+ \theta_{1} + \theta_{2} + \ldots$ 
- Hypothesis: $h_\theta(x)= \theta_{0}+ \theta_{1}x_1+ \theta_{2}x_{2} + \cdots + \theta_{n}x_{n}=\theta^{T}x$ 

- Cost function (Compare with [eq 1](ML_Week_1.md#^493bb8) - only difference is vector form):

$$
J(\theta)= \frac{1}{2m} \sum_{i=1}^{m}\left(h_\theta(x^{(i)})-y^{(i)}\right)^2
$$

- Gradient Descent:

$$
\text{repeat until convergence: } \bigg\{
\theta_{j} := \theta_{j}-\alpha \frac{\partial}{\partial\theta_{j}}J(\theta) \text{   (simultaneous update for all j=0,1,2,}\ldots)
\bigg\}
$$
 ^250e52
- In the form of our [earlier equations for univariate case](ML_Week_1.md#^8c3c5c): 
	$\text{repeat until convergence, for all j=0,1,}\ldots$ 

$$
\theta_{j}:=\theta_{j}-\alpha \frac{1}{m} \sum_{i=1}^{m}\left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right) \cdot x^{(i)}_j
$$
^f878ee

## Normalization

### Feature scaling

- Idea: Make sure features are on a similar scale
- Why? GD might converge faster, cuz the steps are going to be small in each dimension, which may take a long time to converge for features with a large numerical scale.
- eg. Instead of area (2000 sq.ft.), use area/1000.
- In general, get every feature in the $-n \leq x \leq n$ range where $n$ is a relatively small number in the order of 1,2,3...

### Mean normalisation

- Replace $x_i$ with $x_i-\mu_i$ (where $\mu_i$ is the mean value of $x_{i}$) to have the distribution centered at 0
- eg convert $area/1000$ to ${(area-1000)}/{1000}$ if the avg house price is 1000.
We can use together:

$$
 x_{i} \to \frac{x_{i}-\mu_{i}}{s_{i}}
$$

where $\mu_i$ is mean of $x_i$ and $s_{i}$ is standard deviation, or the range if it is available.

## Learning rate

- How do we choose $\alpha$?
- Before that, what is our threshold for saying that GD has "converged"? We earlier said [that GD converges another iteration produces no change in params](ML_Week_1.md#^8eaaad), but in practice that would take an enormous number of iterations, each producing a progressively minuscule change in $J(\theta)$, making more iterations after a point pointless.
- In those cases, we can choose some $\epsilon$ threshold such that if $|\Delta J(\theta)|$ between iterations goes below it, we terminate the algorithm and declare convergence.
- If $\alpha$ is too big, we may see $\Delta J(\theta)$ become positive between iterations. Red flag. GD may not converge if this happens. Reduce $\alpha$ by an order of magnitude to fix this.

## Polynomial Regression

- Sometimes we want to create composite features:
	- eg, given frontage and depth of a house land, you may want to multiply them to create a new feature which would be area of the house.
	- This may give a better model.
- Or sometimes, a linear model simply won't be a good fit to the data. We might need a quadratic, cubic or square root curve to be a better model for the data.

## Normal Equation

> [!Side Note]
>
>Let $X$ be a full rank $m \times n$ matrix. By full rank we mean $\operatorname{rank}(X)=\min \{m, n\}$.
> - If $m<n$, then $X$ has a right inverse given by
> 

$$
X_{\mathrm{right}}^{-1}=X^{\top}\left(X X^{\top}\right)^{-1}
> 
$$

> - If $m>n$, then $X$ has a left inverse given by
> 

$$
X_{\mathrm{left}}^{-1}=\left(X^{\top} X\right)^{-1} X^{\top}
> 
$$

Of course, a right inverse is useful for solving an equation of the form $\theta X=Y$ and a left inverse is useful for solving an equation of the form $X\theta=Y$.
- If we write $X$ in the form shown in [(3)](ML_Week_2.md#^e3c6bc) , we have 

$$
h_\theta(X)=X\theta
$$

- Method to solve for optimal value of $\theta$ analytically instead of iteratively doing gradient descent. Minimising cost function by setting derivative to 0, we have:

$$
\frac{d}{d(\theta)}J(\theta)=0
$$

$$
\Rightarrow h_\theta(X)-y=0
$$

$$
\Rightarrow X\theta=y
$$

$$
\Rightarrow \theta=\left(X^{T} X\right)^{-1} X^{T} y
$$

- Need to calculate inverse of $X^{T}X$, which is $O(n^3)$. Slow if n is very large. (GD scales at $O(n)$ for n features)
- Can't calculate if $X^{T}X$ is singular or non-invertible
	- Can happen if some of your features are linearly dependent. eg $x_3=x_2+2x_1$ 
	- Or if you have $m \leq n$, no left inverse would exist. There are too few examples to solve for all params. (Not enough number of equations as the number of variables you are trying to solve for.)

## Vectorization

- For implementing these algorithms, vectorization provides a convenient way and avoids writing loops which is tedious and can introduce bugs. 
- Notation and a useful result:
	- $X$ is the collated feature vector of size $m\times(n+1)$ as written [here](ML_Week_2.md#^e3c6bc).
	- $y=\left [\begin{array}{} y_{1} \\ y_{2} \\ \vdots \\ y_{m} \end{array}\right]$ is the training set result values of size $m\times1$ 
	- $\theta=\left[\begin{array}{c}\theta_{0} \\ \theta_{1} \\ \theta_{2} \\ \vdots \\ \theta_{n}\end{array}\right]$ is our param vector of size $(n+1)\times1$  
	- $m$ is the number of training examples.
	- $h_\theta(X)=X\theta$ of size $m\times1$ 
	- If $A$ is a column matrix of dimension $n \times 1$, $A^{T}A = \sum_{i=1}^{n}a_i^2$     
- Vectorized form of cost function $J(\theta)$ ([v/s normal summed form](#^d7afb9))

$$
J(\theta) = \frac{1}{2m} \left[ (X\theta-y)^T(X\theta-y) \right]
$$

- Vectorized Gradient descent update steps (compare with our [earlier equation](ML_Week_2.md#^f878ee) )

$$
\theta := \theta - \frac{\alpha}{m}\left[X^T(X\theta-y)\right]
$$