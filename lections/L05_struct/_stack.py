stack = []
stack.append(1)    # [1]
stack.append(2)    # [1, 2]
stack.append(3)    # [1, 2, 3]
top = stack.pop()  # [1, 2]

from collections import deque
stack = deque()
stack.append(1)    # 1
stack.append(2)    # 1, 2
stack.append(3)    # 1, 2, 3
print(list(stack)) # [1, 2, 3]
print(stack[-1])
top = stack.pop()  # 3
print(list(stack)) # [1, 2]
print(len(stack))
while stack: print(stack.pop())


from collections import deque

queue = deque()

queue.append(1)     # встал в очередь
queue.append(2)
queue.append(3)
print(list(queue))  # [1, 2, 3]
first = queue.popleft()  # 1 ушёл
print(len(queue))   # 2
print(list(queue))  # [2, 3]
while queue: 
    print(queue.popleft())