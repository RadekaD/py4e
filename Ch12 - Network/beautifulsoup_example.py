import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

text = soup("a")

for paragraph in text:
    print(text.get("href", None))