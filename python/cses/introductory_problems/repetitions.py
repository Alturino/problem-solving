dna = input()
res = 1
curr = 1
for i in range(len(dna) - 1):
    if dna[i] == dna[i + 1]:
        curr += 1
        res = max(curr, res)
    else:
        curr = 1
        res = max(curr, res)
print(res)
