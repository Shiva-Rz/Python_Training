'''Task 1 : String Anagram Checker: 
Write a function that checks if two strings are anagrams of each other (e.g., "listen" and "silent"). 
Ignore spaces and case sensitivity.'''


def anagrams(word, value):

    first_word = sorted(word.lower())
    second_word = sorted(value.lower())

    first_space = [first for first in first_word if first.strip()]
    print(f"The {word} is sorted into :  {first_space}")
    
    # new_list = []
    
    # for first in first_word:
    #     if first.strip():
    #         new_list.append(first)
    # print(new_list)

    second_space = [second for second in second_word if second.strip()]
    print(f"The {value} is sorted into :  {second_space}")

    if first_space == second_space:
        print(f"The '{word}' and '{value}' is Anagram")
    else:
        print(f"The '{word}' and '{value}' isn't Anagram")
        
    print(type(first_space))

anagrams("LIsten", "s i l e n t ") 