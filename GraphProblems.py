

islands = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

def find_num_islands(islands: list[int]):
    def dfs(i, j):
        if (i < 0) or (i >= m) or (j < 0) or (j >= n):
            return
        if islands[i][j] == 0:
            return
        islands[i][j] = 0
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)

    m, n = len(islands),  len(islands[0])
    num_islands = 0

    for i in range(m):
        for j in range(n):
            if islands[i][j] == 1:
                num_islands += 1
                dfs(i, j)


from math import log, floor

root = [1,2,3,4,None,None,None]
# print(root[0:1])
# print(root[0:7])

m, n = 0, 0
solution = []
levels = []
for i in range(0, floor(log(len(root), 2))):
    n += 2 ** i
    levels.append(root[m:n])
    m = n

remainder = root[m:]
levels.append(remainder)
for level in levels:
    for i in range(len(level)-1, -1, -1):
        if level[i] != None:
            solution.append(level[i])
            break

print(solution)


