import math
n = int(input(""))
colors = input("")
colors = sorted(colors.split())
c = 0
pairs_c = 0
pairs_list = []
for lista in range(0,n-1):
    if colors[lista] == colors[lista+1]:
        c += 1
        continue
    pairs_list.append(c)
    c = 0
for lista in range(0,len(pairs_list)-1):
    pairs_c += math.floor((pairs_list[lista]+1)/2)
print(pairs_c)