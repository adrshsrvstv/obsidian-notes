
### Prof Soh

This thesis studies the application of diffusion models, specifically focusing on Schrödinger Bridge diffusion, in the context of robotic task planning. The research hypothesizes that starting from a distribution closer to the target distribution in diffusion models can enhance sampling efficiency without sacrificing generation quality.

**Major comments**:

**Chapter 1**: Provides a succinct introduction to diffusion models and their diverse applications, setting a clear foundation for the thesis. However, the chapter lacks a comprehensive overview of the thesis, including its scope and objectives. More contextual background on the importance of diffusion models in robotics and AI would enhance its depth (what can diffusion models do that other models lack).

**Chapter 2**: The chapter on background and related work how diffusion models are utilized in robotics, to provide necessary context and framework for the thesis. The section on Diffuser in Chapter 3 should be moved to Chapter 2.

**Chapter 3**: provides an exploration of I2SB for planning and a description of experimental setups and findings. The chapter lacks clear a robust analysis on why certain the method did not work as anticipated. The experiments could have been more extensive (e.g., different environments, alternative formulations) to better examine why the hypothesis was not supported. Some of this is given in the Chapter 4 but should be in a discussion section of chapter 3.

**Chapter 4**: Provides an analysis of the findings, particularly why the Schrödinger Bridge model didn't meet expectations and suggests future research directions. The chapter is brief and only provides very short potential reasons for the problems encountered. It also lacks broader implications.

Overall, the thesis presents an exploration into the use of approximate schrodinger bridge models in robotic task planning. However, it requires more comprehensive coverage in its introductory and background sections, a deeper analysis of experimental findings, especially in cases where the results did not support the hypothesis, and a more detailed conclusion to broaden the context and implications of the research. It just about meets the bar of acceptance for a Mcomp project thesis.


### Prof Hooi



Motivation (in introduction and section 2) for the use of SB is not sufficiently clear and detailed. The expected benefits of using SB (and how they relate to the SB model) should be clearly explained (it may be fine to defer some details to the cited papers, but you should still give enough high level explanation so it is reasonably clear to the reader). For example, 1 motivation is that SB allows for the use of informative priors, but this is hardly explained (especially in chapter 2). The other motivation is that SB can be sampled in closed form, but it is not clearly explained why this is the case considering that SB is supposed to be a generalization of DDPM (so how can it improve the efficiency of sampling then?) The current explanation in chapter 2 is too brief and doesn't really answer this clearly.  
  
Since the thesis is mostly focused on the Diffuser approach, it would be better to give a clearer explanation of this paper (again, fine to leave out specific details, but there should still be enough detail so the reader can at least understand from a high level view)  
  
Figure 3 is not explained clearly enough - e.g. the meaning of the points and colors, and where the start and end points are for these cases. E.g. are the start and end points the same for Figure 3.7 and Figure 3.9? All these details needed to understand the figures should be explained clearly. Also, the construction of these priors is also not totally clear (e.g. how exactly to create a prior from a "straight line joining the start and goal locations"? And how is the 2 layer MLP trained, and what are its inputs and outputs, etc?) Sufficient details should be given for reproducibility (i.e., the reader should be able to reproduce basically everything you have done based on your explanations)  
  
Overall, the analysis and experimental results are still quite superficial, and lacking in clear explanations especially for the performance gap between DDPM and SB. While some explanations are mentioned, there is a lack of details or experimental evidence for them (e.g. one explanation is the "averaging effect", but it is not explained how the averaging effect explains the observed drops in performance with number of training steps, and there is no clear evidence given for this averaging effect). Hence, I suggest doing more experiments to provide better analysis / understanding of this performance gap (e.g. to verify that the proposed explanations can really explain the difference between DDPM and SB), and also improve the quality and level of detail of the writing as explained above, and check with your advisor to make sure the experiments are sufficient before resubmitting.