"""Transcribes a Strand of RNA from a strand of DNA.

Problem: https://rosalind.info/problems/rna/
"""
def transcribe(dna) -> str:
    rna = ""

    for base in dna:
        if base == "T":
            rna += "U"
        else:
            rna += base
    
    return rna

with open("in/rosalind_rna.txt", "r") as infile:
    dna = infile.readlines()[0].strip()

    with open("out.txt", "w") as out:
        out.write(transcribe(dna))