import heapq
from collections import deque

'''
Given a large array of integers and a window of size 'w', find the current maximum in the window as the window slides through the entire array.
'''

# O(nw) time complexity, O(k) space complexity
def find_max_window(input_array, window_size):
    max_res = []
    for i in range(0, len(input_array)-1):
        max_res.append(max(input_array[i:i+window_size]))
    return max_res

# heap is another best solution
# space complexity O(w) and time complexity is O(n log window_size)

def find_max_window1(input_array, window_size):
    max_heap = []
    for i in range(0, len(input_array)):
        if len(max_heap) == window_size:
            heapq.heappushpop(max_heap, input_array[i])
        else:
            heapq.heappush(max_heap, input_array[i])
    print(max_heap)

# doubly linked list reduce the time_complexity to O(n)
def find_max_window2(input_array, window_size):
    max_heap = deque([])

    for i in range(0, len(input_array)):
        while len(max_heap) > 0 and max_heap[-1] < input_array[i]:
            if len(max_heap) > 0:
                max_heap.popleft()
        max_heap.append(input_array[i])

        if len(max_heap) > window_size:
            max_heap.popleft()

    print(max_heap)


temp_array = [-4, 2, -5, 3, 6]
find_max_window2(temp_array, 3)      #---------> output:6
find_max_window1(temp_array,3)