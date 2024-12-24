---
title: Overall Structure
subtitle: 
author:
  - Adarsh Srivastava
date: 8 May, 2024
tags:
---



### Intro

> [!Guidelines]
> 
> - give context for your research, introduce your research question, and outline your work
> - It is also common to add a list of contributions
> 

- What is the problem
- How have we been solving that
- What are the issues with that
- What are alternate methods to solve similar problems
- What do you propose as the hypothesis - what's the idea
- What are your main results
- How is the rest of the thesis structured - talk about each section and what it talks about. 
- List of main contributions
- Summarize - give a small conclusion or takeaway from the thesis


Addresses: 
Prof Soh: `However, the chapter lacks a comprehensive overview of the thesis, including its scope and objectives. More contextual background on the importance of diffusion models in robotics and AI would enhance its depth (what can diffusion models do that other models lack).`

and

Prof. Hooi: `Motivation (in introduction and section 2) for the use of SB is not sufficiently clear and detailed. The expected benefits of using SB (and how they relate to the SB model) should be clearly explained (it may be fine to defer some details to the cited papers, but you should still give enough high level explanation so it is reasonably clear to the reader).`

### Background

> [!Guidelines]
> - Every non-trivial piece of information should be mentioned here.

- Have sections on all the major frameworks and approaches you build on, which are:
	- Informative priors
	- Planning in RL
	- Diffusion models
	- Schrodinger bridges
	- I2SB
	- Diffuser
- Anything else?

**Addresses**:

- Prof Soh: `The chapter on background and related work how diffusion models are utilized in robotics, to provide necessary context and framework for the thesis. The section on Diffuser in Chapter 3 should be moved to Chapter 2.`

- Prof Hooi: `Since the thesis is mostly focused on the Diffuser approach, it would be better to give a clearer explanation of this paper (again, fine to leave out specific details, but there should still be enough detail so the reader can at least understand from a high level view)`

- Prof Hooi: `For example, 1 motivation is that SB allows for the use of informative priors, but this is hardly explained (especially in chapter 2). The other motivation is that SB can be sampled in closed form, but it is not clearly explained why this is the case considering that SB is supposed to be a generalization of DDPM (so how can it improve the efficiency of sampling then?) The current explanation in chapter 2 is too brief and doesn't really answer this clearly.`
### Approach

> [!Guidelines]
> - you introduce your idea: What solves your research question?
> - This section should be comparatively short
> 

- Introduce your own approach
- how you mixed up the ideas discussed above, and any particular implementation details



- components of the architecture - network, diffusion formulation, and prior
- notion of a prior
- this is how you solve the problem - first theoretically, then say how you set up the code. Give equations in terms of distributions etc. Introduce the notion of a prior and talk about the various possibilities.
- setup that allows the NFE and diffusion steps to be different - talk about that

**Addresses**: 
No comments on this


### Evaluation

> [!Guidelines]
> - existing approach or other baseline to compare your new approach to. Be sure to determine some metrics that you want to measure

- the metrics you use to evaluate
- **the experiments you use** - *where we  need more experimental data*
- the benchmarks compared to and why
- the actual results obtained for each of the experiments


- give details about the benchmark
- give details about the particular task
- give details about the metrics to evaluate on
- then, talk about the priors constructed for the experiments given the task in question.
- then, present your results in a systematic manner
- annotate the images and tell what the colors mean
- 

**Addresses**: 
- Prof Hooi: `Figure 3 is not explained clearly enough - e.g. the meaning of the points and colors, and where the start and end points are for these cases. E.g. are the start and end points the same for Figure 3.7 and Figure 3.9? All these details needed to understand the figures should be explained clearly. Also, the construction of these priors is also not totally clear (e.g. how exactly to create a prior from a "straight line joining the start and goal locations"? And how is the 2 layer MLP trained, and what are its inputs and outputs, etc?) Sufficient details should be given for reproducibility (i.e., the reader should be able to reproduce basically everything you have done based on your explanations)`

### Discussion

> [!Guidelines]
> - discussion critically evaluates your approach and evaluation
> - acknowledge the weaknesses of your thesis and discuss why or why not they matter (and how they could be addressed by someone else extending your approach)
> 
> 

