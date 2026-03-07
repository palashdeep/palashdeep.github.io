# Monty Hall with a Twist

## Problem Statement

Monty Hall has introduced a new twist to his famous game, by generalizing the initial probabilities of where the car might be. Specifically, there are three doors, behind one of which there is a car, and behind the other two of which there are goats. Initially, door *i* has probability $p_i$ of having the car, where $p_1, p_2, p_3$ are known constants such that $0 < p_1 \leq p_2 \leq p_3 < 1$ and $p_1 + p_2 + p_3 = 1$. The contestant chooses a door. Monty then opens one of the remaining doors and reveals a goat, after with the contestant is offered the choice to swtich to the other unopened door.

(a) Assume Monty knows in advance which door has the car. He always opens a door to reveal a goat, and if he has a choice of which door to open he chooses with equal probabilities. Suppose the contestant initially chooses door 3, and Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch? (If the decision depends on the $p_i$'s, give a simplified criterion in terms of them.)

(b) Now assume Monty does not know in advance where the car is. He randomly chooses which door to open (other than the contestant's choice), with equal probability. (The game is spoiled if he reveals the car.) Suppose again that the contestant initially chooses door 3, and Monty opens door 2, revealing a goat. Given the above information, find the conditional probability that door 3 has the car. Should the contestant switch? (If the decision depends on the $p_i$'s, give a simplified criterion in terms of them.)

## Solution Outline

This problem is a variation(twist) of the classic Monty Hall problem. Before we dive into how to solve this one I want to state an important result that has helped me solve/understand the Monty Hall problems in general.

### A Genenal Principle for Monty Hall Problems

Suppose there are *n* doors and the contestant chooses one of them, following which Monty opens *m* doors out of the remaining $n - 1$ doors, each revealing goats. 

The probability that the **original choice** had car remains,

$$ P(\text{original door}) = \frac{1}{n} $$

which **remains constant** throughtout the game because nothing has happened that would affect the chance of initial correct guess. 

However, the probability that car lies behind one of the **other unopened doors** is

$$ \frac{n-1}{n} $$

Once Monty eliminates *m* doors, this probability gets **redistributed among the remaining unopened doors**, which gives

$$ P(\text{success with switching}) = \frac{n-1}{n} \cdot \frac{1}{n-m-1} $$

which we can understand as:
* **Residual probability:** the probability that the car was not behind the original door
* **Redistribution:** how that probability spreads across the remaining unopened doors

This perspective is extremely useful and can come in handy when analyzing many Monty Hall variations.

### Solution to (a)

The Monty Hall problem and its variations become easy to understand and solve if you're able to isolate the different cases clearly which is how we attempt the solution. For the same purpose define,

* $C_i$: car behind door *i*
* $D_i$: Monty opens door *i*

Monty **knows** where the car is and always opens a goat door.

We are given that the contestant chooses **door 3**, and Monty opens **door 2**. We therefore want $P(C_3 | D_2)$ which we can write using conditional probability,

$$ P(C_3 | D_2) = \frac{P(C_3 \cap D_2 )}{P(D_2)} $$

There are two scenarios which lead to Monty opening door 2.

**Case 1: Car behind door 3**

Monty is equally likey to open either door 1 or door 2,

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

Now Monty **does not know** where the car is and randomly opens of the two doors not chosen by the contestant.

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

## Key Insight

The most important step in solving Monty Hall problems is **carefully modeling the information revealed by Monty's actions**.

Monty's choice depends on:

* whether Monty knows where the car is, and
* what choices Monty has available.

Because of that, any updates to prior must account for how likely Monty was to perform that particular action under each possible scenario.

Once scenarios are separated and conditional probabilities written cleanly, the problem becomes a simple application of Bayes' rule. Most of the confusion disappears once events are defined clearly and analyzed case by case.  
