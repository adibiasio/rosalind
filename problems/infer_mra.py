"""Inferring mRNA from a Protein Strand.

Problem: https://rosalind.info/problems/mrna/
"""

aa_freq = {
    "F": 2,
    "L": 6,
    "S": 6,
    "Y": 2,
    "X": 3,
    "C": 2,
    "W": 1,
    "P": 4,
    "H": 2,
    "Q": 2,
    "R": 6,
    "I": 3,
    "M": 1,
    "T": 4,
    "N": 2,
    "K": 2,
    "V": 4,
    "A": 4,
    "D": 2,
    "E": 2,
    "G": 4
}

with open("in/rosalind_mrna.txt", "r") as infile:
    protein = infile.readline().strip() + "X"
    prod = 1

    for aa in protein:
        prod *= aa_freq[aa]
        if (prod > 1000000):
            prod %= 1000000

    with open("out.txt", "w") as out:
        out.write(str(prod))
