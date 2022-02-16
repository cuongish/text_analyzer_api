# coding: utf-8

from typing import Dict
from typing import List
from typing import Text
from typing import Union

import spacy
from bs4 import BeautifulSoup
from collections import Counter
from urllib.request import urlopen
from spacy.tokens import Doc

nlp = spacy.load('en_core_web_sm')


def scrape_paragraph(url: Text) -> Text:
    if not url.startswith("https://"):
        raise ValueError('url does not starts with https://')
    else:
        http_response = urlopen(url)
        try:
            soup = BeautifulSoup(http_response, 'html.parser')
            elements = soup.find_all("p")
            passage: Text = ""
            for e in elements:
                passage += e.text
            return passage
        except not http_response.status == 200:
            raise AssertionError(f"Expected HTTP code 200, but got {http_response.status}")


def count_word(passage: Text) -> Dict[Text, int]:
    counter = Counter(passage.lower().split())

    return counter


def collect_names(passage: Text) -> List[Text]:
    doc: Union[Doc] = nlp(passage)
    names = []

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            names.append(ent.text)

    return names
