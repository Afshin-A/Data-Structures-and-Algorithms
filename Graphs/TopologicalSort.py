from collections import deque
from pprint import pprint
from Queue.IndexedPriorityQueue import IndexedPriorityQueue
from Heap.MinHeap import MinHeap

graph1 = {
    'C': ['A', 'B'],
    'A': ['D'],
    'B': ['D'],
    'E': ['A', 'D', 'F'],
    'D': ['H', 'G'],
    'F': ['K', 'J'],
    'H': ['J', 'I'],
    'G': ['I'],
    'K': ['J'],
    'J': ['M', 'L'],
    'I': ['L'],
    'M': [],
    'L': [],
}

graph2 = {
    'A': [('B', 3), ('C', 6)],
    'B': [('E', 11), ('D', 4), ('C', 8)],
    'C': [('D', 8), ('G', 11)],
    'D': [('E', -4), ('F', 5), ('G', 2)],
    'E': [('H', 9)],
    'F': [('H', 1)],
    'G': [('H', 2)],
    'H': []
}

graph3 = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 2), ('E', 1), ('C', 3)],
    'C': [('B', 1), ('D', 4), ('E', 5)],
    'D': [],
    'E': [('D', 1)]
}

graph4 = {
    'S': [('A', 3), ('B', 4)],
    'A': [],
    'B': [('A', -5)]
}

graph5 = {
    'S': [('E', 8), ('A', 10)],
    'A': [('C', 2)],
    'B': [('A', 1)],
    'C': [('B', -2)],
    'D': [('A', -4), ('C', -1)],
    'E': [('D', 1)],
}

def is_DAG(graph: dict[str, list[str]])->bool:
    ''''''
    return True

def topological_order(graph: dict[str, list[str]]):
    '''
    How the algorithm works:
    We basically add leaf nodes and mark them off of the to-be-visited list
    In a tree, this looks like "cherry picking" the leaf nodes, starting from the bottom of the 
    and making our way to the head.
    
    Starting at a node, do a depth first search. When we reach a leaf node, we add it to the end of the list.
    
    '''
    # topological order doesn't exist if there's a directed cycle in the graph
    if not is_DAG(graph):
        return
    visited = set()
    # we use a double ended queue because in this algorithm, we build from left to right
    # it might be more efficient to use an array the size of all nodes, and keep track of an insersion index
    # this way we won't have to convert a queue (linked list?) to a list at the end (O(n))
    # but using a deque is simpler
    order = deque()
    
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        # *weight will unpack 2nd and the rest of elements into a list. if there is no second element, the list will be empty. without this technique, we will get a value error when the graph doesn't include weights
        for neighbor, *weight in graph[node]:
            dfs(neighbor)
        
        order.appendleft(node)
            
    for node in graph:
        dfs(node)
    
    return list(order)

# print(topological_order(graph1))


# shortest path, meaning find the path with the least weight
# graph must be a DAG
# does not care about positive or negative edge weights, where dijkstra's algorithm may not work with negative edge weights
# O(n^2) because that is the worst time complexity of dfs
# Single Source Shortest Path (SSSP)
def best_path(graph: dict[str, list[set[str, int]]]) -> dict[str: int]:
    '''Returns a map that maps each node with the minimum cost to reach that node starting at the 
    first node in a topological order
    
    We also want to know what that path is, and because the process is similar, I'm cramming it all in one function
    '''
    if not graph:
        return
    
    # First, sort all nodes in graph topologically
    order = topological_order(graph)
    # print(order)
    
    # Stores the least cost to get to each node
    # Initially, we set the cost of reaching all nodes to infinity (this is to make our comparisons work the first time a node is reached)
    cost = {node:float('inf') for node in order}
    path = {node:[] for node in order}
    # cost of reaching the first node is 0
    cost[order[0]] = 0
    path[order[0]] = [order[0]]
    
    # If the cost of reaching a neighbor from the current node (cost of reaching THAT node plus the edge cost)
    # is less than previously determined, then we've found a more efficient way, and we need to update the cost
    for node in graph:
        for neighbor, edge_weight in graph[node]:
            # If the current path is better than previously found
            if cost[node] + edge_weight < cost[neighbor]:
                # update the cost with the current cost
                cost[neighbor] = cost[node] + edge_weight
                # clear the bad path
                path[neighbor].clear()
                # replace it with the path to get to the parent, and append the neighbor
                path[neighbor] = path[node] + [neighbor]
                
    pprint(cost)
    pprint(path)
    return cost, path

