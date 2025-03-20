"""
키의 합이 100 이거 조합으로 7개 뽑아서 합쳐서 100이되면 그게 답 아님?
"""
from itertools import combinations
a=[]
for x in range(9):
    a.append(int(input()))
a.sort()
c=[]
for i in combinations(a,7):
    if(sum(i)==100):
        c.append(i)
for x in range(7):
    print(c[0][x])

