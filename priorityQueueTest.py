from Queue.IndexedPriorityQueue import IndexedPriorityQueue

if __name__ == '__main__':
    tasks = [
        (5, 'shower'),
        (4, 'shave'),
        (1, 'cook'),
        (3, 'clean'),
        (6, 'study'),
        (0, 'shop'),
        (2, 'eat'),
    ]
    taskQueue = IndexedPriorityQueue(tasks)
    taskQueue.debug_print()
    taskQueue.dequeue()
    # taskQueue.dequeue()
    taskQueue.update_priority('study', 0)
    taskQueue.debug_print()
    
