"""Enumerating Gene Orders.

Generates all possible permutations of the numbers 1 through n.
"""

from independent_alleles import factorial

def permute(arr, l, r, out):    
    if l == r:
        out.write("\n" + " ".join(arr))
    for i in range(l, r):
        arr[l], arr[i] = arr[i], arr[l]
        permute(arr, l + 1, r, out)
        arr[i], arr[l] = arr[l], arr[i]

with open("in/rosalind_perm.txt", "r") as infile:
    n = int(infile.readline().split()[0])
    arr = list()

    for i in range(1, n + 1):
        arr.append(str(i))
    
    with open("out.txt", "w") as out:
        out.write(str(factorial(n)))
        permute(arr, 0, n, out)
