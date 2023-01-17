"""Counting Nucleotides in a Strand of DNA.
"""

with open('in/rosalind_dna.txt', 'r') as infile:
    dna = infile.readlines()[0].strip()
    nucleotides = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }

    for base in dna:
        nucleotides[base] += 1
    
    counts = ""

    for base in nucleotides:
        counts += str(nucleotides[base]) + ("" if base == "T" else " ")

    with open("out.txt", "w") as out:
        out.write(counts)