# best_path(graph2)




# TODO: what happens when there is a negative edge or negative cycle?
# Add a mechanism that detects infinite loops and quits
# if dijstra's goes through all the nodes and there are n+1 iterations, does that mean we reached an infinite loop?
# need to implement a logic like that
def dijkstra(start: str, graph: dict[str, list[tuple[str, int]]]):
    '''
    Given a starting node, dijkstra's algorithm finds the 
    
    Some notes

this algorithm won't work with negative edges. this is because once we process all of a node's neighbors, 
 the algorithm marks with that node. positive edges to that node will increase the cost to get to that node, and since
we're looking for lower costs,  they can't possibly be the solution.
but negative edge weights can lower the cost to get to the node, after it's been processed

if we've processed all of a node's outgoing edges, can we safely add it to the visited list, even if there are incoming edges?

 Dijkstra's assumes that once you find the shortest path to a node (when it's polled from the min-heap), it won’t be improved by any future paths. Negative weights break this assumption.
After visiting a node, we would have already found the best 

after visiting a node, we would have found the best cost. this is because that node is the next one in the path
    '''
    # this set keeps track of graph nodes we have not visited
    unvisited = set(graph.keys())
    
    # this dictionary stores the best cost to reach each node
    cost: dict[str, int] = {node: float('inf') for node in graph}
    # cost to reach starting node is 0
    cost[start] = 0
    
    # this dictionary stores the best path to reach each node
    best_path = {node: [] for node in graph}
    # best path to reach starting node is itself
    best_path[start].append(start)
    
    # priority queue finds the next best path from the current node
    # it also allows us to update remaining nodes in the queue efficiently
    heap = IndexedPriorityQueue()
    
    # we enqueue each node as (cost, node) and the priority queue will sort based on weight
    heap.enqueue((cost[start], start))
    # while heap is not empty
    while heap:
        # dequeue the next best node
        # current cost is the best cost to the current node
        current_cost, current_node = heap.dequeue()
        # mark it as visited
        unvisited.remove(current_node)
        # loop through all unvisited neighbors
        for neighbor, neighbor_cost in graph[current_node]:
            if neighbor in unvisited:
                # calculate new cost from current node to that neighbor
                new_cost = current_cost + neighbor_cost
                # if cost is more efficient than what was already recorded in the cost map
                if new_cost < cost[neighbor]:
                    # then we found a better cost and path
                    # update the cost in the cost map
                    cost[neighbor] = new_cost
                    # store the better path, which is the path to the previous node plus the current node
                    best_path[neighbor] = best_path[current_node] + [neighbor]
                    # update the neighbor node in the queue with the newly found cost. if it doesn't exist, the function adds the node along wit hits best reach cost to the queue
                    heap.update_priority(neighbor, new_cost)
                    heap.debug_print()
        
    results = {node:(cost[node], best_path[node]) for node in cost}
    # pprint(best_path)  
    # pprint(cost)  
    # pprint(results)  
    return results

        
        

    
'''
number of updates >> number of removals
in a d-array heap, update will take a maximum of log_d(n) because you still have to bubble up or down the node. but to remove, you only bubble down
bubbling up is more efficient than bubbling down. to bubble up, you compare an element to its parent, which is done in constant time.
but to bubble down, you need to find the smallest child, which is an O(n) operation because the children are not ordered (the only requirement 
is that they must all be larger or smaller than their parent, aka the heap invariant)
removing only
the more edges there are, the more updates we will have to do. recall that max number of edges is n(n-1)/2.
The most optimal value for D in D array heap is found by E/n
'''


