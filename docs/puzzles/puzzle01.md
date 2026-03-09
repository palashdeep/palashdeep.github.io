# Subset of Subsets

## Problem Statement

Prove that every set of ten distinct numbers between 1 and 100 contains two disjoint nonempty subsets with the same sum.

## Solution Outline

At first glance this problem doesn't seem to make much sense (at least it didn't to me). You are not given any specific structure for the sets or subsets - just the numbers 1, 100, and 10. That strongly suggests the solution must rely on these values alone. 

The trick here is to realize that this problem has nothing to do with explicitly finding subsets, computing sums or applying complicated mathematics. Instead, it is a beautiful application of the Pigeonhole principle. If that makes sense now, go back and solve this yourself.

If you weren't able to complete it or are here to check your reasoning - let's walk through it.

The trick is to ignore the disjointness of the subsets temporarily. We will return to it later.

For every set of 10 distinct numbers (or any kind of items for that matter) the number of distinct nonempty subsets is: 

$$ 2^{10} - 1 = 1023 $$ 

which means there are 1023 sums. But can all of these be distinct? 

If we can prove that the total number of possible subset sums is less than 1023 our work here is done. 

Now lets find the bounds for the possible sums.

* The minimum sum would obviously be at least 1 
* But what about the maximum? The largest sum occurs when we choose the 10 largest distinct numbers between 1 and 100:

$$ 100 + 99 + 98 + ... + 91 = 955. $$

So every subset sum must lie between 1 and 955 which gives at most 955 possible values. 

But we have 1023 nonempty subsets.

Since 1023 > 955, there must be at least two distinct subsets with the same sum. This follows directly from the Pigeonhole Principle.

Now we address the disjointness condition.

The two subsets found may not be disjoint. But since all numbers in our set are positive, no proper subset can have the same sum as a larger one. Therefore, neither A nor B can contain the other, which means A\B and B\A are nonempty. Hence, we can just throw out their common elements; remainders are disjoint and still have the same sum.

## Key Insight

The key insight is recognizing that this is purely a counting problem. It is not about computing clever subset sums or constructing special examples. Once you see that the number of subsets exceeds the number of possible sums, the conclusion follows immediately from the Pigeonhole Principle.

That shift in perspective is what makes the problem elegant.