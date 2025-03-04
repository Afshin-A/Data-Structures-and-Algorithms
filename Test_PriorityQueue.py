from Queue.PriorityQueue import PriorityQueue
from random import randint



l = [randint(0, 9) for _ in range(10)]
print('l:', l)
q = PriorityQueue(l)
print(q)
q.add(5)
print('added 5:', q)
q.dequeue()
print('after dequeue:', q)
q.enqueue(5)
print('head:', q.peek())
print('contains 5:', q.contains(5))
print('count of 5 before removal:', q._queue._heap.count(5))
q.remove(5)
print('count of 5 after removal:', q._queue._heap.count(5))
print('element at index 0:', q[0])
