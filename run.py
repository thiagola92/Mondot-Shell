import os
import argparse
import importlib.util
from pathlib import Path

from mondot.code import Code
from mondot.shell import Shell


parser = argparse.ArgumentParser(description="Description to be used on mondot")
parser.add_argument("--input", dest="in_filepath")
parser.add_argument("--uri", dest="uri", default="mongodb://127.0.0.1:27017")
parser.add_argument("--database", dest="db", default="admin")
parser.add_argument("--page_size", dest="page_size", default="20")
parser.add_argument("--tmp", dest="tmp_filepath", default="tmp.py")

args = parser.parse_args()
args = vars(args)
args["in_filepath"] = str(Path(args["in_filepath"]).resolve())  # Absolute path
args["tmp_filepath"] = str(Path(args["tmp_filepath"]).resolve())  # Absolute path

Code.rewrite_user_code(input_path=args["in_filepath"], output_path=args["tmp_filepath"])

# Import temporary code
spec = importlib.util.spec_from_file_location("temporary_code", args["tmp_filepath"])
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

os.remove(args["tmp_filepath"])  # Remove temporary code because it's already loaded

Shell(
    uri=args["uri"],
    db=args["db"],
    filepath=args["in_filepath"],
    page_size=args["page_size"],
).run(module.code)
