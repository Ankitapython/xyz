l=[1,4,0,0,6,0,7,0,0,5]
print([j for j in l if j==0]+[i for i in l if i!=0])

# stack

stack = []

stack.append('b')
stack.append('c')
stack.append("a")

print('Initial stack',stack)
# print(stack)

print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
# print(stack.pop())

print('\nStack after elements are poped:',stack)
# print(stack)

# queue
from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue)

a=[7,4,3,5,6,9,1]
x=8
print ([(x-k,k) for k in a if (x-k) in a])