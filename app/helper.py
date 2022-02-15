from typing import Dict
from typing import List
from typing import Text

from bs4 import BeautifulSoup
from collections import Counter
from urllib.request import urlopen
import spacy


nlp = spacy.load('en_core_web_sm')


def scrape_paragraph(url: Text) -> Text:
    if not url.startswith("https://"):
        raise ValueError('url does not starts with https://')
    else:
        http_response = urlopen(url)
        soup = BeautifulSoup(http_response, 'html.parser')
        elements = soup.find_all("p")
        passage = ""
        for e in elements:
            passage += e.text
        return passage


def count_word(passage: Text) -> Dict[Text, int]:
    counter = Counter(passage.lower().split())

    return counter


def collect_names(passage: Text) -> List[Text]:
    doc = nlp(passage)
    names = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)

    return names
