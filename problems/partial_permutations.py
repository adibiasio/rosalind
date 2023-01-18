"""Calculates the Number of Permutations P(n, r).

Problem: https://rosalind.info/problems/pper/
"""

with open("in/rosalind_pper.txt", "r") as infile:
    param = infile.readline().strip().split()
    n = int(param[0])
    r = int(param[1])
    m = 1000000

    pper = 1
    for i in range(n - r + 1, n + 1):
        pper *= i
        if pper > m:
            pper %= m

    with open("out.txt", "w") as out:
        out.write(str(pper))