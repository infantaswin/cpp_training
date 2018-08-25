import json
import Sys

input=
f = open("example", 'w')
f1 = open("sample_number.txt", 'r')


f.write(json.dumps(json.loads(f), indent=1))


f.close()
