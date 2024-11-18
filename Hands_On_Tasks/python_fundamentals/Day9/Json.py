import json

data = {
    "name" : "Shiva",
    "age" : 20,
    1 : "Java",
    2.0 : "Python" }


json_string = json.dumps(data, indent = 3)
print(json_string)


# with open('json_data.json', 'w') as json_file:
#     json.dump(data, json_file)
    
# with open('json_data.json', 'r') as read_json:
#     print(json.load(read_json))

print(json.loads(json_string))