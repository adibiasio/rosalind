"""Mortal Fibonacci Rabbits.

Problem: https://rosalind.info/problems/fibd/
"""

def population(n, m):
    if n == 1: return 1
    if m == 1: return 0
    elif m == 2: return 1

    months = [1, 1]
    i = 2

    while i < m:
        months.append(months[i - 1] + months[i - 2])
        i += 1

    if i == m:
        months.append(months[i - 1] + months[i - 2] - months[i - m])
        i += 1

    while i < n:
        months.append(months[i - 1] + months[i - 2] - months[i - m - 1])
        i += 1

    return months[n - 1]

with open("in/rosalind_fibd.txt", "r") as infile:
    param = infile.readline().split()
    n = int(param[0])
    m = int(param[1])

    with open("out.txt", "w") as out:
        out.write(str(population(n, m)))
