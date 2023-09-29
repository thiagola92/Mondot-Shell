import time
import unittest
from subprocess import Popen

from test_shell import TestShell

from mondot_shell.error import ERR_FILE_EOF, OK
from mondot_shell.page import Page


class HelloWorldTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/iterator/range_iterator_1_to_100.py"
        self.tmp_file = "tmp/tmp.py"
        self.process = Popen(
            f"python run.py --code-path {self.code_file} --tmp-path  {self.tmp_file}",
            shell=True,
        )

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self._delete_input_file(self.code_file)
        self.process.kill()

    def test_range_1_to_100(self):
        time.sleep(1)

        for x in [0, 1, 2, 3, 4, 5]:
            page: Page = self._read_output(self.code_file, x)
            self._validate_output(page, x)
            self._request_next_output(self.code_file)

        assert not self._output_exists(self.code_file, 6)

    def _validate_output(self, page: Page, number: int):
        assert page.error_code in (ERR_FILE_EOF, OK)
        assert len(page.result) == 20 or len(page.result) == 0
        assert page.number == number


if __name__ == "__main__":
    unittest.main()
