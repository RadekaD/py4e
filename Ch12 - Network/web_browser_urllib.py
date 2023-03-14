import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("https://www.fpn.bg.ac.rs/48062")
for line in fhand:
    print(line.decode().strip())