- Discuss the results and what they might mean, and what the possible reasons for that are.
- Discuss possible reasons for why things did not work.
- Need an explanation of averaging effect.
- Explanation of performance gap.

**Addresses**: 

- Prof Soh:  `However, it requires more comprehensive coverage in its introductory and background sections, a deeper analysis of experimental findings, especially in cases where the results did not support the hypothesis, and a more detailed conclusion to broaden the context and implications of the research.`

- Prof Hooi: `Overall, the analysis and experimental results are still quite superficial, and lacking in clear explanations especially for the performance gap between DDPM and SB. While some explanations are mentioned, there is a lack of details or experimental evidence for them (e.g. one explanation is the "averaging effect", but it is not explained how the averaging effect explains the observed drops in performance with number of training steps, and there is no clear evidence given for this averaging effect). Hence, I suggest doing more experiments to provide better analysis / understanding of this performance gap (e.g. to verify that the proposed explanations can really explain the difference between DDPM and SB), and also improve the quality and level of detail of the writing as explained above, and check with your advisor to make sure the experiments are sufficient before resubmitting.`

### Related work

> [!Guidelines]
> - you discuss other work in your area that aims to solve your research problem or related research problems.
> - how how your research builds on them, where you have used them for inspiration, and how different approaches may even be combined to create an even more effective solution (remember the point about the discussion section above that every approach will have weaknesses, including yours). Keep it nice and friendly!
> - Go about it one paper at a time. Mention the paper explicitly (e.g., “Doe et al. [10] do this and that...”), and summarize the main idea behind it. Then, explain why this is good or bad – also in comparison to your approach.
> - make sure this is comprehensive, because ==A short related work section generally means that you do not quite know what you are talking about==

- Discuss the DDBM paper, and what its results are, and how things could be with that approach
- stochastic interpolants paper summary

Addresses: 

### Conclusion

> [!Guidelines]
> - give a brief overview of everything you have done. Some research papers also use this to provide an outlook on future work you plan to do

Addresses: 

-----

## Meeting with Prof.

What did Prof Soh say on my meeting with him?

We don't necessarily need theoretical explanation for everything, but more experimental evidence is needed to solidify what you are saying. You can use experiments to justify what your conclusion is

----- 

## So what's the plan?

- 12th and 13th: Background, approach, evaluation part of report for existing experiment
- 14th: figure more experiments - code, then while it is training - Discussion, related work, 
- 15th and 16th: work on more experiments
- 17th: get any experimental results
- 18th: conclusion, Intro
- 19th: Any last fixes, submit.


We absolutely need to submit by 17th



-----

Writing this on 17th:

I have so far spent a great deal of time reading papers for intro and background, but haven't written anything yet. What do we do from here on:

Spent 17th writing the background, and the intro + related works section. 

We need tomorrow and day after for the experiments and the conclusion etc

If I spend 18th on the experiments, I can maybe fix the report in the time it runs more. 

If I have model trained, results won't take much more time.

Writing conclusion? Can I do it in one more day? 

So:
17th - intro background related work
18th - design experiment and train
19th - write the conclusion
20th morning submit. 

I absolutely need to submit before Jin messages again, no matter what. If I don't I will bring upon financial and academic ruin upon myself, and will certainly not graduate. 

Do I trust myself to do this work? 

I cannot do anything about the past - I have been the way I have been for all sorts of reasons - my own fears, resentments to other people, escaping, etc. NUS doesn't care about any of those. I need to give profs 2 to 3 days to read my report and give their feedback. And I need to make sure all their comments are addressed. 

Do your efforts justice - you have spent a lot of effort and made a lot of sacrifices to come here and earn this degree. You don't need to succeed or fail to prove anything to anyone else. You need to do this for yourself.

For the next 3 days - don't think about it. Just do it. Next review on 20th morning. 


-----

SB Notes, what to write:

- mention the original intent of the paper - and the usecases they use it for

`h Gaussian white noise, which has little or no structural information of the clean data distribution`

`. This shares similarity with imageto-image translation GANs (Zhu et al., 2017; Huang et al., 2018). Constructing these diffusion bridges often necessitates a new computational framework for reversing general diffusion processes`

- mention usecases
`We validate our method in many image restoration tasks including super-resolution, deblurring, inpainting, and JPEG restoration on ImageNet 256×256`

