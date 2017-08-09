# get the input list and iterate them recurrsively

def powerset(A):
    def power_set_helper(input):
        # you already added the actaul set
        # store the current input pos
        curr_pos = input

        if input < 0:
            return result_set.append(None)

        for j in range(input+1, len(A)):
            k = input
            print j, k
            if A[j-k:j] not in A[curr_pos]:
                result_set.append([A[curr_pos],A[j-k:j]])
        power_set_helper(input-1)


    result_set = []
    result_set.append(A)
    power_set_helper(len(A)-1)
    return result_set


L = [1,2,3]
# op:[[1, 2, 3], [2, 3], [1, 2], [1, 3], None]
L1 = [1,2,3,4]
# op: [[1, 2, 3, 4], [3, 4], [2, 3], [2, 4], [1, 2], [1, 3], [1, 4], None]
# actual output: [[1,2,3,4], [1,2,3],[1,3,4],[2,3,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[1],[2],[3],[4],[]}
result = powerset(L1)
print result



