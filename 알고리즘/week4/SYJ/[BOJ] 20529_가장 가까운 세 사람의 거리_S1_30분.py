# 21:05~ 21:30
import itertools

def compare(A, B):
    global dist
    for i in range(4):
        if A[i] != B[i]:
            dist += 1
    return

T = int(input())
for tc in range(T):
    N = int(input())
    mbti = list(input().split())

    if N >32:
        min_dist = 0    
    else:
        combs = list(itertools.combinations(mbti,3))
    
        min_dist = 999
        for comb in combs:
            dist = 0
            compare(comb[0],comb[1])
            compare(comb[1],comb[2])
            compare(comb[2],comb[0])
            min_dist = min(dist, min_dist)

    print(min_dist)


