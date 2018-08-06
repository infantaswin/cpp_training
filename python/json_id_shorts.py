import json
import sys

# print(input)
array={}
input=open(sys.argv[1])
json_array=json.load(input)
# print(json_array)
array['name']=(json_array['name'])
array['id']=sorted(json_array['id'])
# print("===========================================")
array['acronym']=(json_array['acronym'])
array['federation']=(json_array['federation'])
array['city']=(json_array['city'])
array['district']=(json_array['district'])
array['state']=(json_array['state'])
array['country']=(json_array['country'])

print(array)
