'''Given two lists, both having String elements, write a python program using python lists to create a new string 
as per the rule given below:'''
	# 1. The first element in list_one should be merged with last element in list_two, 
    # second element in list_one should be merged with second last element in list_two and so on. 
	
    # 2. If an element in list_one / list_two is None, then the corresponding element in the other list 
	# should be kept as it is in the merged list.
 
#  “An apple a day keeps the doctor away”

list_one = ['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list_two = ['y','tor','e','eps','ay',None,'le','n']

list_two.reverse()

total_list = []

for index in range(len(list_one)):
    if list_one[index] == None:
        total_list.append(list_two[index])
    elif list_two[index] == None:
        total_list.append(list_one[index])
    else:
        total_list.append(list_one[index] + list_two[index])

sentence = " ".join(total_list)
print(sentence)        