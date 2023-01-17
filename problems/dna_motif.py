"""Finding a Motif in DNA.

Problem: https://rosalind.info/problems/subs/
"""

with open("in/rosalind_subs.txt", "r") as infile:
    s = infile.readline().strip()
    t = infile.readline().strip()
    pos = list()

    for i in range(len(s) - len(t)):
        if s[i] == t[0]:
            start = i + 1
            for j in range(len(t)):
                if s[i] != t[j]:
                    i += 1
                    j -= 1
                    break
                i += 1
            if j == len(t) - 1:
                pos.append(start)
    
    with open("out.txt", "w") as out:
        out.write(" ".join(str(x) for x in pos))