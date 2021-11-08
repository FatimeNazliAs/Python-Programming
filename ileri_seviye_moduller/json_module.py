import json
person_string='{"name":"ali","languages":["python","c"]}'
# json string to dict
# result=json.loads(person_string)
# print(result["name"])

# with open ("person.json") as f:
#     data=json.load(f)
#     print(data["name"])


#   dict to json string
person_dict={"name":"ali","languages":["python","c"]}
result=json.dumps(person_dict)#dictionary jsona cevirme
print(result)
print(type(result))

# with open("person.json","w") as f:
#     json.dump(person_dict,f)

