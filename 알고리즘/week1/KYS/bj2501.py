N, K = input().split()

N = int(N)
K = int(K)

numbers = []

for i in range(1, N+1):
    if N % i == 0:
        numbers.append(i)

if len(numbers) < K:
    answer = 0
else:
    answer = numbers[K-1]
    
print(answer)

