# 20:45~

# 부분집합 함수 정의
def subset_comb(cnt, idx):
    result.append(sum(ans))
    if cnt == len(num):
        return
    for i in range(idx,len(num)):
        ans.append(num[i])
        subset_comb(cnt+1,i+1)
        ans.pop()

# input
n, s = map(int, input().split())
num = list(map(int, input().split()))

ans = []    # 부분집합
result = [] # 부분집합의 합의 집합
cnt0 = 0    # 결과 값

# 부분집합의 합이 's'와 같은 경우 count
subset_comb(0,0)
for i in result:
    if i == s:
        cnt0 += 1

# 부분집합의 크기가 양수라고 했기 때문에 공집합(:원소합=0) 제외
if s == 0:
    cnt0 -= 1
print(cnt0)