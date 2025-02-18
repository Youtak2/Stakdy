T = int(input())
for tc in range(T):
    N, K = map(int, input().split())

    scores = []
    for i in range(N):
        a, b, c = map(int, input().split())
        score = a*0.35 + b*0.45+ c*0.2
        scores.append(score)

        if i == K-1:
            K_score = score
    
    scores.sort(reverse=True)
    idx = scores.index(K_score)
    
    order = idx/N * 100
    
    if order < 10: grade = 'A+'
    elif order < 20 : grade = 'A0'
    elif order < 30 : grade = 'A-'
    elif order < 40 : grade = 'B+'
    elif order < 50 : grade = 'B0'
    elif order < 60 : grade = 'B-'
    elif order < 70 : grade = 'C+'
    elif order < 80 : grade = 'C0'
    elif order < 90 : grade = 'C-'
    else: grade = 'D0'

    print(f'#{tc+1}', grade)