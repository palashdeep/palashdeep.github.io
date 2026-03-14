# A Card Game
**Difficulty:** ⭐⭐⭐⭐  
**Topics:** Optimal Stopping, Martingales

*Tags: Optimal Stopping, Dynamic Programming, Martingales, Random Walk, Optional Stopping Theorem*

---

## Problem Statement

You have 52 playing cards (26 red, 26 black). You draw cards one by one. A red card pays you a dollar. A black one fines you a dollar. You can stop anytime you want. Cards are not returned to the deck after being drawn. What is the optimal stopping rule in terms of maximizing expected payoff? Also, what is the expected payoff following this optimal rule?

---

## Solution Outline

Starting off, one thing seems clear, you cannot be better or worse off at the end of the game than you are at the start if you draw all the 52 cards. Which means the worst you can guarantee is **zero payoff**. Can we do better by stopping earlier?

### Dynamic Programming Formulation

Let *R* and *B* denote the total number of red and black cards at the start of the game. Let *r* and *b* denote the number of red and black cards still to be drawn at some intermediate stage of the game. Since you are paid $+1$ for every red card drawn and $-1$ for every black card, your current accumulated score is $(R - r) - (B - b)$. Let the **optimal expected value** of the cards yet to be drawn be $E(r, b)$, so the total value of the game at any stage can be denoted by,

$$ V(r, b) = (R - r) - (B - b) + E(r, b) $$

Now, the important part remains to define what $E(r, b)$ looks like. We can recursively define it as follows,

$$ E(r, b) = \begin{cases} 
0, & \text{if } r = 0 \\
r, & \text{if } b = 0 \\
\max \left\{ 0, \frac{r}{r+b} [1 + E(r-1, b)] + \frac{b}{r+b} [-1 + E(r, b-1)] \right\}, & \text{otherwise.} 
\end{cases} $$

Let's go through each case, if $r = 0$, this means there is no upside left in continuing and hence, one should halt now. If $b = 0$, this implies all remaining cards are red, so you should draw them all. For any other case the expected value is solved recursively as given.

The above equation can be solved programmatically using dynamic programming, which also constructs the $E(r, b)$ matrix. We present the $E(r, b)$ matrix for the 8 cards case as output of the python script. Similar analysis can be done for the 26 cards case,

```
E(r,b) table for 4 red, 4 black:

|     |   b=0 |   b=1 |   b=2 |   b=3 |   b=4 |
|:----|------:|------:|------:|------:|------:|
| r=0 |     0 |  0    |  0    |  0    |  0    |
| r=1 |     1 |  0.5  |  0    |  0    |  0    |
| r=2 |     2 |  1.33 |  0.67 |  0.2  |  0    |
| r=3 |     3 |  2.25 |  1.5  |  0.85 |  0.34 |
| r=4 |     4 |  3.2  |  2.4  |  1.66 |  1    |
```

```
E(26,26) = 2.6245
```

If the expected value of the remaining deck is positive, you should continue playing and if it's negative, you should stop. Note that you won't see negative values in your matrix as they are floored at zero, which doesn't mean you are indifferent about continuing. In fact, in each case you should quit immediately and even for the one where the expectation is actually zero, a risk-averse player would quit.

When playing optimally, the last card drawn is always red. That is, you never pick a black card and then quit. As discussed earlier, the optimal score cannot be negative as you can always get zero payoff by drawing every card. Thus, optimal score is a non-increasing step function of the number of black cards drawn (drawing red cards has no effect on the optimal score to quit).

### Discussion: Optimal Stopping Rule

The decision to stop only depends on **future expectation** as seen earlier. The **current accumulated payoff is irrelevant** as stopping just locks in what you have. If you stop now, the future value becomes zero.

Let's define the **continuation value**,

$$ C(r,b) = \frac{r}{r+b} [1 + E(r-1, b)] + \frac{b}{r+b} [-1 + E(r, b-1)] $$

and

$$ E(r,b) = \max (0, C(r, b)) $$

We also note that the recursive relation of $C(r, b)$ is the **Bellman equation** for the optimal stopping problem with boundary at $V(0,b) = 0$.

As discussed before, we stop whenever the continuation value $\leq 0$ which means stopping rule becomes **a boundary in the $(r, b)$ plane**. Thus the optimal strategy is:

* **continue if** $C(r, b) > 0$
* **stop if** $C(r, b) \leq 0$

Now $V(r, b) = 0$ creates a **nonlinear free-boundary problem** which does not yield a closed analytic expression.

The recursion can be solved efficiently using dynamic programming. For the full deck,

