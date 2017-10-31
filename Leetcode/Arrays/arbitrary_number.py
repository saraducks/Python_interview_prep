'''
Search a given number in a sorted array that has been rotated by some arbitrary number.

TO DO:
get the inversion point
check with the search_key

'''
def element_arbitraryarray(input_array, key_item):
    # get the inversion point
    inversion_idx = 0
    i = 0
    while i < len(input_array):
        if input_array[i] > input_array[i+1]:
            inversion_idx = i
            break
        i += 1

    first_half = input_array[0:inversion_idx]
    print(first_half)
    second_half = input_array[inversion_idx+1:]
    print(second_half)


    if len(first_half) and key_item < first_half[0]:
        res =  search_element(second_half, key_item)
        print(len(first_half) +res)
    else:
        res =  search_element(first_half, key_item)
        print(res)

# binary search
def search_element(input_list, key):
    left, right = 0, len(input_list)

    while left <= right:
        mid = (left + right) // 2

        if input_list[mid] == key:
            return mid
        elif input_list[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1

input_list = [176,188,199,200,210,222,1,10,20,47,59,63,75,88,99,107,120,133,155,162]
# sec_l = [1,10,20,47,59,63,75,88,99,107,120,133,155,162]
# res = search_element(sec_l, 75)
# print(res)
element_arbitraryarray(input_list, 75)
