import os
import json
import time
import unittest
from pathlib import Path
from unittest import TestCase


class HelloWorldTest(TestCase):
    def setUp(self):
        self.code_file = "tests/code/list/range_1_to_100.py"
        self.input_file = f"{self.code_file}_i"
        self.tmp_file = "tmp/tmp.py"

    def tearDown(self):
        Path(self.input_file).unlink(missing_ok=True)
        Path(self.tmp_file).unlink(missing_ok=True)

    def test_range_1_to_10(self):
        os.system(f"python run.py --input {self.code_file} --tmp {self.tmp_file}")

        time.sleep(1)

        output = self._read_output(1)
        self._validate_output_format(output)
        self._validate_output(output)
    
    def _validate_output(self, output):
        assert output["error"] == False
        assert len(output["result"]) == 20

        for r in output["result"]:
            assert isinstance(r, int)
    
    def _read_output(self, page):
        assert Path(self.output).exists()

        output_file = f"{self.code_file}_{page}"

        with open(output_file) as f:
            return json.load(f)
    
    def _validate_output_format(self, output):
        assert isinstance(output, dict)
        assert "error" in output
        assert "result" in output
        assert isinstance(output["error"], bool)
        assert isinstance(output["result"], list)
    
    def _request_next_output(self):
        Path(self.input_file).write_text("1")

if __name__ == "__main__":
    unittest.main()