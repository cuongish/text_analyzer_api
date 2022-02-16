from app.helper import scrape_paragraph
from app.helper import count_word
from app.helper import collect_names

url = "https://en.wikipedia.org/wiki/Space_physics"

passage = scrape_paragraph(url=url)
a = count_word(passage=passage)
b = collect_names(passage=passage)


import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple's looking at buying U.K. startup for $1 billion")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)