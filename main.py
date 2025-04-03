from Stack.SyntaxCheck import check_syntax

from Queue.Queue import Queue, ArrayQueue
from LinkedList.DoublyLinkedList import DoublyLinkedList
# from HashTable.HashTable import HashTableSeperateChaining, HashTableXProbing
# from HashTable.HashTableOOP import HashTableDoubleHashProbe, HashTableLinearProbe, HashTableQuadraticProbe
from HashTable.HashMap import HashMapLinearProbe
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

# hashTable = HashtableSeperateChaining()
# for _ in range(20):
#     hashTable.add(randint(1, 100))

# print(hashTable)

# hashTable = HashTableXProbing(probing_method='linear')

# hashTable.add(1)
# hashTable.add(12)
# hashTable.add(2)
# hashTable.add(5)
# hashTable.add(19)
# hashTable.add(38)
# hashTable.add([1, 12, 2, 5, 19, 38])
# hashTable.remove(1)
# print(hashTable.contains(38))
# print(hashTable)

# hashTable = HashTableLinearProbe()
# hashTable.add([1, 12])
# print('table size after adding two items:', hashTable.size())
# hashTable.remove(12)
# print('table size after removing 1 item:', hashTable.size())
# print(hashTable)
# hashTable.add(12)
# print(hashTable)
# print('table size: ', hashTable.size())

hashMap = HashMapLinearProbe()
hashMap['Afshin'] = 2109476915
hashMap.add('Sepideh', 2545771197)
hashMap.add('Mom', 2104130460)
# print(hashMap)

hashMap['Afshin'], hashMap['Sepideh'] = hashMap['Sepideh'], hashMap['Afshin']

for key, value in hashMap:
    print(value)
