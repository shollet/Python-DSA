import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
print(customQueue.qsize())
customQueue.put(1)
customQueue.put(1)
customQueue.put(1)
print(customQueue.qsize())
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())