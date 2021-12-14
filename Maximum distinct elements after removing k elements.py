import collections
import heapq
def maxoccur(arr,k):
    d = collections.Counter(arr)
    heap = [(-value, key) for key,value in d.items()]
    heapq.heapify(heap)
    while (heap) and (k > 0):
        k -= 1
        x = heapq.heappop(heap)
        if x[0] < -1:
            heapq.heappush(heap,(x[0]+1,x[1]))
    return len(heap)

k = 47
arr = [int(i) for i in '28 26 24 26 17 13 10 2 3 8 21 20 24 17 1 7 23 17 12 9 28 10 3 21 3 14 8 26 30 13 13 19 30 28 14 17 2 23 10 4 22 30 15 8 9 15 6 1 24 17 2 21 27 4 3 21 17 2 16 16 15 28 27 6 17 10 14 18 25 16 13 16 15 28 15 15 4 21 8 19 7 9 9 25'.split()]
print(maxoccur(arr,k))

arr = [5, 7, 5, 5, 1, 2, 2]
k = 3
print(maxoccur(arr,k))
