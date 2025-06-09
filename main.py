from Stack.SyntaxCheck import check_syntax

from Queue.Queue import Queue, ArrayQueue
from LinkedList.DoublyLinkedList import DoublyLinkedList
# from HashTable.HashTable import HashTableSeperateChaining, HashTableXProbing
# from HashTable.HashTableOOP import HashTableDoubleHashProbe, HashTableLinearProbe, HashTableQuadraticProbe
from HashTable.HashMap import HashMap

from Heap.Heap import MaxHeap
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

# hashMap = HashMap()
# hashMap['Afshin'] = 2109476915
# hashMap.add('Sepideh', 2545771197)
# hashMap.add('Mom', 2104130460)
# # print(hashMap)

# hashMap['Afshin'], hashMap['Sepideh'] = hashMap['Sepideh'], hashMap['Afshin']

# for key, value in hashMap:
#     print(key, value)


# from UnionFind.UnionFind import UnionFind
from UnionFind.UnionFindIndex import UnionFind
           # 0    1    2    3    4    5    
elements = ['a', 'b', 'c', 'd', 'e', 'f']
uf = UnionFind(elements)
print('*' * 10)
uf._add(1, 2)
uf._add(3, 4)
uf._add(4, 5)
print(uf)
uf._add(4, 2)
uf._add(0, 5)
print(uf)
print(uf.groups())
# print(uf)
# print(uf)
# print('*' * 10)
# uf.add('d', 'c')
# print(uf)

# # uf.find(50)
# # print(uf)


# keys = [1, 2, 3, 4, 5]
# values = [6, 7, 8, 9, 10]
# keys_cache = keys.copy()
# values_cache = values.copy()

# for i in range(self._size):
#     keys_cache.append(self._keys[i])
#     values_cache.append(self._values[i])

# self._keys = [None] * self._capacity 
# self._values = [None] * self._capacity

# print('resizing to new size: ', self._capacity)
# for key, value in zip(keys_cache, values_cache):
#     print('adding', key, value)
#     if key and key != self._TOMBSTONE:
#         self.add(key, value)


# hm = HashMap()
# l = [i for i in range(100)]
# for index, value in enumerate(l):
#     hm.add(index, value)
    
# print(hm)