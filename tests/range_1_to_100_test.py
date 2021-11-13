import time
import unittest
from subprocess import Popen
from tests.test_shell import TestShell


class HelloWorldTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/list/range_1_to_100.py"
        self.tmp_file = "tmp/tmp.py"
        self.process = Popen(
            f"python run.py --input {self.code_file} --tmp {self.tmp_file}", shell=True
        )

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self._delete_input_file(self.code_file)
        self.process.kill()

    def test_range_1_to_10(self):
        time.sleep(1)

        for i in [1, 2, 3, 4, 5]:
            output = self._read_output(self.code_file, i)
            self._validate_output_format(output)
            self._validate_output(output)
            self._request_next_output(self.code_file)
            time.sleep(1)

        self._validate_last_output(self.code_file, 6)

        assert not self._output_exists(self.code_file, 7)

    def _validate_output(self, output):
        assert output["error"] == False
        assert len(output["result"]) == 20

        for r in output["result"]:
            assert isinstance(r, int)


if __name__ == "__main__":
    unittest.main()
