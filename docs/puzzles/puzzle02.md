# First Black Ace

## Problem Statement

Suppose a deck of 52 playing cards is thoroughly shuffled. You are asked to guess in advance the position of the first black ace. This procedure is repeated many times; each time, this deck is thoroughly shuffled, and each time, you guess the position of the first black ace.

What position in the deck should you guess so that if the procedure is repeated many times, you would maximize your chances of guessing correctly the position of the black ace?

## Solution Outline

At first glance, many of us might guess the familiar answer of 53/3 or around 17th-18th position but that would be incorrect. 

There is a subtle point here that is easy to miss; the problem asks for the "most likely" position of the first black ace, not the "expected" position. This is the difference between the **mode** and the **mean** of a distribution.

So how do we determine the mode of the position of the first black ace or in other words, the most likely position.

First we define the distribution.

We can think of the two black aces as being placed uniformly at random among the 52 positions. Let $A_1$, $A_2$ be the positions of the two aces, Define

$$ X = min(A_1, A_2) $$ 

the position of the first black ace. For $X = k$, one ace must be at *k* and the other must be somewhere between $k+1$ and 52. Once one ace is fixed at position *k*, the second ace has $(52 - k)$ possible positions.

What about total ways to choose two positions out of 52 ? 

$$ \binom{52}{2} $$

Therefore,

$$ P(X = k) = \frac{52 - k}{\binom{52}{2}}, \quad k = 1,2,...,51 $$

Now we have the distribution and all the heavy lifting is done. To find the most likely position, we simply need to maximise the probability function defined above. 

We note here that the numerator $(52 - k)$ is strictly decreasing as *k* increases which means $k = 1$ has the largest probability and the probabilities decrease as we move deeper into the deck.

Hence, the mode of distribution is:

$$ k = 1 $$ 

The somewhat surprising answer is that we should guess that the **top card** is the first black ace in the deck!

It's worth pausing here a moment. While we have solved that position 1 is the most likely, some would still argue it is not likely in any absolute sense 

$$ P(X = 1) = \frac{51}{1326} \approx 3.85\% $$

As noted earlier, the distribution is strictly decreasing but very flat; so no single position is a certain "good guess". What we're really solving here is that among 51 positions, position 1 gives you the best odds and in a repeated game, that edge compounds. This is precisely why the mode, not the mean, is the right statistic to optimize when payoff is for an exact match.

By symmetry, it can also be argued that the most likely position for the second black ace (the maximum of $A_1$, $A_2$) is the bottom card of the deck.

### Mode vs Mean

As mentioned earlier, mode is not equal to mean here.

This matters as the expected position answers the question: if we repeat this procedure forever, where does first black ace land on average?

Mathematically,

$$ \mathbb{E}[X] = \sum_{k=1}^{51} k \cdot \frac{52 - k}{\binom{52}{2}} \approx 17.67 $$

So, the math indeed comes full circle. The expected position is around 17th card, confirming the common intuition. But that is not the most likely single position. 

What we're not doing in this problem is maximizing the average outcome. We are maximizing the probability of guessing a single value correctly which means identifying the largest term in the probability mass function.

## Key Insight

The key insight here is recognizing that the problem is asking about the **most likely** position (the mode), not the **expected** position (the mean). Once the distribution of the two black aces is defined correctly and the relationship of probability with *k* established, the answer follows immediately.

The surprise comes from how often we instinctively think in terms of averages, even when the question is not asking for one.
