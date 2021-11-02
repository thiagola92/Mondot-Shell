import json
from pathlib import Path
from unittest import TestCase

class TestShell(TestCase):
    def _read_output(self, code_file, page):
        output_file = f"{code_file}_{page}"

        assert Path(output_file).exists()

        with open(output_file) as f:
            return json.load(f)
    
    def _request_next_output(self, code_file):
        input_file = f"{code_file}_i"
        Path(input_file).write_text("1")
    
    def _delete_output_files(self, code_file):
        page = 1

        while Path(f"{code_file}_{page}").exists():
            Path(f"{code_file}_{page}").unlink(missing_ok=True)
            page += 1
    
    def _delete_input_file(self, code_file):
        input_file = f"{code_file}_i"
        Path(input_file).unlink(missing_ok=True)
    
    def _validate_output_format(self, output):
        assert isinstance(output, dict)
        assert "error" in output
        assert "result" in output
        assert isinstance(output["error"], bool)
        assert isinstance(output["result"], list)