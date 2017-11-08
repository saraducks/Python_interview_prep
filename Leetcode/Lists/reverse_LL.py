'''
Given a LL, how will you reverse it.

'''

class LL:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def rev_linkedlist(input_list):
    # check if the list is none or length is 1 return list
    if input_list.next == None or input_list is None:
        return input_list

    else:
        rev_list = input_list
        curr_list = input_list.next
        rev_list.next = None

        while curr_list:
            temp = curr_list
            curr_list = curr_list.next

            temp.next = rev_list
            rev_list = temp
    return rev_list

import time
strat = time.time()
L = head = LL(12)
idx = 1

while idx < 10000000:

    L.next = LL(idx)
    L = L.next

    idx += 1

result = rev_linkedlist(head)
end = time.time()
print("Time difference", end-strat)

while result:
    print(result.val, "---->")
    result = result.next