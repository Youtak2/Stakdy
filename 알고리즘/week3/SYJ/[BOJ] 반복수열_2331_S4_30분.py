# 19:11 ~ 19:41 (30분)

A, P = map(int, input().split())

DP = [A]
idx = 1
next_dp = 0

while True:
    if next_dp in DP[:-1]:
        break
    
    last = DP[idx-1] 
    next_dp = 0
    for i in range(len(str(last))):
        next_dp += (last % 10) ** P
        last //= 10
    idx += 1
    DP.append(next_dp)
    # print(idx)    

for i in range(len(DP)):
    if DP[-1] == DP[i]:
        print(i)
        break