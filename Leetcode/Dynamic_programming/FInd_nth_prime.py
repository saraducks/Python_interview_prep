# Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
# The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15,
# shows the first 11 ugly numbers. By convention, 1 is included

def find_nth_prime(input_number):
    result_array = [1]
    num = 2

    # check for the 2, 3, 5 recurrsively, if the result is 1 then it's ugly number
    def test_num(input_number, divisor):
        while input_number % divisor == 0:
            input_number = input_number / divisor
        return input_number
    #     if input_number:
    #         temp = input_number/divisor
    #         if input_number % divisor != 0:
    #             return input_number
    #         else:
    #             test_num(temp, divisor)


    input_number = test_num(input_number, 2)
    input_number = test_num(input_number, 3)
    input_number = test_num(input_number, 5)

    if input_number == 1:
        result_array.append(input_number)

    print result_array

find_nth_prime(15)