$$ E(26, 26) \approx 2.62 $$

Thus optimal play yields an expected profit of about **$2.62**.

### The Game as a Random Walk

How do you estimate an upper bound for this without actually solving the complete problem?

You start at zero. At each step either you gain $1 or lose $1. Let

$$ S_n = \text{cumulative profit after n draws} $$

This is a **random walk** but with probabilities changing over time.

$$ P(+1) = \frac{r}{r+b}, \quad P(-1) = \frac{b}{r+b} $$

The expected value of the walk is always,

$$ E[S_n] = 0 $$

as the deck has equal reds and blacks. So $S_n$ is a **martingale**. More precisely, $S_{t \wedge \tau}$ is a stopped martingale, and since $\tau \leq 52$ is a bounded stopping time, the optional stopping theorem guarantees $E[S_{\tau}] = 0$, the expected profit at the stopping point is zero, and all profit comes purely from the timing optionality.

But the expected profit is positive as we are allowed to **stop at any time**. Our payoff is therefore,

$$ \max_{t \leq 52} S_t $$

and profit,

$$ E[\max S_t] > 0 $$

because taking $max$ breaks the martingale symmetry. We appeal to Doob's $L^2$ maximal inequality for a martingale process which gives

$$ E\left[\max_t S_t^2\right] \leq 4E[S_n^2] $$

Taking square roots and using Jensen's inequality,

$$ E\left[\max_t S_t\right] \leq 2\sqrt{E[S_n^2]} = 2\sqrt{Var(S_n)} $$

Since $Var(S_n) \approx n$ for a symmetric random walk, this gives

$$ E[\max S_t] \leq 2\sqrt{52} \approx 14.4 $$

This bound is loose but serves to show the expected payoff is **finite and sublinear in deck size**. We tighten this bound later on.

Note that while $S_{52} = 0$ in our case, due to the balanced deck, the variance approximation used applies to the *path* of the walk, not its fixed endpoint. We are borrowing this from the unconstrained symmetric random walk, where increments have unit variance. The finite-deck constraint will ultimately force the walk back to zero, which is precisely why the actual value of ~2.6 falls well below this upper bound.

### Large Deck Approximation

We also note a really nice asymptotic insight here. 

For large decks, an asymptotic approximation gives a tighter bound and reveals the geometric structure of the problem. The process behaves like **Brownian motion**. Let $d = r - b$ be the red advantage. The remaining deck size is

$$ n = r + b $$

The variance of the remaining walk is roughly of the order of *n*. Optimal stopping theory shows the stopping boundary approximately satisfies

$$ d \approx c \sqrt{n} $$

where *c* can be numerically estimated from the DP solution to be a constant of order 1. This means you should continue only if your red advantage exceeds roughly $\sqrt{n}$, i.e. the remaining volatility of the walk.

Under the Brownian motion approximation, $S_t$ converges to a scaled Brownian motion $B_t$. For a standard Brownian motion, the reflection principle gives

$$ E[|B_n|] = \sqrt{\frac{2n}{\pi}} $$

and since the running maximum of a Brownian motion satisfies

$$ E[\max_{t \leq n} B_t] = E[|B_n|] $$

By symmetry and reflection, we get:

$$ E\left[\max_t S_t\right] \approx \sqrt{\frac{2n}{\pi}} \approx 5.75 $$

This is a tighter upper bound than the Doob bound, though still above the true value ~2.6. The gap can be explained by two compounding effects: first, the finite-deck constraint forces $S_{52} = 0$, which penalizes the running maximum relative to the unconstrained case; second, the changing draw probabilities as the deck depletes mean the walk loses volatility toward the end, further constraining the maximum. The true value is roughly half the BM bound, which is consistent with these constraints absorbing half the optionality. 

Thus we obtain the rough bounds,

$$ E[\max S_t] < \sqrt{\frac{2n}{\pi}} < \sqrt{n} $$

### You are Holding an American Option

The optimal stopping structure discussed has a well-known financial analogue. The problem is essentially a **finite American option on a biased random walk with changing probabilities**.

At any time you can **exercise and lock in your profit**. Your payoff therefore, as defined before, is

$$ \max_{t \leq n} S_t $$

This is exactly the payoff of an American option:

* underlying: random walk $S_t$
* exercise value: current value $S_t$
* maturity: $n$

If the walk rises past the optimal threshold, you exercise; otherwise you continue holding the option.

---

## Key Insight

Even in a perfectly fair game, the ability to stop early creates value. The player is effectively holding a small **American option on the path of a random walk**, and this optionality alone generates about **$2.6 of expected profit**. 