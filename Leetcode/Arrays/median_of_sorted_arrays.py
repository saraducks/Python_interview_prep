import math
# find the median of the two sorted arrays
# input [1,3] [2]
# output 2

# approach 1 combine the two arrays and return the result
def find_median(input1, input2):
    # case 1 if input1 length is 0 and input2 length is greater than 0
    if len(input1) == 0 and len(input2) > 0:
        return compute_median(first_array=None,second_array=input2)
    #case2 if the input2 length is 0 and input1 length is 1
    elif len(input1) > 0 and len(input2) == 0:
        return compute_median(input1, second_array=None)
    #case3 if both the input length is greater than 0
    elif len(input1) > 0 and len(input2) > 0:
        return compute_median(input1, input2)
    #case4 if both the input1 and input2 length is 0 return None
    else:
        return 0


def compute_median(first_array, second_array):
    # check if both the input is not none else just return the median based on size of the single array
    # case 1 first_array is None and second_array is greater than 0
    if first_array is None and second_array:
        return median(second_array)
    # case 2 first_array is not None and second array is None
    elif first_array and second_array is None:
        return median(second_array)
    else:
        #combine the array and call median on the combined array
        first_array_ptr = 0
        second_array_ptr = 0
        equal = False

        if len(second_array) < len(first_array):
            temp = first_array
            first_array = second_array
            second_array = temp
            print(first_array)
            print(second_array)

        if len(second_array) == len(first_array):
            equal = True

        temp = []
        while first_array_ptr < len(first_array) and second_array_ptr < len(second_array) if equal == True else None:

            # compare and append the result to temp
            if first_array[first_array_ptr] < second_array[second_array_ptr]:
                temp.append(first_array[first_array_ptr])
                print("temp", temp)
                first_array_ptr += 1

            elif second_array[second_array_ptr] < first_array[first_array_ptr]:
                temp.append(second_array[second_array_ptr])
                print("temp", temp)
                second_array_ptr += 1

            elif first_array[first_array_ptr] == second_array[second_array_ptr]:
                temp.append(first_array[first_array_ptr])
                print("temp", temp)
                first_array_ptr += 1
                second_array_ptr += 1
            print(first_array_ptr, second_array_ptr)

        if first_array_ptr < len(first_array):
            temp.extend(first_array[first_array_ptr:len(first_array)])

        if second_array_ptr < len(second_array):
            temp.extend(second_array[second_array_ptr:len(second_array)])
        print("temp",temp)
        # call median
        return median(temp)

def median(input_array):
    size_of_inputarray = len(input_array)
    if size_of_inputarray % 2 == 0:
        temp_size = size_of_inputarray / 2
        return float(input_array[temp_size-1] + input_array[temp_size])/float(2)
    else:
        return float(input_array[int((size_of_inputarray)/2)])


# input
# input1 = [1,3]
# input2 = [2]
# output ----> 2.0

# input
#input1 = [1, 2]
#input2 = [3, 4]

# output ---> 2.5

#input1 = [1, 2]
#input2 = [1, 1]

# output ---> 1.0

#input1 = []
#input2 = [1]

#output ---> 1.0

#input1 = [100001]
#input2 = [100000]
#output ---> 100000.5

input1 = [1,3]
input2 = [2]
res = find_median(input1, input2)
print(res)