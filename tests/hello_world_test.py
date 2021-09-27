import os
import json
import time
import unittest
from pathlib import Path
from unittest import TestCase


class HelloWorldTest(TestCase):
    def setUp(self):
        self.input = "tests/code/hello_world.py"
        self.output = "tests/code/hello_world.py_1"
        self.tmp = "tmp/tmp.py"

    def test_hello_world(self):
        os.system(f"python run.py --input {self.input} --tmp {self.tmp}")

        time.sleep(1)

        assert Path(self.output).exists()

        with open(self.output) as f:
            output = json.load(f)

        self._validate_output(output)

        assert output["error"] == False
        assert output["result"][0] == None

    def tearDown(self):
        Path(self.output).unlink(missing_ok=True)
        Path(self.tmp).unlink(missing_ok=True)
    
    def _validate_output(self, output):
        assert isinstance(output, dict)
        assert "error" in output
        assert "result" in output
        assert isinstance(output["error"], bool)
        assert isinstance(output["result"], list)

if __name__ == "__main__":
    unittest.main()