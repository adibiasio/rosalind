"""Translates a Strand of mRNA into a Protein Sequence.

Problem: https://rosalind.info/problems/prot/
"""

# X represents a 'Stop' codon
codon_table = {
    "UUU": "F",
    "UUC": "F",
    "UUA": "L",
    "UUG": "L",
    "UCU": "S",
    "UCC": "S",
    "UCA": "S",
    "UCG": "S",
    "UAU": "Y",
    "UAC": "Y",
    "UAA": "X",
    "UAG": "X",
    "UGU": "C",
    "UGC": "C",
    "UGA": "X",
    "UGG": "W",

    "CUU": "L",
    "CUC": "L",
    "CUA": "L",
    "CUG": "L",
    "CCU": "P",
    "CCC": "P",
    "CCA": "P",
    "CCG": "P",
    "CAU": "H",
    "CAC": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGU": "R",
    "CGC": "R",
    "CGA": "R",
    "CGG": "R",

    "AUU": "I",
    "AUC": "I",
    "AUA": "I",
    "AUG": "M",
    "ACU": "T",
    "ACC": "T",
    "ACA": "T",
    "ACG": "T",
    "AAU": "N",
    "AAC": "N",
    "AAA": "K",
    "AAG": "K",
    "AGU": "S",
    "AGC": "S",
    "AGA": "R",
    "AGG": "R",

    "GUU": "V",
    "GUC": "V",
    "GUA": "V",
    "GUG": "V",
    "GCU": "A",
    "GCC": "A",
    "GCA": "A",
    "GCG": "A",
    "GAU": "D",
    "GAC": "D",
    "GAA": "E",
    "GAG": "E",
    "GGU": "G",
    "GGC": "G",
    "GGA": "G",
    "GGG": "G"
}

def translate(rna) -> str:
    protein = ""

    for i in range(0, len(rna) - 3, 3):
        if codon_table[rna[i:i + 3]] == "X": break
        protein += codon_table[rna[i:i + 3]]
    
    return protein

with open("in/rosalind_prot.txt", "r") as infile:
    rna = infile.readlines()[0].strip()

    with open("out.txt", "w") as out:
        out.write(translate(rna))