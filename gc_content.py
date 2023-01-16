"""Computes GC-Content of Strands of DNA inputted from FASTA format.
"""

with open("in/rosalind_gc.txt", "r") as infile:
    lines = infile.readlines()
    gc = {}
    count = 0
    total = 0
    curr_strand = ""

    for i in range(0, len(lines)):
        if lines[i][0] == ">":
            curr_strand = lines[i][1:len(lines[i]) - 1]
            count = 0
            total = 0
        else:
            for base in lines[i]:
                if base == "G" or base == "C":
                    count += 1
            total += len(lines[i].strip())

            # if last line or next line is a new strand, calculate gc content
            if i + 1 > len(lines) - 1 or lines[i + 1][0] == ">":
                gc[curr_strand] = round(((count / total) * 100000000)) / 1000000


    with open("out.txt", "w") as out:
        out.write(max(gc, key=gc.get))
        out.write("\n")
        out.write(str(max(gc.values())))