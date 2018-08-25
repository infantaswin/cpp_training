import json
import sys

input=open(sys.argv[1])
# print(input)
json_array=json.load(input)
print(json_array)
# array={}
#
# array['name']=(json_array['name'])
# array['id']=sorted(json_array['id'])
# # print("===========================================")
# array['acronym']=(json_array['acronym'])
# array['federation']=(json_array['federation'])
# array['city']=(json_array['city'])
# array['district']=(json_array['district'])
# array['state']=(json_array['state'])
# array['country']=(json_array['country'])
#
# print(array)
#


# with open("datas.json","w") as f:
#     json.dump(array, f)
# with open(input) as f:
# array['id']=sorted(templist, key=int)

# array['name']="aswin"
# templist = [25, 50, 100, 150, 200, 250, 300, 33]
# array['id']=sorted(templist, key=int)
# print(array)
# print(json_array)
