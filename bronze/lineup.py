# Just try all the permutations:
# Sort the permutations by alphabetical order
# Check each permutation

from itertools import permutations

fin = open("lineup.in")
fout = open("lineup.out", 'w')

n = int(fin.readline())

reqlist = []
for line in fin.readlines():
    reqlist.append((line.split()[0],line.split()[-1]))

# Get permutations
permutations = sorted(list(permutations(["Bessie", "Buttercup", "Belinda", "Beatrice", "Bella", "Blue","Betsy","Sue"])))

# Check permutations
for perm in permutations:
    for cow in perm:
