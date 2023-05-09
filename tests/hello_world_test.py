import time
import unittest
from subprocess import Popen

from mondot.error import ERR_FILE_EOF
from mondot.page import Page
from tests.test_shell import TestShell


class HelloWorldTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/none/hello_world.py"
        self.tmp_file = "tmp/tmp.py"
        self.process = Popen(
            f"python run.py --input {self.code_file} --tmp {self.tmp_file}", shell=True
        )

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self.process.kill()

    def test_hello_world(self):
        time.sleep(1)

        page: Page = self._read_output(self.code_file, 1)
        self._validate_output(page)

        assert not self._output_exists(self.code_file, 2)

    def _validate_output(self, page):
        assert page.error_code == ERR_FILE_EOF
        assert page.number == 1
        assert page.result == None


if __name__ == "__main__":
    unittest.main()
