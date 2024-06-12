import json, sys
jsonfile = sys.argv[1]
jsonkey = sys.argv[2]
with open(jsonfile, 'r') as myfile:
    data = myfile.read()
obj = json.loads(data)
print (str(obj[jsonkey]))