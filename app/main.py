from fastapi import FastAPI, Header, HTTPException
from pydantic import validate_arguments

from app.classes import PrettyJSONResponse
from app.classes import InputJSON
from app.classes import OutputJSON
from app.helper import scrape_paragraph
from app.helper import count_word
from app.helper import collect_names

app = FastAPI()
url = "https://en.wikipedia.org/wiki/Space_physics"
fake_secret_token = "coneofsilence"


@app.get("/", response_class=PrettyJSONResponse)
async def read_root():
    passage = scrape_paragraph(url=url)

    word_counts = count_word(passage=passage)
    names = collect_names(passage=passage)

    return {"word_counts": word_counts, "names": names}


@app.put("/analyze", response_class=OutputJSON)
@validate_arguments
def text_analyze(input_json: InputJSON):
    if not input_json.url.startswith("https://"):
        raise HTTPException(status_code=404, detail="URL does not start with https//")

    passage = scrape_paragraph(url=input_json.url)

    word_counts = count_word(passage=passage)
    names = collect_names(passage=passage)

    return {"word_counts": word_counts, "names": names}
