'''
Description:

Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''

def high(x):
    sum_list = []
    word_list = x.split(' ')
    
    for word in word_list:
        sum = 0
        for character in word :
            number = ord(character) - 96
            sum += number
        sum_list.append(sum)
    
    
    max = 0
    max_num = 0
    
    for i in range(len(sum_list)) :
        if sum_list[i] > max:
            max = sum_list[i]
            max_num = i
    

    return word_list[max_num]
