import time
from collections.abc import Callable
from pathlib import Path

from mondot.error import ERR_SCRIPT_FAILED, get_exception_message
from mondot.page import Page
from mondot.paginator import Paginator
from mondot.runner import Runner

INPUT_SUFFIX = "in"
OUTPUT_SUFFIX = "out"


class Shell:
    """
    Responsible for the communication with Mondot (input & output).
    """

    def __init__(self, uris: list[str], dbs: list[str], filepath: str, page_size: int):
        self._filepath = filepath
        self._runner: Runner = Runner(uris, dbs)
        self._paginator: Paginator = Paginator(page_size)

    def run(self, code: Callable):
        try:
            obj = self._runner.run(code)
        except Exception:
            return self._write_output(
                Page(
                    error_code=ERR_SCRIPT_FAILED,
                    error_msg=get_exception_message(),
                )
            )

        for page in self._paginator.paginate(obj):
            self._write_output(page)

            # Any error should abort pagination
            if page.error_code:
                break

            self._read_input()

    def _write_output(self, page: Page):
        page_json = page.to_json()
        filepath = f"{self._filepath}_{OUTPUT_SUFFIX}_{page.number}"

        Path(filepath).write_text(page_json)

    def _read_input(self):
        filepath = f"{self._filepath}_{INPUT_SUFFIX}"

        # Clear previous input
        Path(filepath).write_text("")

        # Wait new input
        while Path(filepath).read_text() == "":
            time.sleep(1)
