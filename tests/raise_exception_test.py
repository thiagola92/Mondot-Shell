import time
import unittest
from subprocess import Popen
from tests.test_shell import TestShell

from mondot.error import Error


class RaiseExceptionTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/error/raise_exception.py"
        self.tmp_file = "tmp/tmp.py"
        self.process = Popen(
            f"python run.py --input {self.code_file} --tmp {self.tmp_file}", shell=True
        )

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self.process.kill()

    def test_raise_exception(self):
        time.sleep(1)

        output = self._read_output(self.code_file, 1)
        self._validate_output_format(output)
        self._validate_output(output)
        self._validate_last_output(self.code_file, 2)

        assert not self._output_exists(self.code_file, 3)

    def _validate_output(self, output):
        assert output["error"] == Error.ERR_SCRIPT_FAILED
        assert len(output["result"]) == 1
        assert isinstance(output["result"][0], str)


if __name__ == "__main__":
    unittest.main()
