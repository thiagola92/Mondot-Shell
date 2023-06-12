import time
import unittest
from subprocess import Popen

from test_shell import TestShell

from mondot.error import ERR_PARSE_ERROR
from mondot.page import Page


class FailParseTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/error/fail_parse.py"
        self.tmp_file = "tmp/tmp.py"
        self.process = Popen(
            f"python run.py --code-path {self.code_file} --tmp-path  {self.tmp_file}",
            shell=True,
        )

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self.process.kill()

    def test_fail_parse(self):
        time.sleep(1)

        page: Page = self._read_output(self.code_file, 0)
        self._validate_output(page)

        assert not self._output_exists(self.code_file, 1)

    def _validate_output(self, page: Page):
        assert page.error_code == ERR_PARSE_ERROR
        assert page.error_msg
        assert page.number == 0
        assert page.result == ""


if __name__ == "__main__":
    unittest.main()
