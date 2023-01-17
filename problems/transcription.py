"""Transcribes a Strand of RNA from a strand of DNA.
"""

with open("in/rosalind_rna.txt", "r") as infile:
    dna = infile.readlines()[0].strip()
    rna = ""

    for base in dna:
        if base == "T":
            rna += "U"
        else:
            rna += base
    
    with open("out.txt", "w") as out:
        out.write(rna)