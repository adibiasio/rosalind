"""Calculating Population Size as a function of time.

Problem: https://rosalind.info/problems/fib/
"""

def population(n, k):
    return populationHelper(1, 1, k, 3, n)

def populationHelper(f1, f2, k, m, n):
    if n == 1 or n == 2: return 1
    fn = f2*k + f1

    if m < n:
        return populationHelper(fn, f1, k, m + 1, n)
    else:
        return fn

with open("in/rosalind_fib.txt", "r") as infile:
    param = infile.readline().split()
    n = int(param[0])
    k = int(param[1])

    with open("out.txt", "w") as out:
        out.write(str(population(n, k)))

