from collections import defaultdict


def dfs(graph, visited, now, ans):
    visited[now] = True
    for neig in graph[now]:
        if not visited[neig]:
            ans += [neig]
            dfs(graph, visited, neig, ans)


with open("input.txt", "r") as file:
    contents = list(map(int, file.read().split()))
    V, E = contents[0], [1]
    graph = defaultdict(list)
    ans = list()
    V1 = contents[2::2]
    V2 = contents[3::2]
    for v1, v2 in zip(V1, V2):
        graph[v1].append(v2)
        graph[v2].append(v1)
    visited = dict(zip(graph.keys(), [False] * V))
    dfs(graph, visited, 1, ans)
    ans += [1]
    ans.sort()
    print(len(ans))
    print(*ans)
