# Is My Number Higher?

## Problem Statement

A referee independently draws two numbers *x* and *y* uniformly from $[0, 1]$. The numbers are written down on two peices of paper and put into different envelopes.

(a) You are given one of the envelopes. You open the envelope and observe the number. Now you must guess whether the other number is higher or lower. What is the probability you make the correct guess?

(b) Both envelopes are given to you and your friend (one each). You can only look into your own envelope. Simultaneously and without communicating, both of you announce either "mine is higher" or "mine is lower". The team wins if at least one announcement is coorect. Before the game starts, you can decide upon any strategy you may like. What is the team's win probability under random independent guessing? What is the optimal strategy and what does it achieve?

## Solution Outline

Many decision problems with a lack of information look impossible at first glance. Yet surprisingly, small structural tricks can be used to get to strategies that outperform random guessing.

This set of puzzles are exactly that but the strategies for both are quite different. We will solve both of these simultaneously.

### The Naive Trap

For the game with single player, at first it seems that the probability of guessing correctly is 50%, i.e., it can be either right or wrong.

For the two player game, similarly the naive answer to the probability of winning with at least one guess correct would be 50%, as neither of the player knows the other number. There's nothing to be done.

The reasoning in both cases is wrong in a subtle way. For the first case you can do better without much effort by a simple strategy which we discuss later. But for the second part each player being stuck at 50% and the team stuck at 50% are different things. The joint distribution of who is right or wrong depends on the strategy which we discuss in the next sections.

### Random Guessing

For the single player game, random guessing, let's say by flipping a coin, indeed gives a probability of success as 50%, with no strategy whatsoever.

But what about the case with two players. Let's say both players ignore their numbers entirely and each one independently announces "higher" or "lower", again by flipping a private coin.

What is the probability that both of them will be wrong?

Both of them wrong will require exactly one of:

* Player 1 says "higher" but $x < y$, and Player 2 says "lower" but $y > x$
* Player 1 says "higher" but $x > y$ and Player 2 says "lower" but $y < x$

Since the announcements are independent of each other and of the numbers, each event independently has 50% probability of occuring,

$$ P(\text{both wrong}) = \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$$

which implies:

$$ P(\text{win}) = \frac{3}{4} $$

This beats naive intuition. The team wins 75% of the time by doing nothing clever. The negative correlation between "who is right" which is built into the structure of the game comes to a save.

### Optimal Strategy

The optimal strategy for both the single player and two player games is similar but the reason they work is quite different and the success probability achieved is also not the same.

Define the optimal strategy as choosing a random threshold **T**. If $x > T$, guess your number as higher, otherwise guess lower. Now let's see how this strategy performs in each of the cases.

For the single player game, assume the two numbers be:

$$x < y$$

You will observe either *x* or *y* with equal probability. Now consider cases for where *T* might lie,

**Case 1 - *T* is the numbers**

$$x < T < y$$

Then the rule works perfectly:

* If you see *x* : $x < T$, you guess lower which is correct.
* If you see *y* : $y > T$, you guess higher which is correct. 

So for this case, you are correct 100% of the time.

**Case 2 - *T* outside the interval**

$$T < x, \text{or} T > y$$

Then the rule is basically random as threshold provides no information - you are correct 50% of the time.

**Total Probability**

$$ P(\text{win}) = P(T < x) \cdot \frac{1}{2} + P(x < T < y) \cdot 1 + P(T > y) \cdot \frac{1}{2} $$

But

$$ P(T < x) + P(T > y) = 1 - P(x < T < y) $$

implies

$$ P(\text{win}) = \frac{1}{2} \cdot (1 + P(x < T < y)) $$

Since $P(x < T < y) > 0$ for any continuous threshold distribution,

$$ P(win) > 0.5 $$

So this strategy **always beats random guessing**.

What about the two player case? Similar to above you and your friend could agree upon a threshold *T* beforehand. Both players will then announce "higher" if your number exceeds *T*, otherwise annouce "lower". We analyze below all the cases,



### Different Thresholds

### Equilibrium Analysis

### Geometric Interpretation

### Connecting the Two Parts

### Intuition and Use in Trading

The random threshold acts like a probe that sometimes lands between the numbers.
Whenever it does, it reveals the correct ordering.

You don’t know the distribution of the numbers — but you don’t need to.

## Key Insight

By introducing your own randomness, you can guess correctly more than 50% of the time, even with no knowledge of the distribution.

## Generalizations
