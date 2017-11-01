'''
Given a sentence reverse the strings
'''

def reverse_given_sentences(input_sentences):
    #first check if the given sentence is empty
    if len(input_sentences) == 0 or len(input_sentences) < 2:
        return input_sentences
    # copy the input_sentences to list
    res = input_sentences.split()

    start, end = 0, len(res)-1
    # swap the elements from front with the tail
    while start < end:
        res[start], res[end] = res[end], res[start]
        start += 1
        end -= 1
    # this will print the swapped list into a sentence
    print(' '.join(res))



reverse_given_sentences("The quick brown fox jumped over the lazy dog.")

# Time complexity O(n)
# space complexity O(n)
