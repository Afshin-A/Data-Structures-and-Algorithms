from Graphs.TopologicalSort import graph3, dijkstra, bellmanFord, graph5, graph6, graphToMatrix, floydWarshall
from Queue.IndexedPriorityQueue import IndexedPriorityQueue
from pprint import pprint





# print(dijkstra('A', graph3))
# print(dijkstra('S', graph4))

# pq = IndexedPriorityQueue()
# pq.enqueue((0, 'A'))
# pq.dequeue()
# pq.update_priority('B', 4)
# pq.update_priority('C', 2)
# pq.dequeue()
# pq.update_priority('B', 3)
# pq.update_priority('D', 6)
# pq.update_priority('E', 7)


# pq.debug_print()



        
    
# print(bellmanFord(graph5))

graph7 = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', -3), ('C', 3)],
    'C': []
}    
# floydWarshall(graph7)

