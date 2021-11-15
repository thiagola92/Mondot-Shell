import time
from pathlib import Path
from bson import json_util

from mondot.error import Error


class Pages:
    def __init__(self, filepath, page_size):
        self._filepath = filepath
        self._page_size = page_size

        self._current_page = 1
        self._current_docs = []

        self.error = Error.OK

    def append_document(self, doc):
        self._current_docs.append(doc)

        if len(self._current_docs) >= self._page_size:
            self.write_current_page()
            self._wait_mondot_input()

    def write_current_page(self):
        # Doesn't need to write file when no document exist
        if len(self._current_docs) <= 0:
            return

        filepath = f"{self._filepath}_{self._current_page}"
        page_json = self._get_page_json(
            content={"error": self.error, "result": self._current_docs}
        )

        Path(filepath).write_text(page_json)

        self._start_new_page()

    def write_last_page(self):
        filepath = f"{self._filepath}_{self._current_page}"
        page_json = self._get_page_json(
            content={"error": Error.ERR_FILE_EOF, "result": ["No more pages"]}
        )

        Path(filepath).write_text(page_json)

    def _get_page_json(self, content):
        try:
            return self._get_json(content)
        except Exception as e:
            return self._get_json(
                {
                    "error": Error.ERR_PARSE_ERROR,
                    "result": [Error.get_exception_message()],
                }
            )

    def _get_json(self, obj):
        return json_util.dumps(
            obj, indent=2, json_options=json_util.RELAXED_JSON_OPTIONS
        )

    def _start_new_page(self):
        self._current_page += 1
        self._current_docs.clear()

    def _wait_mondot_input(self):
        filename = f"{self._filepath}_i"

        self._clean_mondot_input(filename)

        while self._read_mondot_input(filename) == "":
            time.sleep(1)

    def _clean_mondot_input(self, filename):
        with open(filename, "w") as f:
            f.write("")

    def _read_mondot_input(self, filename):
        with open(filename, "r") as f:
            return f.read()
