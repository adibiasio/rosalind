"""Generates the Reverse Complement of a Strand of DNA.

Problem: https://rosalind.info/problems/revc/
"""

base_pairing = {
    "A": "T",
    "T": "A",
    "C": "G",
    "G": "C"
}

with open("in/rosalind_revc.txt", "r") as infile:
    dna = infile.readlines()[0].strip()
    complement = ""

    for i in range(len(dna) - 1, -1, -1):
        complement += base_pairing[dna[i]]
    
    with open("out.txt", "w") as out:
        out.write(complement)