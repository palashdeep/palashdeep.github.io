# Penney's Game

## Problem Statement

Two players A and B, each choose a sequence of three outcomes of a fair coin toss (for example HHT, TTH, etc.).

The coin is then tossed repeatedly, producing a sequence of heads (H) and tails (T). As soon as one player's chosen sequence appears as three consecutive outcomes, that player wins.

Player A chooses a sequence first. Player B then chooses a different seqeunce.

Answer the following:

1. Does Player B have a strategy that gives them a probability of winning greater than *1/2*?

2. For a given choice by Player A, what sequence should Player B choose to maximize their chance of winning?

3. Explain why the advantage occurs.

## Solution Outline

This is a problem which is at times misunderstood to be extremely trivial but the result is quite unexpected which makes it one of the most beautiful insights out there. Lets start with a small example.

### Simulation Intuition

Lets assume Player A picks the sequence **HHT** and in response Player B picks the sequence **THH**. We start flipping the coin repeatedly and the first pattern to appear wins the game. Lets calculate the probability that B wins.

We will solve it using a state analysis. Lets define,

* $P(X)$ is the probability X wins (A or B) the game
* $P_{seq of H, T}(X)$ is the probability that X wins after the sequence has occured

Now conditioning on first toss,

$$ P(B) = \frac{1}{2} P_H(B) + \frac{1}{2} P_T(B) $$

We can further condition this on the second toss

$$ P_H(B) = \frac{1}{2} P_{HH}(B) + \frac{1}{2} P_{HT}(B) $$

We can see that once we have *HH* it is impossible for B to win as the next *T* wins A and any next *H* just keeps the suffix as *HH*. Hence, 

$$P_{HH}(B) = 0$$

and

$$ P_{HT}(B) =  \frac{1}{2} P_{HTH}(B) + \frac{1}{2} P_{HTT}(B) $$

But *HTT* is simple just *T* as that's what matters. For sequence *HTH*, the next *H* wins B and the next *T* is again just simply *T*. So,

$$ P_{HTH}(B) = \frac{1}{2} \cdot 1 + \frac{1}{2} P_{T}(B) $$

Substituting,

$$ P_{HT}(B) =  \frac{1}{4} + \frac{3}{4} P_{T}(B) $$

Lets now condition on first toss being *T*,

$$ P_T(B) = \frac{1}{2} P_{TH}(B) + \frac{1}{2} P_{T}(B) $$

where *TT* is same as just *T* and *TH* can be further conditioned as,

$$ P_{TH}(B) =  \frac{1}{2} \cdot 1 + \frac{1}{2} P_{T}(B) $$

Substituting,

$$ P_T(B) = \frac{1}{4} + \frac{3}{4} P_{T}(B) $$

implies

$$ P_T(B) = 1 $$

and

$$ P_{HT}(B) = 1, \quad P_H(B) = \frac{1}{2} $$

Finally we get,

$$ P(B) = \frac{1}{2} \cdot \frac{1}{2} + \frac{1}{2} \cdot 1  = \frac{3}{4} $$

We note here that B wins with probability *3/4*, a massive advantage, which is quite surprising when both the patterns have equal length and the coin is fair. Naive intuition suggests that both the sequences have probability *1/8* of appearing in three tosses, hence, both the players should have equal chance of winning. A quick simulation on 1000 paths also returns the probability B wins to be **about 0.75** which confirms our result from solving.

Lets understand why this asymmetry appears.

### Why Naive Symmetry Fails

The naive symmetry fails here because the suffix patterns overlap differently with future flips. For example, as we saw, if the sequence currently ends in *HH*, it is impossible for B to win but A wins in all the cases. Similarly once we get a *T*, B's win is guaranteed no matter what. 

Thus it comes down to some partial histories/suffixes favouring one pattern more than the other.

The probabilities of those partial histories appearing breaks the "assumed" symmetry.

### Optimal Response Rule

We introduce here an elegant trick to guarantee higher odds for Player B, for any pattern Player A may choose.

Let Player A choose the pattern:

```
a b c
```

then Player B can choose:

```
(not b) a b
```

which will always have higher probability of win for Player B. B's pattern is constructed in such a way that **whenever A is about to complete their pattern B is already closer**.

### Expected Waiting Times

