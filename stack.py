"""
Last-in, First-Out (LIFO)

Push :      add a new item to the top of the stack
Pop  : removing the item from the top of the stack
Peek : Look at the top item without removing it
"""

stack = []

# Push elements onto the stack
stack.append("A")
stack.append("B")
stack.append("C")
print(f"Stack after pushing elements: {stack}")

# Pop elements from the stack
item_c = stack.pop()
print(f"Popped item: {item_c}")
print(f"Stack after popping 'C': {stack}")

item_b = stack.pop()
print(f"Popped item: {item_b}")
print(f"Stack after popping 'B': {stack}")