- show performance on some images to help the reader get an idea
- technical details - which are also the core technical details of our paper

`It is known that SB generalizes SGM to nonlinear structur`


- key results of their paper


- limitations:
	- `. Note that I2SB requires pair information compared to standard SB.`



```latex
\subsection{Brownian Bridges}

A Brownian bridge is a continuous-time stochastic process $B(t)$ whose probability distribution is the conditional probability distribution of a standard Wiener process $W(t)$ (a mathematical model of Brownian motion) subject to the condition (when standardized) that $W(T) = 0$, so that the process is pinned to the same value at both $t = 0$ and $t = T$. The state distribution at each time step of a Brownian bridge process starting from point $\boldsymbol{x}_0 \sim q_{\operatorname{data}}\left(\boldsymbol{x}_0\right)$ at $t = 0$ and ending at point ${x}_T$ at $t = T$ can be formulated as:

\begin{equation}
p\left(\boldsymbol{x}_t \mid \boldsymbol{x}_0, \boldsymbol{x}_T\right)=\mathcal{N}\left(\left(1-\frac{t}{T}\right) \boldsymbol{x}_0+\frac{t}{T} \boldsymbol{x}_T, \frac{t(T-t)}{T} \boldsymbol{I}\right)
\end{equation}

```


`Finally, we characterize in how I2SB reduces to an optimal transport ODE (Peyr´ e et al., 2019) when the diffusion vanishes, strengthening the algorithmic connection among dynamic generative models.`

```latex

\begin{equation}\label{closedformsampling}
q\left(X_n \mid X_0, X_N\right)=\int \Pi_{k=n}^{N-1} p\left(X_k \mid X_0, X_{k+1}\right) \mathrm{d} X_{k+1}
\end{equation}

They are trained on UNet like time-dependent networks to optimize the objective:

\begin{equation}
\left\|\epsilon\left(X_t, t ; \theta\right)-\frac{X_t-X_0}{\sigma_t}\right\|
\end{equation}

```


kkjh


```latex
\subsection{Brownian Bridges}

A Brownian bridge is a continuous-time stochastic process $B(t)$ whose probability distribution is the conditional probability distribution of a standard Wiener process $W(t)$ (a mathematical model of Brownian motion) subject to the condition (when standardized) that $W(T) = 0$, so that the process is pinned to the same value at both $t = 0$ and $t = T$. The state distribution at each time step of a Brownian bridge process starting from point $\boldsymbol{x}_0 \sim q_{\operatorname{data}}\left(\boldsymbol{x}_0\right)$ at $t = 0$ and ending at point ${x}_T$ at $t = T$ can be formulated as:

\begin{equation}
p\left(\boldsymbol{x}_t \mid \boldsymbol{x}_0, \boldsymbol{x}_T\right)=\mathcal{N}\left(\left(1-\frac{t}{T}\right) \boldsymbol{x}_0+\frac{t}{T} \boldsymbol{x}_T, \frac{t(T-t)}{T} \boldsymbol{I}\right)
\end{equation}
```



```latex

Diffusion models have emerged as a powerful class generative models, because of their superior sample quality and more stable training compared to earlier approaches such Variational Autoencoders (VAE) and Generative Adversarial Networks (GAN). They have exhibited state-of-the-art performance in a wide array of domains such as image and video~\parencite{luo2021diffusion}~\parencite{lugmayr2022repaint}~\parencite{ho2022imagen}, language processing~\parencite{li2022diffusionlm}~\parencite{austin2023structured}, audio~\parencite{Lee_2021}~\parencite{kong2021diffwave}, and drug discovery~\parencite{xu2022geodiff}~\parencite{schneuing2023structurebased}~\parencite{wu2022diffusionbased}.

Of particular interest to us is their use on image-to-image translation tasks. While \cite{pallete} and \cite{xia2023diffi2i} use standard diffusion models to add noise partially and then denoise to the desired image distribution, some recent models have explored using bridge models to go directly from one image to another without having separate noise adding and denoising processes~\parencite{debortoli2023diffusion}~\parencite{chen2023likelihood}~\parencite{i2sb}~\parencite{li2023bbdm}~\parencite{ddbm}.

```

