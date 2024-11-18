"""File Read"""
# file = open("readme.txt", "r")
# print(file.read())

# file = open("readme.txt", "a")
# file.write("\nI'm from Madurai")

# file.close()

# with open('readme.txt') as file:
#     file_read = file.read()
#     print(file_read)
#     file.close()

# with open('readme.txt') as f:
#     [print(line) for line in f.readlines()]

# file_image = open('images.jpg', 'rb')
# # print(file_image.read())


# file_write = open('krish.jpg', 'wb')

# for i in file_image:
#     print(file_write.write(i))


"""Check the files exists"""
# from os.path import exists as file_exists
# print(file_exists("Employees.txt"))


# from pathlib import Path

# file = Path('krish.jpg')

# if file.is_file():
#     print(f"The {file} is Exist")
# else:
#     print(f"The {file} doesn't Exist")


"""Read CSV"""
# import csv
# csv_file = open("MVP(Tables).csv", "r")
# print(csv_file.read())

# with open('Web_Security_Topics_Batch_01(Sheet1).csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line in csv_reader:
#         print(line)

# with open('Web_Security_Topics_Batch_01(Sheet1).csv', 'r') as f:
#     csv_reader = csv.reader(f)
#     for line_no, line in enumerate(csv_reader, 1):
#         if line_no == 1:
#             print('Header :')
#             print(line)
#             print('Data :')
#         else:
#             print(line)

import pypdf 

pdf_file = open('Web_Security_Topics_Batch_01.pdf', 'rb')
read = pypdf.PdfReader(pdf_file)

page = read.get_page(0)
# print(read.get_num_pages())

data = page.extract_text()
# print(data)

Name = "Sankarasathasivam Muthu Krishnan"

if Name in data:
    print(Name)
else:
    print("Not Exist")