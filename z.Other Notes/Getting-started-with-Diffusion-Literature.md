
Summary of the most important papers and blogs about diffusion models for students to learn about diffusion models. Also contains an overview of all published robotics diffusion papers

## Learning about Diffusion models 

While there exist many tutorials for Diffusion models, below you can find an overview of some introduction blog posts and video, which I found the most intuitive and useful:

- [What are Diffusion Models?](https://www.youtube.com/watch?v=fbLgFrlTnGU&t=1s): an introduction video, which introduces the general idea of diffusion models and some high-level math about how the model works
- [Generative Modeling by Estimating Gradients of the Data Distribution](https://yang-song.net/blog/2021/score/): blog post from the one of the most influential authors in this area, which introduces diffusion models from the score-based perspective 
- [What are Diffusion Models](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/): a in-depth blog post about the theory of diffusion models with a general  summary on how diffusion model improved over time 
- [Understanding Diffusion Models](https://arxiv.org/pdf/2208.11970.pdf): an in-depth explanation paper, which explains the diffusion models from both perspectives with detailed derivations

If you don't like reading blog posts and prefer the original papers, below you can find a list with the most important diffusion theory papers:

- [paper link](http://proceedings.mlr.press/v37/sohl-dickstein15.pdf), Sohl-Dickstein, Jascha, et al. "Deep unsupervised learning using nonequilibrium thermodynamics." _International Conference on Machine Learning_. PMLR, 2015.
- [paper link](https://proceedings.neurips.cc/paper/2020/file/4c5bcfec8584af0d967f1ab10179ca4b-Paper.pdf), Ho, Jonathan, Ajay Jain, and Pieter Abbeel. "Denoising diffusion probabilistic models." _Advances in Neural Information Processing Systems_ 33 (2020): 6840-6851.
- [paper link](https://arxiv.org/pdf/2011.13456),Song, Yang, et al. "Score-Based Generative Modeling through Stochastic Differential Equations." _International Conference on Learning Representations_. 2020.
- [paper link](https://arxiv.org/pdf/2207.12598), Ho, Jonathan, and Tim Salimans. "Classifier-Free Diffusion Guidance." _NeurIPS 2021 Workshop on Deep Generative Models and Downstream Applications_. 2021.

Our current model implementation is based on this paper:

- [paper link](https://arxiv.org/pdf/2206.00364), Karras, Tero, et al. "Elucidating the Design Space of Diffusion-Based Generative Models." _Advances in Neural Information Processing Systems_ 35 (2022)

A general list with all published diffusion papers can be found here: [Whats the score?](https://scorebasedgenerativemodeling.github.io/)


## Diffusion in robotics
Since the modern diffusion models have been around for only 2 years, the literature about diffusion models in the context of robotics is still small. Below you can find most robotics diffusion papers, which have been published or uploaded to arxiv so far:

---

### Imitation Learning and Policy Learning

- Chi, Cheng, et al. ["Diffusion Policy: Visuomotor Policy Learning via Action Diffusion."](https://arxiv.org/pdf/2303.04137) arXiv preprint arXiv:2303.04137 (2023).

- Pearce, Tim, et al. ["Imitating human behaviour with diffusion models."](https://openreview.net/pdf?id=Pv1GPQzRrC8) 
" _International Conference on Learning Representations_. 2023.

- Dai, Yilun, et al. ["Learning Universal Policies via Text-Guided Video Generation."](https://arxiv.org/pdf/2302.00111) arXiv preprint arXiv:2302.00111 (2023).

- Kapelyukh, Ivan, Vitalis Vosylius, and Edward Johns. ["DALL-E-Bot: Introducing Web-Scale Diffusion Models to Robotics."](https://openreview.net/forum?id=HzOy6lUzPj1) CoRL 2022 Workshop on Pre-training Robot Learning.

- Yu, Tianhe, et al. ["Scaling robot learning with semantically imagined experience."](https://arxiv.org/pdf/2302.11550.pdf) arXiv preprint arXiv:2302.11550 (2023).

--- 

### Offline RL

- Ajay, Anurag, et al. ["Is Conditional Generative Modeling all you need for Decision-Making?."](https://arxiv.org/pdf/2211.15657) _International Conference on Learning Representations_. 2023.

- Janner, Michael, et al. ["Planning with Diffusion for Flexible Behavior Synthesis."](https://arxiv.org/pdf/2205.09991.pdf) _International Conference on Learning Representations_. 2022.
- Wang, Zhendong, Jonathan J. Hunt, and Mingyuan Zhou. ["Diffusion policies as an expressive policy class for offline reinforcement learning."](https://arxiv.org/pdf/2208.06193.pdf)  _International Conference on Learning Representations_. 2023.

- Brehmer, Johann, et al. ["EDGI: Equivariant Diffusion for Planning with Embodied Agents."](https://arxiv.org/pdf/2303.12410) arXiv preprint arXiv:2303.12410 (2023).

- Chen, Huayu, et al. ["Offline Reinforcement Learning via High-Fidelity Generative Behavior Modeling."](https://openreview.net/pdf?id=42zs3qa2kpy)" _International Conference on Learning Representations_. 2023.

- Liang, Zhixuan, et al. ["AdaptDiffuser: Diffusion Models as Adaptive Self-evolving Planners."](https://arxiv.org/pdf/2302.01877) arXiv preprint arXiv:2302.01877 (2023).

--- 

### Grasping

- Urain, Julen, et al. ["SE (3)-DiffusionFields: Learning cost functions for joint grasp and motion optimization through diffusion."](https://arxiv.org/pdf/2209.03855) ICRA 2023

- Liu, Weiyu, et al. ["StructDiffusion: Object-centric diffusion for semantic rearrangement of novel objects."](https://arxiv.org/pdf/2211.04604) arXiv preprint arXiv:2211.04604 (2022).

- Mishra, Utkarsh A., and Yongxin Chen. ["ReorientDiff: Diffusion Model based Reorientation for Object Manipulation."](https://arxiv.org/pdf/2303.12700) arXiv preprint arXiv:2303.12700 (2023).

--- 

## Diffusion history

Diffusion models are a generative model type based on the initial idea of  [Sohl-Dickstein et al., (2015)](https://arxiv.org/abs/1503.03585). The model is inspired by non-equilibrium thermodynamics and learns to invert a diffusion process. This process is a Markov chain consisting of diffusion steps, which add random Gaussian noise to a data sample. The diffusion model is used to learn to invert this process. While the paper was presented  in 2015, it took several years for the diffusion models to get widespread attention in the research community. Diffusion models are a type of generative model and in this field, the main focus are vision based applications, thus all theory papers mentioned in the text below are mostly focused on image synthesis or similar tasks related to it. 

Diffusion models can be viewed from two perspectives: one is based on the initial idea of  of  [Sohl-Dickstein et al., (2015)](https://arxiv.org/abs/1503.03585) and the other is based on a different direction of research: score-based generative models. [Song & Ermon, (2019)](https://proceedings.neurips.cc/paper/2019/file/3001ef257407d5a371a96dcd947c7d93-Paper.pdf) introduced the score-based generative models category. They presented the  _noise-conditioned score network (NCSN)_, which is a predecessor to diffusion model. The main idea of the paper is to learn the score function of the unknown data distribution with a neural network. While this idea had been around before, their paper and the follow-up work [Song & Ermon (2020)](https://arxiv.org/abs/2006.09011) enabled scaling score-based models to high-dimension data distributions and made them competitive on image-generation tasks. The key idea in their work was to perturb the data distribution with different levels of Gaussian noise and learn a noise-conditional score model to predict the score of the model.

In the following year [Ho et al., (2020)](https://arxiv.org/abs/2006.11239) introduced  _denoising diffusion probabilistic models (DDPM)_, which was the stepping stone for the success of Diffusion models. It still was not competetive to state-of-the-art models such as GANs. However, this changed rapidly in the following year. [Nichol & Dhariwal (2021)](https://arxiv.org/abs/2105.05233) improved upon the previous paper and proved, that Diffusion models are competitive with GANs on image synthesis tasks. It is important to note, that Diffusion models are not the jack of all trades. GANs are still relevant and have far lower sampling costs. Moreover, diffusion models still struggle with certain traits such as face generation. Another important idea for diffusion models in the context of image generation has been the introduction of _latent diffusion models_ in [Rombach & Blattman et al., (2022)](https://arxiv.org/abs/2112.1075). By training the diffusion model in the latent space instead of image space directly, they were able to improve the sampling and training speed and made it possible for everyone to run their own diffusion model on local PCs with a single GPU. Recent AI generated art is mostly based on the stable AI implementation of latent diffusion models and is open source: [Github repo](https://github.com/CompVis/stable-diffusion). Check out some cool Diffusion art on the [stable-diffusion-reddit](https://www.reddit.com/r/StableDiffusion/).

**Conditional Diffusion models**
The initial diffusion models are usually trained on marginal distributions $p(x)$. One research area of interest is the conditional image generation. Therefore, we need conditional diffusion models to _guide_ the generation process into a desired direction. Right now, there are two popular methods to enable conditional generation with diffusion models:
- Classifier Guided Diffusion by [Dhariwal & Nichol (2021)](https://arxiv.org/abs/2105.05233)
- Classifier-Free Guidance by [Ho & Salimans, (2021)](https://openreview.net/forum?id=qw8AKxfYbI)


**Diffusion models perspectives**

As mentioned before, diffusion models can be viewed from two different perspectives:
- the denoising diffusion probabilistic perspective based on [Ho et al., (2020)](https://arxiv.org/abs/2006.11239) 
- the score-based model perspective based on  [Song & Ermon, (2019)](https://proceedings.neurips.cc/paper/2019/file/3001ef257407d5a371a96dcd947c7d93-Paper.pdf)
There has been a lot of effort to combine these two views into one general framework. The best generalization has been the idea of stochastic differential equations (SDEs) first presented in [Song et al. (2021)](https://arxiv.org/pdf/2011.13456).

While diffusion models have successfully conquered the generative model area, they are not common in robotics. Only a few prior work exist in this regard. Why should we use diffusion models in robotics? What are the useful properties of diffusion models? 

Diffusion models offer:
- high expressiveness: can learn arbitrarily complicated data-distributions 
- stable and easy to train, especially in contrast GANs or EBMs
- multimodality: they are able to learn complicated multimodal distributions

