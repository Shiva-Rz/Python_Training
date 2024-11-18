# Given the below dict
# 		student_scores = {
# 		  "Harry": 81,
# 		  "Ron": 78,
# 		  "Hermione": 99, 
# 		  "Draco": 74,
# 		  "Neville": 62,
# 		}
# 		Check for keys based on the marks
# 			>90 -- Outstanding
# 			>80 -- Exceeded expectations
# 			>70 -- Acceptable
# 			Other - Have to work hard
	
# 	Output:	Your output has be a dict. Key has be the key and value should be a list of students


student_scores = {
		  "Harry": 81,
		  "Ron": 78,
		  "Hermione": 99, 
		  "Draco": 74,
		  "Neville": 62,
		}
# print(student_scores)

student_dict = {}
first = []
second = []
third = []
fourth = []

for name, mark in student_scores.items():
    if mark > 90:
        first.append({name : mark})
        # print(f"Outstanding",{name : mark})
    elif mark > 80:
        second.append({name : mark})
        # print(f"Exceeded expectations",{name : mark})
    elif mark > 70:
        third.append({name : mark})
        # print(f"Acceptable",{name : mark})
    else:
        fourth.append({name : mark})
        # print(f"Have to work hard",{name : mark})

# print(student_scores)

student_dict["Outstanding"] = first
student_dict["Exceeded expectations"] = second
student_dict["Acceptable"] = third
student_dict["Have to work hard"] = fourth

print(student_dict)