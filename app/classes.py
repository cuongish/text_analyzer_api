from typing import Any
from typing import List
from typing import Text
from typing import Dict
import json

from pydantic import BaseModel
from starlette.responses import Response


class PrettyJSONResponse(Response):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        return json.dumps(
            content,
            ensure_ascii=False,
            allow_nan=False,
            indent=4,
            separators=(", ", ": "),
        ).encode("utf-8")


class InputJSON(BaseModel):
    url: Text


class OutputJSON(PrettyJSONResponse):
    word_counts: Dict[Text, int]
    names: List[Text]
