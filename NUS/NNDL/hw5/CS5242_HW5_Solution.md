---
title: CS5242_HW5_Solution
subtitle: 
author:
  - Adarsh Srivastava (A0254358X)
date: 3 October, 2022
tags:
---

**Question 1:**
1. Rotation, flip, random erasing, mixing images would be invalid transformations since they could change the output class of the image.
2. Looking at an object from a different angle that is not symmetrical (say front of car instead of top), different faces with same expression for human expression classification are examples of an invariance in visual recognition that cannot be solved by augmentation.
**Question 2:**

| Convolution Type |      Kernel Size       | Number of Kernels | Stride |                         Output Size                         |
| :--------------: | :--------------------: | :---------------: | :----: | :---------------------------------------------------------: |
|        1D        | h x 2 x  c<sub>1</sub> |   c<sub>2</sub>   |   1    |                 $1 \times (w-1) \times c_2$                 |
|        2D        | 3 x 3 x c<sub>1</sub>  |   c<sub>2</sub>   |   3    | $\lfloor h/3 \rfloor \times \lfloor w/3 \rfloor \times c_2$ |
|        3D        |       3 x 3 x 2        |         1         |   1    |            $(h-2) \times (w-2) \times (c_1 -1)$             |

**Question 3:**
For the new layers,
kernel size = $1 \times 1$
Since the blocks replace existing layers, the input and output shapes to and from the block must remain same.
So, 
**For CONV1:**
1st layer input channels = $CONV1$ o/p channels = $96$
2nd layer output channels = $CONV1$ o/p channels = $96$
1st layer o/p channels = 2nd layer o/p channels (since given that they have the same number of kernels) = $96$
2nd layer input channels = 1st layer o/p channels = $96$
Therefore, we can write the two new layers in the block as 
$1 \times 1 \times 96 \times 96$
$1 \times 1 \times 96 \times 96$
Similarly,
**For CONV2:**
The two new layers will be
$1 \times 1 \times 256 \times 256$
$1 \times 1 \times 256 \times 256$

Further, the output shape of the blocks must be the same. Given the kernel is $1 \times 1$ , this gives us 
$padding =0, stride =1$ 

1. The extra params excluding bias terms will be:

| Block             | Extra params (excluding bias)                           |
| ----------------- | ------------------------------------------------------- |
| CONV1 replacement | $(1 \times 1 \times 96 \times 96 ) \times 2 =18,432$    |
| CONV2 replacement | $(1 \times 1 \times 256 \times 256 ) \times 2 =131,072$ |

2. The majority of the extra memory needed will the memory needed to store the activations of the two new layers which will be used during backpropagation. The sizes of the outputs are the same as the respective original layers. Assuming each tensor is a 4 bytes float32. 

| Block             |             Extra memory needed for activations              | Extra memory  needed for parameters |
| :---------------- | :----------------------------------------------------------: | :---------------------------------: |
| CONV1 replacement | $(55 \times 55 \times 96 ) \times 2 \times 4 \space bytes = 2,323,200 \space bytes = 2.32 \space MB$ | $18,432 \times 4 \space bytes = 73,728 = 73.7 \space KB$ |
| CONV2 replacement | $(27 \times 27 \times 256 ) \times 2 \times 4 \space bytes = 1,492,992 \space bytes = 1.49 \space MB$ | $131,072 \times 4 \space bytes = 524,288 = 524.3 \space KB$ |

**Question 4:**

|                            Action                            | Impact on Bias | Impact on variance |
| :----------------------------------------------------------: | :------------: | :----------------: |
|                     Adding weight decay                      |   increases    |     decreases      |
|       Increasing the number of hidden units per layer        |   decreases    |     increases      |
|                Using dropout during training                 |   increases    |     decreases      |
| Adding more training data (drawn from the same distribution as before) |   no change    |     decreases      |
