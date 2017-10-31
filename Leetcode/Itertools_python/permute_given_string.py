# input will be of the form LEETCODE 3 (the LEETCODE is the string we have to permute and the length of perm is 3)

from itertools import permutations

get_string, k = input().strip().split(' ')

sorted_str_input = sorted(get_string)
k_as_num = int(k)
res = list(permutations(sorted_str_input,k_as_num))

for i in range(0, len(res)):
    print(''.join(res[i]))



