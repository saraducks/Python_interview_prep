'''
given a key and list, delete a node of given value.
1. check if the curr node's next value is equal to the key
2. just adjust the pointer to next of next
'''
# Time complexity is O(n) and space complexity is O(1)

def delete_node(input_list, key):
    dummy_head = temp = input_list

    while temp:
        if temp.val == key:
            # copy the next node value to this node and delete the next node
            temp.val = temp.next.val
            temp.next = temp.next.next
            return dummy_head
        else:
            temp = temp.next



