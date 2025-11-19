class Solution:
    def dfs(self, adj):
        # Printing adj returns [[2, 3, 1], [0], [0, 4], [0], [2]]
        visited = [False] * len(adj)
        res = []
        self.dfsRec(adj, visited, 0, res)
        return res
        
    def dfsRec(self, adj, visited, s, res):
        visited[s] = True
        res.append(s)
    
        for i in adj[s]:
            if not visited[i]:
                self.dfsRec(adj, visited, i, res)

solution = Solution()

myGraph = [[2, 3, 1], [0], [0, 4], [0], [2]] # Expected output 0 2 4 3 1
res = solution.dfs(myGraph)
print(res)