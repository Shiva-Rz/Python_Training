'''Write a Python program to read a file line by line and store it into a list.'''

file_list = []
file = open('file_3.txt', 'r')

for file_read in file:
    file_list.append(file_read.replace('\n',''))

print(file_list)

file.close()