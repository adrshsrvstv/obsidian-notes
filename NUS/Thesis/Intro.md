
- **Structure**:
	- What is the problem
	- How have we been solving that
	- What are the issues with that
	- What are alternate methods to solve similar problems
	- What do you propose as the hypothesis - what's the idea
	- What are your main results
	- How is the rest of the thesis structured - talk about each section and what it talks about. 
	- List of main contributions
	- Summarize - give a small conclusion or takeaway from the thesis


- Where to look for ideas/similar stuff:
	- diffuser
	- i2sb
	- ddbm

### Intro new 

- Talk about how RL from scratch is expensive, and how informative priors can sometimes be constructed. Talk about how transfer learning can port skills, but what if there are no skills to port.
- Talk about the idea of incorporating domain or task contraints in a natural way in RL algorithms, or using easily trainable worse performing algorithms to train better performing algorithms using more expensive methods.

The RL framework has gained popularity as learning methods have been developed that are capable of handling increasingly complex problems. However, when RL agents begin learning from a clean slate, mastering difficult tasks is often slow or infeasible, and thus a significant amount of current RL research focuses on improving the speed of learning by exploiting domain expertise with varying amounts of human-provided knowledge


`One flexible way to utilize unstructured prior experience is by extracting skills, temporally extended actions that represent useful behaviors, which can be repurposed to solve downstream tasks. Skills can be learned from data without any task or reward information and can be transferred to new tasks and even new environment configurations. Prior work has learned skill libraries from data collected by humans [6, 7, 8, 9, 10] or by agents autonomously exploring the world [11, 12]. To solve a downstream task using the learned skills, these approaches train a high-level policy whose action space is the set of extracted skills. The dimensionality of this action space scales with the number of skills. Thus, the large skill libraries extracted from rich datasets can, somewhat paradoxically, lead to worse learning efficiency on the downstream task, since the agent needs to collect large amounts of experience to perform the necessary exploration in the space of skills [13].`

from Accelerating Reinforcement Learning with Learned Skill Priors


`Intelligent agents rely heavily on prior experience when learning a new task, yet most modern reinforcement learning (RL) approaches learn every task from scratch. One approach for leveraging prior knowledge is to transfer skills learned on prior tasks to the new task. However, as the amount of prior experience increases, the number of transferable skills grows too, making it challenging to explore the full set of available skills during downstream learning. Yet, intuitively, not all skills should be explored with equal probability; instead information e.g. about the current environment state can hint which skills are promising to explore. In this work, we propose to implement this intuition by learning a prior over skills. We propose a deep latent variable model that jointly learns an embedding space of skills and the skill prior from offline agent experience.`

Ok, stop here. Come back later.

also look at Heuristic-Guided Reinforcement Learning


problems in RL

sample efficiency

what else?

long horizon credit assignment


The central premise of this work is the use of source policies for diffusion-based imitation learning: we posit that starting with a more informative source density facilitates the shaping of the target density.


This can alleviate challenges due to sample efficiency and ex- ploration by providing the algorithm with an initial dataset to “kick-start" the learning process, either in the form of high-quality expert demonstrations, or even low-quality but high-coverage exploratory trajectories.