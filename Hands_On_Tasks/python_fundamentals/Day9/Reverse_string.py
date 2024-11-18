""" Reverse Word Order
    Write a program (using functions!) that asks the user for a long string containing multiple words. 
    Print back to the user the same string, except with the words in backwards order."""
    
words = "Good Morning, Welcome to Relevantz"

reversal = words.split()
print(*list(reversed(reversal)))

print(''.join(reversed(words)))
