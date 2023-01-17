""""Calculates Hamming Distance between two Strands of DNA.

Problem: https://rosalind.info/problems/hamm/
"""

with open("in/rosalind_hamm.txt", "r") as infile:
    s1 = infile.readline().strip()
    s2 = infile.readline().strip()
    hamm = 0
    
    for b1, b2 in zip(s1, s2):
        if b1 != b2: hamm += 1
    
    with open("out.txt", "w") as out:
        out.write(str(hamm))