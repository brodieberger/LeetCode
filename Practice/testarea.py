grid = [
    ["1","0","0","0","1"],
    ["2","0","0","0","0"],
    ["3","0","0","0","0"],
    ["1","0","0","0","1"]
  ]

print(grid)

print(" ")

visited = [[False] * len(grid[0]) for _ in range(len(grid))]
visited[0][0] = True
for element in visited:
    print(element) 

print(grid[0][-1])


hey = [0,1,2,3,4]

print(hey[-1])