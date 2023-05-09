from dataclasses import dataclass
from typing import Self

from bson import json_util

from mondot.error import ERR_PARSE_ERROR, get_exception_message


@dataclass
class Page:
    error_code: int = 0
    error_msg: str = ""
    result: str = ""
    number: int = 1

    def from_json(text: str) -> Self:
        d: dict = json_util.loads(text)

        return Page(**d)

    def to_json(self) -> str:
        page_dict = self.to_dict()

        try:
            return json_util.dumps(
                page_dict,
                indent=2,
                json_options=json_util.RELAXED_JSON_OPTIONS,
            )
        except Exception:
            page = Page(
                error_code=ERR_PARSE_ERROR,
                error_msg=get_exception_message(),
                number=self.number,
            ).to_dict()

            return json_util.dumps(
                page,
                indent=2,
                json_options=json_util.RELAXED_JSON_OPTIONS,
            )

    def to_dict(self) -> dict:
        return {
            "error_code": self.error_code,
            "error_msg": self.error_msg,
            "result": self.result,
            "number": self.number,
        }
