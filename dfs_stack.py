with open("input.txt", "r") as file:
    contents = file.read().split()
    v, e = int(contents[0]), int(contents[1])
    if e and "1" in set(contents):
        graph = {}
        V1 = contents[2::2]
        V2 = contents[3::2]
        for v1, v2 in zip(V1, V2):
            if v1 not in graph:
                graph[v1] = set()
            if v2 not in graph:
                graph[v2] = set()
            graph[v1].add(v2)
            graph[v2].add(v1)
        visited = set("1")
        stack = list(graph["1"])
        while len(stack):
            last_element = stack[-1]
            if last_element not in visited:
                visited.add(last_element)
                stack.pop()
                neighbours = graph[last_element]
                for neig in neighbours:
                    if neig not in visited:
                        stack.append(neig)
            else:
                stack.pop()
        ans = sorted(list(map(int, visited)))
    else:
        ans = [1]
    print(len(ans))
    print(*ans)
