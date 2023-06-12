import time
import unittest
from subprocess import Popen

from mondot.error import ERR_SCRIPT_FAILED
from mondot.page import Page
from tests.test_shell import TestShell


class RaiseExceptionTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/error/raise_exception.py"
        self.tmp_file = "tmp/tmp.py"
        self.process = Popen(
            f"python run.py --code-path {self.code_file} --tmp-path  {self.tmp_file}",
            shell=True,
        )

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self.process.kill()

    def test_raise_exception(self):
        time.sleep(1)

        page: Page = self._read_output(self.code_file, 0)
        self._validate_output(page)

        assert not self._output_exists(self.code_file, 1)

    def _validate_output(self, page: Page):
        assert page.error_code == ERR_SCRIPT_FAILED
        assert page.number == 0


if __name__ == "__main__":
    unittest.main()
