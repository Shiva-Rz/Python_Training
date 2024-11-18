first_list = [10, 30, 43, 50]
second_list = [20, 20, 20, 20, 20]
third_list = [30, 30, 30, 30]
# value = 0

value_list = []

# for index in first_list:
#     value = value + index
#     print(index)

# print("The sum of list :",value)

# print(sum(first_list))

# for index in range(0, len(first_list)):
#     value_list.append(first_list[index] + second_list[index] + third_list[index])
    
# value_list = [first_list[i] + second_list[i] for i in range(len(first_list))]

for i in range(len(first_list)):
    value_list.append(first_list[i] + second_list[i])   

print(value_list)