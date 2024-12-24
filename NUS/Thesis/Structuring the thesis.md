
From: [Writing a Computer Science Thesis by Tobias Pfandzelter](https://raw.githubusercontent.com/pfandzelter/thesis-tips/main/thesis.pdf)

- Introduction:
	- where you ==give context for your research, introduce your research question, and outline your work==. It is supposed to give your reader an idea of what they can expect in your these, and it helps to set the scene for the text
	- ==It is also common to add a list of contributions==, i.e., bullet points on what you contribute to the research area, similarly to what we have done in Section 1.
- Background:
	- In a research paper, the background section normally serves two tasks: First, it introduces the terminology and definitions you use in the rest of your paper
	- Second, the background section lets you introduce the concepts you will use in the rest of your paper. ==Every non-trivial piece of information should be mentioned here.==
	- It shows the reader that you as a student have completely understood the research area you operate in. Conversely, if, during your writing process, you or your advisor notice that there is something missing from this section, you should go back into the literature and try to close that gap
- Approach:
	- This section should be named according to its contents (e.g., A Markov Model Approach to Linux Kernel Development), but the basic idea is that ==you introduce your idea: What solves your research question?== This section should be comparatively short, but in a research paper this part is often the most important one that everything revolves around.
- Evaluation:
	- You can simply write a small simulation environment (which will often be faster than using any of the existing, full-fledged simulation frameworks) and plug in a dataset or algorithm. You will likely need some ==existing approach or other baseline to compare your new approach to. Be sure to determine some metrics that you want to measure==, so you get relevant results.
- Discussion:
	- A discussion is not an explanation of your results – this should be part of your evaluation. Instead, a ==discussion critically evaluates your approach and evaluation==. Most things we do in computer science are not perfect: There will be edge cases, limitations, or scenarios where other approaches are better. This section is your opportunity to ==acknowledge the weaknesses of your thesis and discuss why or why not they matter (and how they could be addressed by someone else extending your approach)==
- Related Work:
	- In a related work section, ==you discuss other work in your area that aims to solve your research problem or related research problems==. The goal of this is not to discredit these papers but rather to show how your research builds on them, where you have used them for inspiration, and how different approaches may even be combined to create an even more effective solution (remember the point about the discussion section above that every approach will have weaknesses, including yours). Keep it nice and friendly!
	- ==Go about it one paper at a time. Mention the paper explicitly (e.g., “Doe et al. [10] do this and that...”), and summarize the main idea behind it. Then, explain why this is good or bad – also in comparison to your approach.== Sometimes, multiple papers have a categorically different approach (e.g., centralized vs. decentralized) than yours. In that case, group those papers and explain the advantages and disadvantages using an example. Remember that all of these approaches do actually have advantages – otherwise, they would not exist
	- ==A short related work section== might seem to be an indicator that your thesis is especially good because it solves a problem that no one else has looked at before and that you were now able to solve with your research superpowers – instead, it ==generally means that you do not quite know what you are talking about.==
- Conclusion:
	- Here, ==give a brief overview of everything you have done. Some research papers also use this to provide an outlook on future work you plan to do== – in most cases, students do not continue to work on their thesis projects, though (it might still be interesting to hear your thoughts on this if you have some ideas which are not implementation details/features


## Actual PDF

![](attachments/Writing%20a%20Computer%20Science%20Thesis_withMarginNotes.pdf)