def test_math_func(x,y):
    addition = x + y;             #This is to test '+' addition
    print "This is addition", addition
    if x > y:                     # check which number is great and then perform '-' subraction
        subraction = x - y
        print "This is subraction", subraction
    else:
        subraction = y - x
        print "This is subraction", subraction
    if x > y:                    # check if numerator is greater than denominator
        division = x/y
        print "This is division", division
    else:
        division = y/x
        print "This is division", division
    multiplication = x * y       #This is to test '*'
    print "This is Multiplication", multiplication
    remainder = x % y            #test my modulo and get my remainder
    print "This is remainder", remainder
    temp = True if x < y else False #test '<' symbol and else will evaluate to x '>' y
    print "Test < and > logic", temp
    print "whats is 5 % 2", 5 % 2  #evaluating directly from print statement
    print "if x <= y", 4<=2

test_math_func(4,5)    # This will call my tes_math_function.

