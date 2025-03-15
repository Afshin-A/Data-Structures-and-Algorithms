from Stack.SyntaxCheck import check_syntax

from Queue.Queue import Queue, ArrayQueue
from LinkedList.DoublyLinkedList import DoublyLinkedList
from HashTable.HashTable import HashtableSeperateChaining

import sys

from random import randint

# print(syntax_check_refactored('[({}[][)]'))

# queue = ArrayQueue(5)
# queue.enqueue(1)
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.enqueue(5)
# queue.dequeue()
# queue.enqueue(6)
# print(queue)
# print(queue[0])
# queue.dequeue()
# print(queue)
# print(queue[0])
# queue.dequeue()
# print(queue)
# print(queue[0])
# queue.dequeue()
# print(queue)
# print(queue[0])
# queue.dequeue()
# print(queue)
# print(queue[0])
# queue.dequeue()
# print(queue)
# print(queue[0])
# queue.dequeue()
# print(queue)
# print(queue[0])

hashTable = HashtableSeperateChaining()
for _ in range(20):
    hashTable.add(randint(1, 100))

print(hashTable)