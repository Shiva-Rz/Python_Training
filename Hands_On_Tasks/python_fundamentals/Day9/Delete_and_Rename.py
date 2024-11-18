'''How would you delete and rename a file?'''

import os

# Approach - 1
file_name = input("Enter your file name")
os.remove(file_name)

# Approach - 2
file_name = input("Enter your file name")
if os.path.exists(file_name):
    os.remove(file_name)

# Approach - 3
file_name = input("Enter your file name : ")
try:
    os.remove(file_name)
except FileNotFoundError:
    print(FileNotFoundError)

'''File Rename'''
file_name = input("Enter your file name : ")
rename_file = input("Rename your file : ")

try:
    os.rename(file_name, rename_file)
except FileExistsError:
    print(f"{file_name} already exist")
except FileNotFoundError:
    print(f"{file_name} doesn't exist")
