# Project

## Introduction

The mini-project focuses on practical implementation. You are encouraged to investigate an optimization algorithm for a real-life machine learning / data science  application and gain insight into that algorithm. You should provide empirical evidence for some property of your chosen optimization algorithm. This property could be discussed in class or not and could be desirable or undesirable. The optimization algorithms can be anything of your choice. Don’t be scared to try variants not seen in class, as the project’s focus is not on theory. You can also choose any relevant ML/DS application. It does not matter if it is deep learning, linear models, random forests or less ML in flavor such as inverse problems, signal processing, imaging (denoising, deblurring) or something else.

- Grading. The project is mandatory and should be done in groups of 2-3 students. Project reports (3 page PDF) and code are due February 28th.
- Please inform me about your team and topic decision by the end of December **at the latest**. Earlier is better. 

## List of possible topics

The list below is by no means exhaustive. You are encouraged to freely chose very different aspects and topics as
long as they concern optimization and as long as you study them for any ML/DS-relevant application.

- **coordinate descent** vs **(accelerated) proximal gradient** for _Lasso_. 

  tags: [difficulty:easy], [reading:little], convex, covered in the lecture

- compare **variance reduction** methods

  tags: [difficulty:medium], [reading:little/medium], covered in the lecture
  + for example on an arbitrary logistic regression problem
  + convex vs nonconvex
  + (hard) on nonconvex problems if one starts close to a bad local minimum then SGD is more likely to escape. Can you find such an example.
  
- **Meta-Learning**: Can you learn the learning rate? The direction or curvature? More formally: Can a ML predict good hyperparameters for another model. See also the larger field of AutoML.

  tags: [medium/hard], [reading:medium], not covered in the lecture

- How well do **zero-order** optimization methods do for ML applications, compared to standard first-order
methods?

  tags: [difficulty:medium/hard], [reading:medium/lots], briefly covered in lecture

- What happens when you train deep nets with very **large batch sizes**. Is this influenced by the properties of the optimizer (SGD with or without momentum / Adam). What about the objective function value and what about generalization.

  tags: [difficulty:medium], [reading:medium] easier if you have DL knowledge,

- Explore the **role of momentum** for convex and nonconvex problems: SGD with or without momentum vs ADAM.
  What about heavy ball vs Nesterov?

  tags: [difficulty:easy/medium], [reading:little/medium], covered in the lecture

- Explore the practical **differences of first and second order** methods. Can you see a difference in the generalization error (for nonconvex models)? 

  tags: [difficulty:medium], [reading:little/medium], covered mostly in the lecture (second order for nonconvex requires some reading)

- The role of **duality** in optimization. Pick a problem which is generally solved by considering its dual - such as support vector machines - and explore the difference.

  tags: [difficulty:medium/hard], [reading:medium/lots]most theoretical topic out of all the ones mentioned here.

- Explore the role of different optimizers in **adversarial learning**, see [the cleverhans repo on github](https://github.com/cleverhans-lab/cleverhans). It should have all the relevant code available.

  tags: [difficulty:hard], [reading:medium], requires DL knowledge and some reading, but super interesting, see [ this paper ](https://arxiv.org/pdf/1706.06083.pdf%E4%B8%AD%E6%9C%89%E4%BD%93%E7%8E%B0%EF%BC%8C%E4%BB%A5%E5%90%8E%E8%AF%B4%E5%88%B0CW%E6%94%BB%E5%87%BB%E5%86%8D%E7%BB%86%E8%AF%B4%E3%80%82)

- Difference between **SGD and random reshuffling**.
  The way we presented SGD in the lecture, a sample is picked uniformly at random. This means that the same sample could be chosen multiple times in a row (or at least more frequently than others). Random reshuffling, as the name suggests, shuffles all samples and loops through them resulting in every sample being selected at the same frequency as others.

  tags: [difficulty:easy], [reading:little/medium], very relevant

- **Line search**: if the smoothness constant is not known there ways to find a good step size (or step length) by means of line search, most notably Armijo (many others: backtracking, Barzilai-Borwein, exact line search, etc.). Test the performance of these methods on a problems of your choice.

  tags: [difficulty:medium], [reading:medium/lots], not covered in the lecture

- **Matrix Factorization**: Many different versions: Recovering a low rank matrix. See Netflix problem. Compare convex and nonconvex formulations and different methods to solve them.

  tags: [difficulty:medium], [reading:medium/lots], briefly covered in the lecture


## Deliverables

- **Written Report**. You will write a maximum 3 page PDF report on your findings, using LaTeX. You can
use unlimited addition pages for references and for an appendix. The main paper should be self-contained!


- **Code**. In a language of your choice. Python with PyTorch is recommended for convenient access to gradients and optimizers. External libraries and existing implementations are allowed, if properly cited. You submit the complete executable and documented code, as a github repository either use the existing one for the exercises or use a new (public one) and send me the link. Rules for the code part:
    + Reproducibility: In your submission, provide a script like run.py or a notebook that produces all results and plots you use in the paper. (notebook would be my preference)
    + Documentation: Your system must be clearly described in your PDF report and also well-documented in the code itself. A useful ReadMe file must be provided.

- **Submission Deadline**: It would be great if you could submit them until the end of the semester (which would be the 31st of January), but I will set the 28th of February as the official deadline. Please bear in mind that it would be great if hand in your project before the oral exam so we can talk about it and would like to have all exams done by the end of February also.


## Grading Criteria

We will grade you on the scientific contribution you made, that is on the insights gained compared to standard
baseline methods. This is only possible based on a rigorous and fair empirical comparison. The criteria are

- **Solid comparison baselines supporting your claims**

Quantify the benefits of your method by providing clear quality measurements of the most important aspects and additions you chose for your model. Start with a very basic baseline, and demonstrate what improvements your contributions yield.

- **Reproducibility**

Your readers should be able to reproduce your results based on your report only. Describe what what hyper-parameters you selected and why, chose realistic and representative datasets, and clearly describe the overall pipeline you used.

- **Scientific novelty and creativity.**

You will likely be using more than the standard methods we saw in the course. Make sure that your report addresses the following points.
    + What is the specific aspect which you study, and why this is interesting and important.
    + Have similar experiments appeared in the literature? If yes, how are your experiments adding additional insight? Discuss the pros/cons of the existing studies compared to your approach.
    + How is the algorithm variant or the aspect of your choice helping for optimization speed, accuracy or generalization? For example, you should compare the optimization error with and without your object of study.

- **Writeup quality**
Some advice when writing a scientific report:
    + Try to convey a clear story giving the most relevant aspects of your findings. Learning what has not worked can additionally help the reader (and help them better understand why you have made the many choices you did), but focus on what is most relevant and interesting.
    + Before the submission, have an external person proofread your report. Use a spell-checker.
    + Plots are an excellent way to share information that might be hard to convey by writing. Your plots should be understandable, have axis labels, appropriate axis ranges, and a self-contained caption.


## Report Guidelines

Clearly describe your used methods, state your conclusions, and argue that the results you obtained make (or do
not make) sense and the reasons behind it. Keep the report short and to the point, with a strict limit of 3 pages.
References and additional technical do not count towards this page limit.
Use [this LATEXtemplate](https://github.com/AxelBohm/optimization-for-DS-lecture/blob/main/project/latex-example-paper/latex-template.pdf) to get started with the report. The file also contains some more helpful information on how to write a scientific report or paper.