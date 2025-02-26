from collections import deque

def DFS(graph, V, visited):
    visited[V] = 1
    print(V, end=' ')

    for i in sorted(graph[V]):
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, V, visited):
    queue = deque([V])
    visited[V] = 1

    while queue:
        q = queue.popleft()
        print(q, end=' ')

        for i in sorted(graph[q]):
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0]*(N+1)
DFS(graph, V, visited)
print()

visited = [0]*(N+1)
BFS(graph, V, visited)
print()