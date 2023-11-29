import heapq

heap = []
heapq.heappush(heap,4)
heapq.heappush(heap,1)
heapq.heappush(heap,7)
heapq.heappush(heap,3)
heapq.heappush(heap,9)
print(heap)
# min_element=heapq.heappop(heap)
# print(min_element)
# print(heap)
print(heap[0])
print(heap)
sorted_elements = []
while len(heap) != 0:
    sorted_elements.append(heapq.heappop(heap))
print(sorted_elements)
print(f"heap={heap}")
