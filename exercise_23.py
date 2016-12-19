'''
combine for-loop, List, if-statements, function
'''

def demo(user_input):                                   # compare user result and call the add_element
    temp = 10
    if user_input < temp:
        add_element(user_input)
    else:                                               # if condition fails, execute the else statement
        print "enter the number less than %r" % temp


def add_element(get_input):                             # add elements to the empty list
    list_test = []
    print "Enter the %r numbers and I will append to the list" % get_input
    for i in range(0,get_input):
        list_test.append(raw_input())
    print "Do you want me to sort the list, yes/no?"      # based on user preference, sorted it or return the list
    get_yes_no = ['yes','no']
    user_option = raw_input()
    if user_option == "yes":
        print  sorted(list_test)
    else:
        print "Here's your input list"
        print list_test

def play_for(get_input):                                # while-loop, it fails once the condition temp1 >= 10 is False
    temp1 = get_input
    while temp1 >= 10:
        print temp1
        temp1 = temp1 - 1




demo(4)
play_for(12)