Lets calculate the expected waiting time for different patterns.
We will compare waiting times for *HHH* and *HTH* patterns. We can use the state-analysis approach similar to what we used in the first section but with expectations this time.

For *HHH*:

$$ E = \frac{1}{2} (1 + E_H) + \frac{1}{2} (1 + E_T) $$

Anytime we toss a *T* the pattern resets, hence,

$$ E_T = E, \quad E_{HT} = E, \quad E_{HHT} = E $$

Now,

$$ E_H = \frac{1}{2} (1 + E_{HH}) + \frac{1}{2} (1 + E_{HT}) $$

and

$$ E_{HH} = \frac{1}{2} (1 + E_{HHH}) + \frac{1}{2} (1 + E_{HHT}) $$

Here $E_{HHH} = 0$, since we have reached the required pattern. Solving the above system of equations, we get,

$$ E_{HH} = 8, \quad E_H = 12, \quad E = 14 $$

which means the expected waiting time to see *HHH* is 14 tosses. Similarly, we can solve the same for *HTH* which comes out to be 10 tosses. This is left as an exercise for the reader.

This tends to be a very surprising result for a lot of individuals. But the reason behind it is very simple. Pattern overlap with itself changes how often partial matches occur.

Patterns like *HHH* reset every time we see a *T* whereas patterns like *HTH* reuse partial matches. For example, if we get *THT* at some point, the pattern doesn't reset completely, we still only need an *H* to get to our pattern.

Any programming enthusiasts would identify the conceptual similarities of this problem to the **Knuth-Morris-Pratt** algorithm used to construct Longest Prefix Suffix array. How it makes pattern matching faster is by not resetting completely everytime a mismatch occurs but finding partial overlaps with the already matched pattern.

### Markov Chain

The approach that we used in the previous section and the first section to calculate the probabilities and expectations is famously called the Markov Chain approach.

Each state in the chain of events represents how much of the pattern we have matched. The process evolves as a Markov Chain where we make decisions on which state is favourable to the outcome we desire and which isn't. Transitions to the next state depend on the next coin flip. Eventually one pattern reaches it's absorbing state.

### Non-Transitive Cycle

The most surprising aspect of this game is that **there is no universally best pattern**. Instead, the patterns form a **cycle of advantages**, similar to rock-paper-scissors.

For example:

```
HHT loses to THH  
THH loses to TTH  
TTH loses to HTT  
HTT loses to HHT
```

In each case, the second pattern has **more than 50% probability** of appearing first, which seems quite paradoxical. As if A > B and C > A, shouldn't C > B ? Surprisingly, this reasoning fails as transivity is not preserved in this problem.

The advantage actually depends on how **partial matches interact during repeated flips**. The idea is that the game doesn't always starts/resets every flip. Instead we have residual matches for patterns at each stage. These can either help or hurt different patterns depending on how they interact with themselves and each other.

We can make use of the asymmetry between different patterns to deliberately choose patterns that reuse the partial structure of the pattern chosen by our opponent. Each advantage comes from **exploiting the overlap structure** of the opponent's pattern but the new pattern can itself be exploited by yet another pattern.

In other words, any advantage in this game is **relative**, not absolute which means there is no world in which A can have higher probability of winning by choosing the pattern first.

### Connection to Deeper Context

The idea we discussed appears in real life applications like:

* **N-length patterns**: Similar to what we discussed in the previous section, we can do pattern constructions for n-length sequences to produce optimal counter strategies. 

* **DNA sequence assembly**: Finding overlaps between DNA fragments. We can think of DNA being a chain of repeated tosses with each toss having four possible outcomes.

* **Algorithmic String Matching**: Briefly dicussed above similarities with KMP algorithm.

* **Stochastic Process Waiting Times**: We can calculate waiting times for various stochastic processes using the theory discussed in this problem.

## Key Insight

The surprising feature of Penney's game is that randomness doesn't always imply symmetry contradicting popular belief. In sequential probability problems, **partial information about the past can break symmetry in unexpected ways**. The structure of patterns, specifically how they overlap with future outcomes, determines the advantage.

The existence of a cycle reveals that even in a fair coin process, **structure in the patterns can create systematic advantages**.

This is what makes Penney's game such a beautifule example of non-intuitive behavior in probability.
