import os
import json
import time
from pathlib import Path
from unittest import TestCase


class HelloWorldTest(TestCase):
    def setUp(self):
        self.input = "tests/code/range_1_to_10.py"
        self.output = "tests/code/range_1_to_10.py_1"
        self.tmp = "tmp/tmp.py"

    def test_range_1_to_10(self):
        os.system(f"python run.py --input {self.input} --tmp {self.tmp}")

        time.sleep(1)

        assert Path(self.output).exists()

        with open(self.output) as f:
            output = json.load(f)

        self._validate_output(output)

        assert output["error"] == False
        assert output["result"] == list(range(10))

    def tearDown(self):
        Path(self.output).unlink(missing_ok=True)
        Path(self.tmp).unlink(missing_ok=True)
    
    def _validate_output(self, output):
        assert isinstance(output, dict)
        assert "error" in output
        assert "result" in output
        assert isinstance(output["error"], bool)
        assert isinstance(output["result"], list)

