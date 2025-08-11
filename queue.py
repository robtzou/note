"""
First-in, First-Out (FIFO)

Enqueue:    Adding a new item to the back of the queue.
Dequeue: Removing the item from the front of the queue.


"""

queue_list = []

# Enqueue elements
queue_list.append("X")
queue_list.append("Y")
queue_list.append("Z")
print(f"Queue (list) after enqueuing: {queue_list}")

# Dequeue elements
item_x = queue_list.pop(0) # Removing from the beginning is O(n)
print(f"Dequeued item: {item_x}")
print(f"Queue (list) after dequeuing 'X': {queue_list}")
