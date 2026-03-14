# Choosing the Largest Offer
**Difficulty:** ⭐⭐⭐  
**Topics:** Probability, Optimal Stopping

*Tags: Optimal Stopping, Secretary Problem, Decision Theory, Exploration vs Exploitation*

---

## Problem Statement

In the final round of interviews at a top prop shop, the hiring manager decides to test whether you are truly as smart as your resume suggests. Instead of asking another technical question, they offer you a peculiar challenge.

One hundred slips of paper are placed in a box, each containing a **different offer amount** and thoroughly mixed. A slip is drawn at random and you must decide whether that is the **largest offer** among all 100 or not. 

* If you decide it is and are correct, you get the offer.
* If you decide it is and are wrong, you get nothing.
* If you decide against it, you must choose or refuse the next slip, and so on until you choose one or slips are exhausted. 

You cannot go back to previously rejected slips.

How should you play this game to maximize your probability of securing the job with the largest offer?  

---

## Solution Outline

Placed in this situation, many applicants might question the hiring manager's cruelty. After all, the question arises whether or not your chances are much larger than $1/n$ $(n = 100)$. Yet only the few best applicants have any idea that the size of the probability of winning is **significantly larger**.

Perhaps mathematics can come to our aid. 

One important observation is that the applicant is given **no prior information** about the distribution of the offers. Therefore, the only meaningful comparison is relative to the offers seen so far. 

During the process of drawing the slips, only a slip that has the largest offer thus far is worth considering; lets call this slip a *candidate.*

### The Strategy

I suggest now that the optimal strategy is simply:

* Pass/reject the first *r* slips outright.
* Choose the candidate thereafter (first slip larger than all previous). 

Intuitively, first phase acts as **sampling period**, allowing us to estimate how large the offers might be. After this phase, we should accept the first offer that beats everything we have seen.

### When to Stop?

Obviously, we would choose a candidate at draw *i* if its probability of winning exceeds the probability of winning with the **best** strategy at a later time; formally,

$$ P(i) > P(i+1 \quad onward) $$

We can show that:

* Probability of winning if **we stop now** increases with *i*
* Probability of winning if **we continue** decreases with *i* 

Therefore a state of draw occurs at which it is preferable to keep a candidate rather than to go on.

### Computing Probability of Success

The value of continuing must strictly decrease as *i* increases as the more slips we've seen, the fewer remain, so passing on a candidate becomes costlier.

We noted before that we only stop when we see the largest so far. Hence, the probability that it is the true maximum of the sample is *i/n* (max being in the first *i* draws), which strictly increases with *i* from 1/n to 1. This is our probability of winning with draw *i*.

Somewhere along the line our left hand probability will exceed our right hand probability. Then we can define the optimum strategy by the rule expressed earlier: let the first *r* go by and choose the first candidate thereafter.

We only win only if two events occur for some $r < k \leq n$:

* **Event A:** The largest offer occurs at $k > r$
* **Event B:** The maximum among first $k - 1$ occurs within first *r* slips

Otherwise we would have stopped earlier (between *r* and *k*).

Now the probability max occurs at *k* is (assuming uniform distribution of offers):

$$ P(A) = \frac{1}{n}$$

and the probability maximum of first $k - 1$ appears in the first *r* positions is

$$ P(B) = \frac{r}{k - 1} $$

Thus the probability of winning with threshold *r* is,

$$ P(r) = \sum P(A) \cdot P(B) = \sum_{k=r+1}^{n} \frac{1}{n} \cdot \frac{r}{k - 1} $$

### Approximating for Large *n*

For large n, we can approximate the harmonic sum as:

$$ \sum_{k=r+1}^{n} \frac{1}{k - 1} \approx \ln(\frac{n}{r}) $$

This gives

$$ P(r) \approx \frac{r}{n} \ln(\frac{n}{r}) $$

To maximize, we differentiate:

$$ \frac{1}{n} ( \ln(\frac{n}{r}) - 1 ) $$

Setting to zero yields:

$$ \ln(\frac{1}{n}) = 1, \quad r = \frac{n}{e} $$

### The Optimal Strategy

For $n = 100$,

$$ r \approx \frac{100}{e} \approx 37 $$

So the optimal strategy is:

* Reject the first 37 slips, no matter what.
* The select the first candidate thereafter.

This strategy succeeds with probability approximately

$$ P(r) \approx \frac{1}{e} \approx 36.8\% $$

This is quite remarkable. What initially looks like a hopeless *1/100* can be improved to **over 1/3** using nothing more than a clever stopping rule.

Perhaps that prop shop offer isn't out of reach after all.

---

## Key Insight

The key insight is recognizing that you should **separate exploration from exploitation**. 

We initially observe enough samples to understand scale of the offers. We then finally commit to the first offer that beats everything seen so far.

Mathematically, the optimal threshold for observation occurs at roughly *n/e* samples, which yield the famous *1/e* success probability.

What looks like a cruel puzzle from a hiring manager is actually one of the most elegant stopping problems in probability.
