'''Task : 7 Count Occurrences of Each Character:
source = "hello world"'''
# Write a function that counts the occurrences of each character in the string and returns a dictionary:

# Expected output = {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}


def count_function(source):
    
    source_dic = {}

    words = source.strip()
    print(words)

    for character_count in words:
        if character_count in source_dic:
            source_dic[character_count] = source_dic[character_count] + 1
        else:
            source_dic[character_count] = 1
    print(source_dic)

count_function("hello world")