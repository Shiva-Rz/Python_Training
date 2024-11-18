"""File Write"""

with open('write.txt', 'w') as file:
    line = "Hello \nwelcome \nI'm Shiva"

    file.write("Hi \n")
    file.writelines(line)
    file.close()

with open('write.txt', 'r+') as read_file:
    print("The Output of Read : \n")
    print(read_file.read())

    print("The Output of seek : \n")
    read_file.seek(0)

    print("The output of Readline : \n")
    print(read_file.readline()) # Reads the first line

    print("The Output of Read(9) function")
    print(read_file.read(9)) # Reads the characters upto 19

    print("The Output of Readlines function")
    print(read_file.readlines()) # Read all the leftout lines