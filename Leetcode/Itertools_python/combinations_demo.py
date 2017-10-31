from itertools import combinations

get_input_string, k = input().strip().split()
get_input = sorted(get_input_string)
k_num = int(k)
result=[]

for i in range(k_num+1):
    result.extend(list(combinations(get_input, i)))

for i in range(1,len(result)):
    print(''.join(result[i]))

