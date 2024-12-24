## Binary classification
- Notation:
	- $(x,y)$ is one training example where $\vec{x} \in \mathbb{R}^{n_x}$ and $y \in \{0,1\}$
	- $m$ training example pairs $\{(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), (x^{(3)}, y^{(3)}), \ldots\}$
	- $m_{test}$ and $m_{training}$   
	- $X=\left[\begin{array}{cccc} \mid & \mid & & \mid \\ x^{(1)} & x^{(2)} & \cdots & x^{(m)} \\ \mid & \mid & & \mid \end{array}\right]$
	- Compare above with [earlier defined X](../ML_Old-Coursera-AndrewNg/ML_Week_2.md#^e3c6bc). The way we have defined here is intentional and will make things easier for NNs.
	- $size(X) = (n_{x}\times m)$, or $X \in \mathbb{R}^{n_{x}\times m}$  
	- $Y=\left[\begin{array}{cccc} y^{1} & y^{2} & \cdots & y^{m} \end{array}\right]$ 
- 