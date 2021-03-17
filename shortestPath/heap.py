import heapq
h = []
heapq.heappush(h, (3, "Go to home"))
heapq.heappush(h, (10, "Do not study"))
heapq.heappush(h, (1, "Enjoy!"))
heapq.heappush(h, (4, "Eat!"))
heapq.heappush(h, (7, "Pray!"))
print(h)

while(h):
    print(heapq.heappop(h))


h = []
heapq.heappush(h, 300)
heapq.heappush(h, 200)
heapq.heappush(h, 100)
heapq.heappush(h, 400)
heapq.heappush(h, 250)

print(h)

while(h):
    print(heapq.heappop(h))