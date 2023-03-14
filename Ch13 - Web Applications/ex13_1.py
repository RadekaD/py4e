import urllib.request, urllib.error, urllib.parse
import xml.etree.ElementTree as ET
import ssl

user_input = input("Enter location: ")

data = urllib.request.urlopen(user_input)

print("Retrieving", user_input)
data = data.read()


tree = ET.fromstring(data)
counts = tree.findall(".//count")

print(counts)
