from collections import deque
word = 'hello'
q = deque(word)
print(''.join(q.pop() for i in range(len(word))))