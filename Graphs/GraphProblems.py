from pprint import pprint
from collections import deque

# undirected graph
edge_list1 = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n'],
    ['i', 'l'],
    ['j', 'l']
]
graph2 = {
    5: [0, 8],
    1: [0],
    0: [1, 5, 8],
    8: [0, 5],
    4: [2, 3],
    2: [4, 3],
    3: [4, 2]
}
graph3 = {
    'A': ['B', 'C'],
    'B': [],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
graph4 = {
    'Z': ['Y', 'V'],
    'Y': ['Z'],
    'X': ['Y'],
    'W': ['X', 'V'],
    'V': ['Z'],
}

# to directed graph
def to_adj_list(edge_list: list[list[str]]) -> dict[str, list[str]]:
    '''
    Converts an edge list for an undirected graph to an adjacency list map 
    Also converts undirected edges to double sided edges
    '''
    adjacency_list = {}
    for relationship in edge_list:
        if relationship[0] in adjacency_list.keys():
            adjacency_list[relationship[0]].append(relationship[1])
        else:
            adjacency_list[relationship[0]] = [relationship[1]]
        
        if relationship[1] in adjacency_list.keys():
            adjacency_list[relationship[1]].append(relationship[0])
        else:
            adjacency_list[relationship[1]] = [relationship[0]]
    return adjacency_list
        

graph1 = to_adj_list(edge_list1)


def hasPath(source: str, destination: str, graph: dict[str, list[str]]) -> bool:
    '''
    Returns whether there exists a path from the given source node to the destination
    using a depth first search that uses an iterative approach and a stack
    
    Worst time complexity of all DPS searches is: O(E) = O(n^2)
    
    NOTE: we should use a breadth first search because it is slightly faster 
    both breadth first and depth first have the same worst time complexity, but depth first explores an entire path before it backtracks 
    '''
    stack = []
    visited = set()
    
    stack.append(source)
    # returns true if source equals destination
    while stack:
        current_node = stack.pop()
        if current_node == destination:
            return True
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                stack.append(neighbor)
                
    return False



def numIslands(graph: dict[str, list[str]]) -> int:
    '''
    Given a graph, returns the number of disjoint components using a depth first search 
    implemented iteratively using a stack
    
    Original attempt made more efficient
    No need to keep track of remaining_nodes, we just iterate through all the nodes.
    If node is not visited, then we start our depth-first search at that node. Lookup time complexity is O(1) because hashset
    '''
    count = 0
    # use a hashset because lookup is O(1)
    visited = set()
    # implicitly iterating over dict keys so no need to explicitly write graph.keys()
    
    # we need to go through every node in the graph, that way we can reach disconnected nodes as well
    for node in graph:
        # if node not visited
        if node not in visited:
            # we initialize a depth first search starting at that node and visit all connected nodes
            stack = [node]
            count += 1
            # this is the depth first search
            # while stack is not empty
            while stack:
                current = stack.pop()
                # there may be multiple instances of the current node waiting to be processed,
                # so we need to make sure we add them to the visited list (set) only once
                # not having this won't make the final results invalid because the set ensures the visited nodes remain unique
                # but it does improve performance by not processing the same nodes multiple times.
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
    return count


def biggestIslandSize(graph: dict[str, list[str]]) -> int:
    biggestIsland = 0
    
    visited = set()
    for node in graph:
        start = len(visited)
        if node not in visited:
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in visited:
                    visited.add(current)
                    for neighbor in graph[current]:
                        if neighbor not in visited:
                            stack.append(neighbor)
        islandSize = len(visited) - start
        if islandSize > biggestIsland:
            biggestIsland = islandSize
        # print(change)
    return biggestIsland
    
    

# pprint(graph1)

# print(hasPath('o', 'o', graph))
# print(numIslands(graph))
# print(numIslands(graph))
# print(biggestIslandSize(graph2))



def hasPathRecursive(source, destination, graph: dict[any, list[any]]):
    '''
    Use a recursive algorithm to search if there is a path from source to destination
    '''
    visited: set[any] = set()
    def explore(current):
        visited.add(current)
        if current == destination:
            return True
        for neighbor in graph[current]:
            if neighbor not in visited:
                
                if explore(neighbor):
                    return True
        return False
    
    return explore(source)

# print(hasPathRecursive('A', 'E', graph3))

def numIslandsRecursive(graph: dict[any, list[any]]):
    visited = set()
    count = 0
    
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
    for node in graph:
        if node not in visited:
            count += 1
            dfs(node)
            
    return count

# print(numIslandsRecursive(graph1))


def shortestPath(source, destination, graph: dict[any, list[any]])->int:
    visited = set()
    queue = deque()
    queue.append((source, [source]))
    while queue:
        print(queue)
        current, path = queue.popleft()
        # print((current, path))
        if current == destination:
            return path
        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return -1
    
# print(shortestPath('i', 'm', graph1))



island_grid = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]

def find_islands(grid: list[list[int]]) -> list[list[set[int]]]:
    '''
    Returns a list of coordinates of the islands that are present in the grid
    Land is denoted by 1 while 0 signifies water
    We go through each element and if it's 1, we start a depth first search. We don't keep a visited list
    like we do in traditional graph traversal. Instead, we mark each visited node by 0 that way we won't start another 
    depth first at that location
    '''
    def dfs(i, j):
        if (i < 0) or (i >= m) or (j < 0) or (j >= n):
            return
        if grid[i][j] == 0:
            return
        islands_map[-1].append((i, j))
        grid[i][j] = 0
        dfs(i, j+1)
        dfs(i, j-1)
        dfs(i+1, j)
        dfs(i-1, j)

    m, n = len(grid),  len(grid[0])
    # num_islands = 0
    islands_map: list[list[int]] = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                # num_islands += 1
                islands_map.append([])
                dfs(i, j)
    return islands_map

def find_num_islands(grid: list[list[int]]) -> int:
    return len(find_islands(grid))

def find_min_island(grid: list[list[int]]) -> list[set[int]]:
    return sorted(find_islands(grid), key=lambda x: len(x))[0]
                
print(find_min_island(island_grid))


def adjlist_to_adjmatrix(adjlist: dict[str, list[tuple[str, int]]]) -> list[list[int]]:
    pass