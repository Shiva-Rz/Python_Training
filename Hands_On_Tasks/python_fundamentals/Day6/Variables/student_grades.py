# tamil, english, maths, science, social_science = map(int, input("Enter the 5 subjects marks :").split())
# print("Tamil : ",tamil)
# print("English : ",english)
# print("Maths : ",maths)
# print("Science : ",science)
# print("Social Science : ",social_science)

list = ['Tamil', 'English', 'Maths', 'Science', 'Social']

value_list = []

for subject in list:
    value = int(input(f"{subject} : "))
    value_list.append(value)

total = 0 
for index_value in range(0, len(value_list)):    
    total = total + value_list[index_value]    

average = (total) / 5
# print(average)

if(average >= 90):
    print("Grade : A")
elif(average >= 80 and average < 90):
    print("Grade : B")
elif(average >= 70 and average < 80):
    print("Grade : C")
elif(average >= 60 and average < 70):
    print("Grade : D")
else:
    print("Grade : F")
