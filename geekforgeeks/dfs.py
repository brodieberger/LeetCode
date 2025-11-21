graph = [[2, 3, 1], [0], [0, 4], [0], [2]]

def dfs(adj):
    res = []
    visited = len(graph) * [False]
    search_graph(adj, visited, 0, res)
    return res

def search_graph(adj, visited, node, res):
    visited[node] = True
    res.append(node)
    for connection in adj[node]:
        if visited[connection] == False:
            search_graph(adj, visited, connection, res)

print(dfs(graph))