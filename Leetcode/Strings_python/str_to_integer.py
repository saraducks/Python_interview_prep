def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if len(str) == 0:
        return 0

    set_negative = False
    if str[0] == '-':
        set_negative = True
    start_range = 1 if set_negative == True else 0
    for i in range(start_range, len(str)):
        if not str[i].isdigit():
            return "No special characters"

    return -1 *int(str[1::]) if set_negative else int(str)


result = myAtoi("-123")
print result