"""Mendel's First Law

Problem: https://rosalind.info/problems/iprb/

Calculates probability of an offspring expressing a dominant phenotype,
given the number of homozygous dominant, heterozygous, and homozygous recessive
individuals for the trait in a population. Assumes random mating.
"""

with open("in/rosalind_iprb.txt", "r") as infile:
    # homo. dominant, heterozygous, homo. recessive populations
    counts = infile.readline().split()
    d, t, r = int(counts[0]), int(counts[1]), int(counts[2])
    population = d + t + r

    # Four probable scenarios where offspring may not express dominant phenotype
    # 1) Parent A is heterzygous and Parent B is heterozygous
    # 2) Parent A is heterzygous and Parent B is homo. recessive
    # 3) Parent A is homo. recessive and Parent B is heterozygous
    # 4) Parent A is homo. recessive and Parent B is homo. recessive

    p1 = (t / population) * (((t-1) / (population-1))) * 0.25
    p2 = (t / population) * ((r / (population-1))) * 0.50
    p3 = (r / population) * ((t / (population-1))) * 0.50
    p4 = (r / population) * (((r-1) / (population-1))) * 1

    prob = 1 - (p1 + p2 + p3 + p4)

    with open("out.txt", "w") as out:
        out.write(str(round(prob * 100000) / 100000))
