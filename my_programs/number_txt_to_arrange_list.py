import json
import sys
import re




array={}
input=open(sys.argv[1])
# print(input)
# f = open("exrray)
example=[]
for num in input:
    n="{}".format(num.strip())
    example.append(n)
# print(example)
number=sorted(example)
print(number)
