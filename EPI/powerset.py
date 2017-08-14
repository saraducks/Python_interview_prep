# get the input list and iterate them recurrsively

def powerset(A):
    def power_set_helper(input):
        # you already added the actaul set
        # store the current input pos
        curr_pos = input

        if curr_pos < 0:
            return result_set.append(None)

        for j in range(curr_pos, len(A)):
            k = input
            print j, k
            print [A[j-k:j]]
            print A[curr_pos],"curr"
            if A[curr_pos] not in A[j-k:j]:
                print True
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
# result = powerset(L1)
# print result


def new_powerset(List_A):
    result = [[]]
    for i in List_A:
        temp = [subset + [i] for subset in result]
        result.extend(temp)
    return result

# L8 = [1,2,3,4]
# res = new_powerset(L8)
# print res

def generate_power_set(input_set):
    # Generate all subsets whose intersection with input_set[0], ...,
    # input_set[to_be_selected - 1] is exactly selected_so_far.
    def directed_power_set(to_be_selected, selected_so_far):
        print "to be selected", to_be_selected
        print "selected", selected_so_far
        print power_set
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return

        directed_power_set(to_be_selected + 1, selected_so_far)
        print "I am executing"
        # Generate all subsets that contain input_set[to_be_selected].
        directed_power_set(to_be_selected + 1,
                           selected_so_far + [input_set[to_be_selected]])

    power_set = []
    directed_power_set(0, [])
    return power_set

res = generate_power_set([1,2, 3])
print res