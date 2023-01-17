"""Mendel's Second Law

Problem: https://rosalind.info/problems/lia/

Calculates probability that there are at least n AaBb offspring in the kth 
generation of mating with AaBb organisms, where the 0th generation consisted 
of one AaBb organism.

This problem relies on the fact that regardless what genotype is crossed with 
the AaBb parent, the probability of producing an AaBb offspring is always 25%.
This means we don't need to consider which offspring were produced in earlier 
generations, as this is irrelevant. We only need to consider which offspring are
produced in the kth generation (to determine if they are AaBb).

Thus, we can define the production of an AaBb offspring as a success and set up
a Bernoulli trial with p = 0.25 and q = 0.75. In the bernoulli trial equation,
n represents the number of independent trials (in this case, the number of 
independent reproductions at the final generation = 2^k (the parameter)) and 
k represents the desired number of successes (the number of AaBb offspring = N).

To determine the probability of there being at least N AaBb offspring, we can 
sum the probabilities of all possible numbers of AaBb offspring: N <= x <= 2^k.
"""

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

with open("in/rosalind_lia.txt", "r") as infile:
    nums = infile.readline().split()
    k, n = int(nums[0]), int(nums[1])
    prob = 0

    for i in range(n, 2**k + 1):
        prob += (factorial(2**k)/(factorial(2**k - i) * factorial(i))) * (0.25)**(i) * (0.75)**(2**k - i)

    with open("out.txt", "w") as out:
        out.write(str(round(prob * 1000) / 1000))