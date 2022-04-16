from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)
    for key in graph:
        graph[key].sort(reverse=True)
    
    result = []
    
    def dfs(u):
        result.append(u)
        if graph[u]:
            v = graph[u].pop()
            dfs(v)
            
    dfs("ICN")
    return result