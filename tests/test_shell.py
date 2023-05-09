import time
from pathlib import Path
from unittest import TestCase

from mondot.page import Page
from mondot.shell import INPUT_SUFFIX, OUTPUT_SUFFIX


class TestShell(TestCase):
    def _read_output(self, code_file, page) -> Page:
        output_file: str = f"{code_file}_{OUTPUT_SUFFIX}_{page}"
        output: str = Path(output_file).read_text()

        return Page.from_json(output)

    def _output_exists(self, code_file, page) -> bool:
        output_file = f"{code_file}_{OUTPUT_SUFFIX}_{page}"
        return Path(output_file).exists()

    def _request_next_output(self, code_file):
        input_file = f"{code_file}_{INPUT_SUFFIX}"
        Path(input_file).write_text("1")
        time.sleep(1)

    def _delete_output_files(self, code_file):
        page = 1

        while Path(f"{code_file}_{OUTPUT_SUFFIX}_{page}").exists():
            Path(f"{code_file}_{OUTPUT_SUFFIX}_{page}").unlink(missing_ok=True)
            page += 1

    def _delete_input_file(self, code_file):
        input_file = f"{code_file}_{INPUT_SUFFIX}"
        Path(input_file).unlink(missing_ok=True)
