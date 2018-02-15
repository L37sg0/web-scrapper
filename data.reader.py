import json

file = open('images.json','r').read()
print(json.loads(file))