import json
import urllib.request, urllib.parse, urllib.error

user_input = input("Enter URL: ")
i = 0

fhand = urllib.request.urlopen(user_input).read()

data = json.loads(fhand)

for info in data.items():
    
    print(info[1][i])
    i = i + 1
