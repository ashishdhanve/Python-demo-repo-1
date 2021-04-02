import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

img = urllib.request.urlopen("http://data.pr4e.org/cover.jpg").read()
fhand = open("cover.jpg","wb")
fhand.write(img)
fhand.close()

fhand1 = urllib.request.urlopen('http://data.pr4e.org/')
soup = BeautifulSoup(fhand1, 'html.parser')

for l in soup:
    print(l)