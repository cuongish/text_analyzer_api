from app.helper import scrape_paragraph
from app.helper import count_word
from app.helper import collect_names

url = "https://en.wikipedia.org/wiki/Space_physics"

passage = scrape_paragraph(url=url)
a = count_word(passage=passage)
b = collect_names(passage=passage)

print(a)
print(b)
