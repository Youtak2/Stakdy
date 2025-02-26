N, k = map(int, input().split())
score = list(map(int, input().split()))

def sort(score):
    for i in range(len(score)-1):
        max_index = i

        for j in range(i+1, len(score)):
            if score[max_index] < score[j]:
                max_index = j
        score[i], score[max_index] = score[max_index], score[i]

    return score
result = sort(score)
answer = result[k-1]
print(answer)