def bellmanFord(graph: dict) -> dict:
    '''
    - Description: SSSP (single source shortest path) algorithm using the bellman-ford algorithm
    - Time complexity O(|n||v|)
    - Explanation: for each iteration, we go through all edges. There are n-1 iterations. So time complexity is O(|n||V|)
    - Notes:
    -- We use this algorithm when there are negative edges in the graph
    -- It can be used to detect negative cycles
    -- The time complexity is much worse than dijskra's algorithm
    '''
    if not graph:
        return
    
    vertices = graph.keys()
    # number of vertices
    n = len(vertices)
    best_cost = {node: float('inf') for node in vertices}
    best_path = {node: [] for node in vertices}
    # get first node
    s = next(iter(vertices))
    # cost to first node is 0
    best_cost[s] = 0
    best_path[s].append(s)
    changed = True
    
    # iterations
    for _ in range(n-1):
        # if no change between iteration, then we found solution
        if not changed:
            break
        # reset the changed status at every iteration
        changed = False
        # for all nodes
        for current_node in vertices:
            # if best cost of a node is infinity, that means it hasn't been reached before. It might be disconnected
            # so we skip it            
            if best_cost[current_node] == float('inf'):
                continue
            # for neighbors of the current node
            for neighbor, cost_to_neighbor in graph[current_node]:
                alt_cost = best_cost[current_node] + cost_to_neighbor
                # if the best cost of reaching the neighbor can be improved, update it
                if alt_cost < best_cost[neighbor]:
                    # one True is enough to keep 
                    # I feel pretty big brain for coming up with this
                    changed |= True
                    best_cost[neighbor] = alt_cost
                    best_path[neighbor] = best_path[current_node] + [neighbor]
                else:
                    # if no changes at all, then algorithm is done and we can return results early
                    changed |= False
                    
    results = {node:(best_cost[node], best_path[node]) for node in best_cost}
    # pprint(best_cost)
    # pprint(best_path)
    # pprint(results)
    
    return results

graph6 = {
    'A': [('B', 2), ('D', 3)],
    'B': [('A', 3), ('C', 2)],
    'C': [('D', 4)],
    'D': [('B', 6), ('A', -2), ('C', -5)]
}

def graphToMatrix(dictGraph: dict[str, list[tuple[str, int]]]) -> list[list[int]]:
    '''
    Converts an adjacency list to an adjacency matrix
    '''
    # node to respective index map
    nti = {node:index for index, node in enumerate(dictGraph.keys())}
    # index to respective node map. This is needed in the floyd warshal algorithm to convert indices back to 
    itn = {index:node for index, node in enumerate(dictGraph.keys())}
    # cost matrix
    cMatrix = [[float('inf') for _ in dictGraph] for _ in dictGraph]
    # previous-node matrix. the node that comes second to last in the shortest path from A to B
    # it's used in re-creating the shortest path
    pMatrix = [[None for _ in dictGraph] for _ in dictGraph]
    for node, neighbors in dictGraph.items():
        i = nti[node]
        for neighbor, cost in neighbors:
            j = nti[neighbor]
            cMatrix[i][j] = cost
            pMatrix[i][j] = node
    
    for i in range(len(cMatrix)):
        cMatrix[i][i] = 0
    
    return itn, cMatrix, pMatrix


def floydWarshall(graph: list[list[int]]):
    '''
    Time complexity: O(n^3)
    Space complexity: O(n^2)
    
    This is a dynamic programming algorithm. We build up the solution from smaller parts
    '''
    indexToNode, M, T = graphToMatrix(graph)
    n = len(M)
      
    # for each iteration, we consider one node
    for k in range(n):
        # we go from node i to j through k: i -> k -> j 
        # if the path is better than i -> j then we update the matrix
        for i in range(n):
            for j in range(n):
                if k == i or k == j:
                    continue
                # does i to j have a better path through k?
                if M[i][k] + M[k][j] < M[i][j]:
                    M[i][j] = M[i][k] + M[k][j]
                    T[i][j] = indexToNode[k]
                    
    print(M)
    print(T)
    
    
    # run the algorithm a second time. if better values are found, that means those nodes are 
    # affected by a negative cycle
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if k == i or k == j:
                    continue
                # does i to j have a better path through k?
                if M[i][k] + M[k][j] < M[i][j]:
                    M[i][j] = float('-inf')
                    T[i][j] = -1
    pprint(M)
    pprint(T)

    



