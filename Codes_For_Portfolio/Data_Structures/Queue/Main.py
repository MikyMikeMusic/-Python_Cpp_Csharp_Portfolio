from Queue import Queue

q = Queue()


print(q.is_Empty())

for i in range(1, 10, 2):
    q.enqueue(i)
    print(f"Adding {i} to the queue")
    
print(f"Peek: {q.peek()}")
print(f"Rear: {q.get_rear()}")
