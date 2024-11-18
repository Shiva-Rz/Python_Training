"""Task 2 : Count Words in a Sentence:
Input : source = "This is a test sentence. This is only a test."""

# Write a function that counts the occurrences of each word and returns a dictionary:

# Expected output = {'This': 2, 'is': 2, 'a': 2, 'test': 2, 'sentence.': 1, 'only': 1}

def word_count(source):
    
    dic = {}

    source_words = source.split()
    print(source_words)

    for count in source_words:
        if count in dic:
            dic[count] = dic[count] + 1
        else:
            dic[count] = 1
    print(dic)

    # count = 0
    # for words in source:
    #     if words == source_count:
    #         count = count + 1
    #         print(count)
    # print(source, count)
    
word_count("This is a test sentence. This is only a test.")