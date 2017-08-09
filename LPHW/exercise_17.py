def print_word(input_string):  # It will print the given input string
    print input_string

def split_string(input_string):             # Split the string based on white spaces
    word = input_string.split(' ')
    return word

def sort_words(input_string):              # It will sort the string
    return sorted(input_string)

def firstword(input_string):               # gives first word from the list
    return input_string.pop(0)

def lastword(input_string):                # last word from the list
    return input_string.pop()

def first_last_word(input_string):          # returns the first and last word of the sentence
    temp = split_string(input_string)
    result = sort_words(temp)
    return firstword(result),lastword(result)

sentence = "Hello, Can you hear me?"
temp = split_string(sentence)
print temp
temp1 = sort_words(temp)
print temp1
temp2 = firstword(temp1)
print temp2
temp3 = firstword(temp1)
print temp3