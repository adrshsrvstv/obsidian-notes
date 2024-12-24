---
title: Machine Learning Notes
subtitle: Week 1
author:
  - Adarsh Srivastava
date: 19 November, 2021
tags:
---

## Supervised learning

Labelled dataset with "right answers" given as training data
1. Regression problem - predict continuous valued output
	- eg predicting house prices
2. Classification problem - discrete valued output (0 or 1)
	- eg Classifying if tumour is cancerous or not
	- or, type 1 cancer, type 2 cancer, type 3 cancer, no cancer (multi class classification)
3. Can have any number of features - eg age and tumour size to predict benign or cancerous
	- even infinite number of features possible (??)

## Unsupervised learning

Data is unlabelled - algorithm is asked to find structure in the data
1. Clustering algorithms
	- eg Google news story clusters
	- computing clusters, social network analysis, market segmentation, astronomical data analysis
3. Non Clustering algorithms - like singular value decomposition
	- eg solving Cocktail party problem - separating voices from two microphones. 
		- Solution using SVD: $[W, s, v]=\operatorname{svd}\left(\left(\operatorname{repmat}(\operatorname{sum}(x . * x, 1), \operatorname{size}(x, 1), 1) .^{*} x\right)^{*} x^{\prime}\right) ;$

## Linear Regression

Let's start with example of housing price prediction:
- Training set - $m$ number of data points, consisting of $x$ - area $y$ - price. $(x_i, y_i)$ is one training example.
- Training set -> fed to a learning algorithm -> which outputs a function $h$ or *hypothesis function*. This maps house area to house prices based on the data set.  
- One example of hypothesis function - a linear one: $h(x) = \theta_0 + \theta_1x$
- This is called Linear regression in One Variable. 

## Cost function

Figuring how to figure best possible line to our data we intent to apply linear regression to.
- In the equation , $h_\theta(x) = \theta_0 + \theta_1x$ for different values of $\theta_0$ and $\theta_1$ (our _parameters_) we'll have different lines - slope and y intercept of the line. ^e36df9
- Task is to predict $\theta_0$ and $\theta_1$ so that our predictions based on training set - $h(x)$ are as close as possible to the actual values $y$
- Minimise over $\theta_0$ and $\theta_1$ , $(h_\theta(x) - y)^2$ for all x and y in the training set of $m$ elements. 

$$
J(\theta_0, \theta_1)=\frac{1}{2 m} \sum_{i=1}^{m}\left(h_\theta\left(x^{(i)}\right)-y^{(i)}\right)^{2} \tag{1}
$$

^493bb8

- ^ This is called the mean squared error cost function (halved to simplify extra $2$ from differentiation in gradient descent). Works well for linear regression problems.
- The cost function $J(\theta_0, \theta_1)$ has the form of a paraboloid ( or a parabola if $\theta_0$ is set to a constant). Finding the minimum (convex function, so there's only one local, and also global, minimum) would entail finding the point where the slope ( or derivative wrt $(\theta_0, \theta_1)$) is 0.

## Gradient Descent

- This is a general algorithm used all over ML to minimising an arbitrary function $J$ over any number of params $\theta_0, \theta_1, \theta_2 ,\cdots$ 
- Algorithm goes like so. Imagine you are somewhere on the plot of $J$ (in whatever dimensions):
	1. Choose any starting point on the curve for some values of params $\theta_{0}, \theta_{1},\theta_{2}, \cdots$
	2. Take a little step in some direction that _decreases_ the value of $J$ _most steeply_. (A tiny step in the direction of steepest descent). This will correspond to moving in _each dimension_ in the direction of steepest descent on the curve wrt that dimension.
	3. Repeat (2) until you converge to a local minimum - or until another step in any other direction will be an ascent on J.
Mathematically,
$\text{repeat until convergence:}$
$$
\theta_{j}:=\theta_{j}-\alpha \frac{\partial}{\partial \theta_{j}} J\left(\theta_{0}, \theta_{1},\cdots \right) \quad(\text { for } j=0 \text { , } j=1 \text { and so on} \text { ) }  \tag{2}
$$
Here, 
- We say we converged when another iteration produces no change in params. That's when we are at a local minimum for cost function $J$. ^8eaaad
- $\alpha$ is learning rate. Size of the step we take.
	- if $\alpha$ is too small - you take a ton of iterations to converge. We should adjust our parameter $\alpha$ to ensure that the gradient descent algorithm converges in a reasonable time
	- if $\alpha$ is too large, you may miss the minimum and overshoot and never converge, or even diverge instead
- In each iteration, we simultaneously update all $\theta_i$ 
- $\frac{\partial}{\partial \theta_{j}} J\left(\theta_{0}, \theta_{1}, ...\right)$ will be the slope on the curve of J wrt $\theta_{j}$. By subtracting $\alpha$ times this slope, we ensure we move $\theta_j$ in the direction of decreasing $J$ - i.e. we'll add to $\theta_{j}$ if slope is negative, and subtract when slope is positive.
	- Slope decreases in magnitude as you begin to approach local minimum, so the _steps_ become smaller with each iteration.

## Gradient descent for Linear Regression Cost Function

For univariate linear regression, we have two params, and the gradient descent equations come out to be:
$\text{repeat until convergence:}$
$$
\theta_{0}:=\theta_{0}-\alpha \frac{1}{m} \sum_{i=1}^{m}\left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right)  \tag{3}
$$

$$
\theta_{1}:=\theta_{1}-\alpha \frac{1}{m} \sum_{i=1}^{m}\left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right) \cdot x^{(i)} \tag{4}
$$



- "Batch" gradient descent: Since we are summing over _all_ $m$ training examples in _each_ iteration.

## Linear algebra review

- [Matrices and linear transformations - Math Insight](https://mathinsight.org/matrices_linear_transformations) 
- Remember that Matrix multiplication is basically function composition of two linear functions represented as Matrices. [What is the intuition behind multiplication of matrices? - Quora](https://www.quora.com/What-is-the-intuition-behind-multiplication-of-matrices) 