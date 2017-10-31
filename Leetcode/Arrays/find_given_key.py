'''
Given the array, find if the given key is in the array
1. is array sorted? -----> use binary search
2. If array is not sorted?
'''

def find_given_key(input_array, key_to_search):
    left, right = 0, len(input_array)

    while left < right:
        mid = left + (right - left) // 2

        if input_array[mid] == key_to_search:
            return mid
        elif input_array[mid] < key_to_search:
            left = mid + 1
        else:
            right = mid - 1

    return -1

temp_array = [1, 10, 20 ,47, 59, 63, 75, 88, 99, 107 ,120, 133, 155, 162, 176, 188, 199, 200, 210, 222]
res = find_given_key(temp_array, 20)
print(res)
