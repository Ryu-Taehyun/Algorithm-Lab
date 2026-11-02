graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

def dfs(graph, node):
    print(node)

    for neighbor in graph[node]:
        dfs(graph, neighbor)
        
dfs(graph, "A")