from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://en.wikipedia.org/wiki/Space_physics'

html = urlopen(url)

soup = BeautifulSoup(html, 'html.parser')

elements = soup.find_all("p")


counts = dict()

word_list = []
for element in elements:
    word_list += element.text.split()

for word in word_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
