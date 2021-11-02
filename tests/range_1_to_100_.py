import os
import time
import unittest
from tests.test_shell import TestShell


class HelloWorldTest(TestShell):
    def setUp(self):
        self.code_file = "tests/code/list/range_1_to_100.py"
        self.tmp_file = "tmp/tmp.py"

    def tearDown(self):
        self._delete_output_files(self.code_file)
        self._delete_input_file(self.code_file)

    def test_range_1_to_10(self):
        os.system(f"python run.py --input {self.code_file} --tmp {self.tmp_file}")

        time.sleep(1)

        output = self._read_output(self.code_file, 1)
        self._validate_output_format(output)
        self._validate_output(output)
    
    def _validate_output(self, output):
        assert output["error"] == False
        assert len(output["result"]) == 20

        for r in output["result"]:
            assert isinstance(r, int)

if __name__ == "__main__":
    unittest.main()