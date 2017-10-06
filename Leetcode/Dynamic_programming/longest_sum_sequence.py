# given an array return the longest sum subsequence
# to know the longest sequence you should know the result of previous results
# Store the max sum of each row, start_index and it's end index

def find_largestsum_seq(input_array):
    def find_longest_seq_helper(start_idx):
        curr_max, idx = input_array[start_idx], start_idx   # stores the curr_max, start_idx, end_idx(where the curr_max is found)
        prev = input_array[start_idx]                       # to store the previous sum_result
        for temp in range(start_idx+1, len(input_array)):
            res[start_idx][temp] =  input_array[temp] + prev
            prev = res[start_idx][temp]
            # if the current_sum at the temp position is larger than the maximum recorded then update the curr_max
            if res[start_idx][temp] > curr_max:
                curr_max, idx = res[start_idx][temp], temp

        res[start_idx][len(input_array)] = [curr_max, start_idx, idx]
        return res

    # initializing the res table to 0 with additional space at the end where it stores the maximum_element_in_given_row,
    # start_idx, end_idx
    res = [[0]*(len(input_array)+1) for _ in range(len(input_array))]

    for i in range(0, len(input_array)):
        find_longest_seq_helper(i)

    return res

temp_arr = [-2, -3, 4, -1, -2, 1, 5, -3]
get_result = find_largestsum_seq(temp_arr)

# now iterate the res and based on the last index array value return the result
ret_maxmimum = [0,0,0]
for k in range(0, len(get_result)):

    if get_result[k][-1][0] > ret_maxmimum[0]:
        ret_maxmimum = get_result[k][-1]

print(ret_maxmimum)
