# given a students marks [98, 23, 67, 76, 40, 35, 90, 94]
# distribute the candy, each person will compare the number of candies their neighbours has received based on their marks
# [98, 23, 67, 76, 40, 35, 90, 94]
# [ 3,  1,  2,  3,  1,
# [ 3,  1,  2,  4,  2,  1,  2, 3]
# [98, 23, 67, 76, 40, 35, 90, 90, 94]
# [ 3,  1,  2,  4,  2,  1,  2, 2, 3]


def distribute_candy(input_list):
    total_candies = 0
    local_candy = 1
    prev_count = 0
    for i in range(0, len(input_list)):
        if input_list[i] < input_list[i-1]:
            # iterate until you find the element > elem_at_front
            total_candies += local_candy
            # find the increment
            count = 0
            local_i = i
            while local_i >= 1:
                if input_list[local_i] > input_list[local_candy-1]:
                    count += 1
                    break
                count += 1
                local_i -= 1
            prev_count = 1
            total_candies += count

        elif input_list[i] == input_list[i-1]:  #if there is a equal distribution then I should know the
            total_candies += prev_count

        else:
            total_candies += 1

            prev_count = total_candies

    print(total_candies)


# Test case 1
student_marks = [98, 23, 67, 76, 40, 35, 90, 94]  # ----> should return 18
distribute_candy(student_marks)

# Test case 2
student_mark1 = [98, 23, 67, 76, 40, 35, 90, 90, 94]  #-------------> should return 19
# distribute_candy(student_mark1)

# Test case 3
student_mark2 = [38, 49, 50, 60, 78, 90, 100]         # -------------> [1, 2, 3, 4, 5, 6, 7]
distribute_candy(student_mark2)