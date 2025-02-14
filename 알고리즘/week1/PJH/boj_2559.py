N,K = map(int,input().split())
list_a = list(map(int,input().split()))

sum_a = ans = sum(list_a[:K])
for i in range(K,N):
    ans = ans+list_a[i] - list_a[i-K]
    sum_a = max(sum_a,ans)

print(sum_a)