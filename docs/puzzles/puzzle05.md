# Monty Hall with a Twist
**Difficulty:** ⭐⭐⭐  
**Topics:** Probability, Bayesian Inference

*Tags: Bayesian Inference, Conditional Probability, Information Revelation, Game Shows*

---

## Problem Statement

Monty Hall has introduced a new twist to his famous game, by generalizing the initial probabilities of where the car might be. Specifically, there are three doors, behind one of which there is a car, and behind the other two of which there are goats. Initially, door *i* has probability $p_i$ of having the car, where $p_1, p_2, p_3$ are known constants such that $0 < p_1 \leq p_2 \leq p_3 < 1$ and $p_1 + p_2 + p_3 = 1$. The contestant chooses a door. Monty then opens one of the remaining doors and reveals a goat, after which the contestant is offered the choice to switch to the other unopened door.

(a) Assume Monty knows in advance which door has the car. He always opens a door to reveal a goat, and if he has a choice of which door to open he chooses with equal probabilities. Suppose the contestant initially chooses door 3, and Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch? (If the decision depends on the $p_i$'s, give a simplified criterion in terms of them)

(b) Now assume Monty does not know in advance where the car is. He randomly chooses which door to open (other than the contestant's choice), with equal probability. (The game is spoiled if he reveals the car.) Suppose again that the contestant initially chooses door 3, and Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch? (If the decision depends on the $p_i$'s, give a simplified criterion in terms of them)

---

## Solution Outline

This problem is a variation (twist) of the classic Monty Hall problem. We use this to illustrate how Bayesian reasoning works when priors are non-uniform. The problem is not new but before we dive into how to solve this one we build intuition for a general framework that has helped me understand these problems and can be extended to more complex variants.

### A General Principle for Monty Hall Problems

The core of any Monty Hall problem is a Bayesian update. Monty's actions convey information and how informative those are depends entirely on what Monty knows and the choices he has.

Specifically, suppose contestant chooses door *k*, and Monty opens door *j*, revealing a goat. By Bayes' rule, the posterior that car is behind door *i* is:

$$ P(C_i | D_j) = \frac{P(D_j | C_i) \cdot P(C_i)}{P(D_j)} $$

where,

$$ P(D_j) = \sum_l P(D_j | C_l) \cdot P(C_l) $$

The prior $P(C_i) = p_i$ is usually given. The quantity that varies across different Monty Hall variants is the **likelihood** P(D_j | C_l) - probability that Monty opens door *j* given car is behind door *l*. This depends entirely on Monty's knowledge and strategy, hence, modeling his behavior is the most important step.

**The Uniform Case as a Special Example**

Suppose there are *n* doors with uniform priors $p_i = 1/n$ and the contestant chooses one of them, following which Monty opens *m* goat doors uniformly out of the remaining $n - 1$ doors.

Since all priors are equal, the posterior simplifies to being purely proportional to the likelihood:

$$ P(C_i | D_j) \propto P(D_j | C_i) $$

The probability that the **original choice** had car

$$ P(\text{original door}) = \frac{1}{n} $$

which under uniform priors ($p_i = 1/n$) **remains constant** as observing which specific door Monty opens does not update the posterior for the original door. This symmetry breaks down under non-uniform priors.

However, the probability that car lies behind one of the **other unopened doors** is

$$ \frac{n-1}{n} $$

Once Monty eliminates *m* doors, this probability gets **redistributed among the remaining unopened doors**, which gives

$$ P(\text{switching wins}) = \frac{n-1}{n} \cdot \frac{1}{n-m-1} $$

which we can understand as:
* **Residual probability:** the probability that the car was not behind the original door
* **Redistribution:** how that probability spreads across the remaining unopened doors

For the classical case $n = 3, m = 1$, gives the familiar result of $P(\text{switching wins}) = 2/3$.

This perspective is extremely useful and can come in handy when analyzing many Monty Hall variations.

**Why this Breaks Down Here**

Once priors are non-uniform, posteriors are no longer directly proportional to likelihoods. The full Bayes' rule must be applied directly, and Monty's behavior affects likelihoods in a non-trivial way.

### Solution to (a)

The Monty Hall problem and its variations become easy to understand and solve if you're able to isolate the different cases clearly which is how we attempt the solution. For the same purpose define,

* $C_i$: Car behind door *i*
* $D_i$: Monty opens door *i*

Monty **knows** where the car is and always opens a goat door.

We are given that the contestant chooses **door 3**, and Monty opens **door 2**, revealing a goat. We therefore want $P(C_3 | D_2)$ which we can write using conditional probability,

$$ P(C_3 | D_2) = \frac{P(C_3 \cap D_2)}{P(D_2)} $$

There are two scenarios which lead to Monty opening door 2.

**Case 1: Car behind door 3**

Monty is equally likely to open either door 1 or door 2,

$$ P(C_3 \cap D_2) = p_3 \cdot \frac{1}{2} $$

**Case 2: Car behind door 1**

Monty must open door 2.

$$ P(C_1 \cap D_2) = p_1 $$

This,

$$ P(D_2) = p_3 \cdot \frac{1}{2} + p_1 $$

Combining, we get

$$ P(C_3 | D_2) = \frac{p_3 \cdot \frac{1}{2}}{p_3 \cdot \frac{1}{2} + p_1} $$

which is also the probability of winning **without switching** (as we win if car is behind door 3 in that case). 

Hence, probability of winning **by switching** (event **S**) is,

$$ P(S | D_2) = 1 - P(C_3 | D_2) = \frac{p_1}{p_3 \cdot \frac{1}{2} + p_1} $$

**Switching Criterion**

Switching is beneficial when

$$ p_1 > \frac{p_3}{2} $$

Otherwise the contestant should stay.

Note how this differs from the standard result of *2/3*, since the initial probabilities are no longer symmetric.

### Solution to (b)

Now Monty **does not know** where the car is and randomly opens one of the two doors not chosen by the contestant.

For the case when the car is behind door 3, the situation is unchanged:

$$ P(C_3 \cap D_2) = p_3 \cdot \frac{1}{2} $$

If the car is behind door 1, now Monty doesn't always open door 2. Only half the cases in which the game continues (Monty doesn't reveal the car) matter. Hence,

$$ P(C_1 \cap D_2) = p_1 \cdot \frac{1}{2} $$

Thus,

$$ P(D_2) = p_3 \cdot \frac{1}{2} + p_1 \cdot \frac{1}{2} $$

Combining,

$$ P(C_3 | D_2) = \frac{p_3 \cdot \frac{1}{2}}{p_3 \cdot \frac{1}{2} + p_1 \cdot \frac{1}{2}} = \frac{p_3}{p_3 + p_1} $$

The probability of winning by switching (event **S**) is therefore,

$$ P(S | D_2) = 1 - P(C_3 | D_2) = \frac{p_1}{p_3 + p_1} $$

Since $p_3 \geq p_1$, we have

$$ P(S | D_2) \leq \frac{1}{2} $$

Thus, the contestant **should not switch**.

---

## Key Insight

The most important step in solving Monty Hall problems is **carefully modeling the information revealed by Monty's actions**.

Monty's choice depends on:

* whether Monty knows where the car is, and
* what choices Monty has available.

Because of that, any updates to prior must account for how likely Monty was to perform that particular action under each possible scenario.

Once scenarios are separated and conditional probabilities written cleanly, the problem becomes a simple application of Bayes' rule. Most of the confusion disappears once events are defined clearly and analyzed case by case.  
