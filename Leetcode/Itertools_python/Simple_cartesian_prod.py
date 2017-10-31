# given a input which is spaced seperated, first line is the list A and the second line indiciates the list B
# return the cartesian product with the space seperated
from __future__ import print_function

from itertools import product

# naive method without using the python mao tool
#
# list_A = list(input().strip().split())
# list_B = list(input().strip().split())
#
#
# def convert_str_to_num(list_t):
#     for i in range(0, len(list_t)):
#         list_t[i] = int(list_t[i])
#     return list_t
#
#
# conv_to_numA = convert_str_to_num(list_A)
# conv_to_numB = convert_str_to_num(list_B)
#
# result_prod = (list(product(conv_to_numA, conv_to_numB)))
#
# for i in range(0, len(result_prod)):
#     print(result_prod[i], end ='')
#
#

list_A = map(int, input().split())
list_B = map(int, input().split())


result_prod = (list(product(list_A, list_B)))

for i in range(0, len(result_prod)):
    print(result_prod[i], end=" ")



