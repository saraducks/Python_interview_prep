from __future__ import print_function

from LL import LL as RL

'''
remove duplicates from the unsorted linked list
1. use hash key as node val, val as the no of occurences
2. we will check every time if the given node val is in the hash table 
'''
# the time complexity is O(n) and the space complexity is O(k), K is the unique elements
def remove_duplicates(input_list):
    h = {}                                                                   #initialize the hash map
    dummy_head = input_list

    while input_list.next is not None:
        try:
            h.get(input_list.next.val)
            input_list = input_list.next.next
        except:
            h[input_list.val] = 1
            input_list = input_list.next

    return dummy_head

R = head = RL("head")

L = [45, 67, 89, 34, 56, 90, 76, 67, 123, 321, 890, 450, 421, 780, 900, 999, 1000, 123, 909, 900, 12, 34, 3210, 1000, "tail"]

i = 1

while i < len(L):
    R.next = RL(L[i])
    R = R.next
    i += 1

result = remove_duplicates(head)

while result and result.val is not "tail":
    print(result.val, end="---->")
    result = result.next
print(result.val, end = " ")

