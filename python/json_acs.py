
 s=json dumps(id)
 with open("/home/project/new_file_name","w") as f;
 f.write(s)

import json

source_file=("aalto_20072018","rU")
with open('','r') as json_file:
    data = json.load(json_file)
json_data=json.load(source_file)
value = json.dumps({'id': sorted(id, key=lambda x: x['count'])})
id.sort(key=int)
print (value)
print(id)
