"""A Collection of Common Methods Used to Solve Problems.
"""

from transcription import transcribe
from translation import translate
from rna_splicing import splice

"""
Reads from a file containing DNA strands in FASTA format.

@param infile: the file to read from
@return: A list containing the DNA strands as strings
"""
def read_fasta(infile):
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

    return strands


"""
Calculates the factorial of a number, n.

@param n: the number
@return: the value of n factorial (n!)
"""
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)