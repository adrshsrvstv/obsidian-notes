---
title: ML_Week_3
subtitle: 
author:
  - Adarsh Srivastava
date: 17 November, 2024
tags:
---


### Classification

- Two class classification: $y_j^{(i)} \in \{0,1\}$ - a negative class and positive class
- Multi class: $y_j^{(i)}  \in \{0,1, 2, 3, \ldots \}$ 
### Binary Classification
- We want out hypothesis to satisfy $0 \leq h_{\theta}(x) \leq 1$ 
- Sigmoid function (or logistic function): 
$$g(z)=\frac{1}{1+e^{-z}}$$
- Plot: ![Plot | 200](https://cdn.mathpix.com/solve/images/6380eca4f1aa8c95e6a70ad00f4f7137.png)   

- Hypothesis: $h_\theta(x)=g(\theta^Tx)$ 
	- Output is estimated probability that $y=1$ on input $x$ 
	- In other words $h_{\theta}(x)=P(y=1|x,\theta)$ 

### Decision Boundary:
- When do we predict $y=1$ and when do we predict $y=0$, since we only have probabilities till now.
- Simplest decision boundary would be $0.5$, predicting $y=1$ when $h_{\theta}(x) \geq 0.5$  and $y=0$ when below it.
	- This would imply predicting $y=1$ whenever $\theta^{T}x \geq 0$ and  $y=0$ whenever $\theta^{T}x \lt 0$ 
	- Given $\theta^{T}x$ is a linear function, the above statement is akin to saying "one side" of the "line/plane" is $y=1$ and the other "side" is $y=0$.
	- This "line/plane/higher dimension linear curve" becomes our decision boundary
- What about when data is such that a linear boundary can't work?
	- Need higher order polynomial features. e.g. $x_{1}, x_{2}, x_{1}^2,x_{2}^3, x_1x_2^2$   

### Cost function and Gradient Descent for Logistic Regression
- We can re-write our original [cost function for linear regression](ML_Week_2.md#^d7afb9) as: $$J(\theta)= \frac{1}{m} \sum_{i=1}^{m}\left( \operatorname{Cost(h_\theta(x^{(i)}),y^{(i)}}\right)$$
- For logistic regression, let's define: $$\operatorname{Cost}\left(h_{\theta}(x), y\right)=\left\{\begin{aligned}
-\log \left(h_{\theta}(x)\right) & \text { if } y=1 \\
-\log \left(1-h_{\theta}(x)\right) & \text { if } y=0
\end{aligned}\right.$$
- Writing this in a simplified form:  $$\operatorname{Cost}\left(h_{\theta}(x), y\right)= -ylog(h_{\theta}(x)) - (1-y)log(1-h_{\theta}(x))$$
- Incorporating this in the cost function $J(\theta)$ above: $$J(\theta)= -\frac{1}{m} \sum_{i=1}^{m}\left[ y^i \cdot log(h_{\theta}(x^i)) + (1-y^i) \cdot log(1-h_{\theta}(x^i))\right] \tag{1}$$
	- Why this cost function? This can be derived from Maximum likelihood estimation technique. Minimizing this gives us the best parameters for our model. #follow-up
	- This is also a convex function and so suitable for GD.
	- Vector form of above cost function $(1)$: $$\vec{J(\theta)}=-\frac{1}{m}\left[\vec{y}^T \times log(\vec{h}) + (1-\vec{y})^T \times log(1-\vec{h})\right]$$
- Applying [gradient decent](ML_Week_2.md#^250e52) to $(1)$, we get the same form as linear regression, of course, with $h_\theta(x)$ being defined differently. 
$$\text{repeat until convergence: }\bigg\{\theta_{j}:=\theta_{j}-\alpha \frac{1}{m} \sum_{i=1}^{m}\left[(h_{\theta}(x^i)-y^i) \cdot x^i_j\right] \bigg\} \tag{2}$$
- Vectorized form for $(2)$ above:  $$\theta:=\theta-\frac{\alpha}{m} \left[ X^{T} \times \left(g(X \theta)-y\right) \right]$$
### Multi - class logistic regression
- $y_j^i \in \{1 \ldots n\}$ 
- We solve this by solving $n$ 'one-vs-all' binary classification problems. We use the same logistic regression classifier as earlier, n times.
- $h^{(i)}_{\theta}(x)=P(y=i|x,\theta)$ , where $i=1,2,3, \ldots n$
- For a new input x, predict $y=i$ for $\max_{i}(h^{(i)}_{\theta}(x))$ 

### Overfitting

- !["high bias", "just right", "high variance" ](attachments/0cOOdKsMEeaCrQqTpeD5ng_2a806eb8d988461f716f4799915ab779_Screenshot-2016-11-15-00.23.30.png) 
- *"High bias"*: Underfitting. The model assumes too much and maps poorly to the trend of the data - such as fitting a linear model to a clearly polynomial trend.
- *"Just right"*: More or less follows the trend, and generalizes well to new data. This may mean not being the lowest cost hypothesis and having a lower accuracy on training set - the curve doesn't bend all over the place to fit data.
- *"High variance"*: Overfitting. The curve bends all over the place to fit the data very accurately, but does not generalize well to predict new data. This would have a very high accuracy on training set, but may give bizarre results on new data. Called high variance because the model has a high variance for even a small change in training set/on separate training sets from the same problem we're trying to model.
- What to do to overcome these issues?
	- Choose/Reduce features carefully, and remove redundant/irrelevant features
		- Can do manually
		- Or do feature selection/reduction using algorithms
	- Regularize the parameters and thus decrease the impact of features that have only a minuscule effect on the prediction; i.e., we keep all the features, but reduce the magnitude of parameters $\theta_j$.

### Regularization
- **Intuition**: Hypothesis overfits when higher order coefficients have non-trivial contributions - if we make them close to zero, our hypothesis behaves essentially like a lower order polynomial.
- Consider the Linear regression hypothesis $h_\theta(x)= \theta_{0}+ \theta_{1}x_1+ \theta_{2}x_{2}^2 + \theta_{3}x_{3}^3+ \theta_{4}x_{4}^4$ . We could write the cost function with added terms like so: $$J(\theta)= \frac{1}{2m} \sum_{i=1}^{m}\left(h_\theta(x^{(i)})-y^{(i)}\right)^2 + 1000 \cdot \theta_{3}^2 + 10000 \cdot \theta_{4}^2 \tag{3}$$
- Now, when we try to minimize $J(\theta)$, we are forced to assign a smaller value to $\theta_3$ and $\theta_4$, thereby effectively reducing the order of our hypothesis.
- Simpler hypothesis -> Less prone to overfitting ("Smoother" functions)
- If we have a large number of features, we may not be able to choose the parameters to regularize well. So we normalize all $\theta_n$ 
- Regularized cost function - note that $j$ starts from $1$, i.e., we are not regularizing $\theta_0$: $$J(\theta)=\frac{1}{2m}\left[\sum_{i=1}^{m}\left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right)^{2}+\lambda \sum_{j=1}^{n} \theta_{j}^{2}\right] \tag{4}$$
- $\lambda$ is called the regularization parameter:
	- too large -> underfitting
	- too small -> overfitting
	- In practice, chosen automatically by certain algorithms.
### Regularized Linear Regression
- The [gradient descent update rule](ML_Week_2.md#^f878ee) when modified for regularization becomes (the rule for $\theta_{0}$ remains the same, this is for $j=1,2,3 \ldots n$): $$\theta_{j}:=\theta_{j}\left(1-\alpha \frac{\lambda}{m}\right)-\alpha \frac{1}{m}\sum_{i=1}^{m}\left(h_{\theta}\left(x^{(i)}\right)-y^{(i)}\right) x_{j}^{(i)} \tag{5}$$
### Regularized Logistic Regression
- $$J(\theta)=\frac{1}{m} \sum_{i=1}^{m}\left[-y^{(i)} \cdot \log(h_{\theta}(x^{(i)}))-(1-y^{(i)}) \cdot \log(1-h_{\theta}(x^{(i)}))\right]+\frac{\lambda}{2 m} \sum_{j=1}^{n} \theta_{j}^{2}$$