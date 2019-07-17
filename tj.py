from itertools import combinations
#unpack the tuples
(n,p)=input().split()
p = int(p)
ls=[]
comb = combinations(n,len(n)-p)
comb = list(comb)
for i in comb:
    ls.append("".join(i))
print(min(ls))
