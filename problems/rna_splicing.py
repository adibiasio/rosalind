"""RNA Splicing.

Removes the specified introns from a strand of dna,
then transcribes and translates the processed strand
into a protein string using algorithms for transcription
and translation written for other rosalind problems.

Problem: https://rosalind.info/problems/splc/
"""

from transcription import transcribe
from translation import translate

def splice(dna, introns) -> str:
    for intron in introns:
        dna = dna.replace(intron, "")

    return dna


with open("in/rosalind_splc.txt", "r") as infile:
    strands = []
    curr_strand = ""

    for line in infile:
        if line[0] == ">":
            strands.append(curr_strand)
            curr_strand = ""
        else:
            curr_strand += line.strip()

    strands.append(curr_strand)
    strands.remove("")

    dna = strands[0]
    introns = strands[1:]
    spliced_dna = splice(dna, introns)
    mRNA = transcribe(spliced_dna)
    protein = translate(mRNA)
    
    with open("out.txt", "w") as out:
        out.write(protein)
    