import argparse
import importlib.util
from pathlib import Path

from mondot.code import rewrite_user_code
from mondot.shell import Shell

# fmt: off
parser = argparse.ArgumentParser(description="Description to be used on mondot")
parser.add_argument("--input", dest="in_filepath", type=str)
parser.add_argument("--uri", dest="uri", default="mongodb://127.0.0.1:27017", action="append", type=str)
parser.add_argument("--database", dest="db", default="admin", action="append", type=str)
parser.add_argument("--page_size", dest="page_size", default="20", type=int)
parser.add_argument("--tmp", dest="tmp_filepath", default="tmp.py", type=str)
# fmt: on

args = parser.parse_args()
args = vars(args)

in_filepath: Path = Path(args["in_filepath"]).resolve()  # Absolute path
tmp_filepath: Path = Path(args["tmp_filepath"]).resolve()  # Absolute path

rewrite_user_code(input_path=in_filepath, output_path=tmp_filepath)

# Import temporary code
spec = importlib.util.spec_from_file_location("temporary_code", str(tmp_filepath))
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# Remove temporary code because it's already loaded
tmp_filepath.unlink(missing_ok=True)

Shell(
    uris=args["uri"],
    dbs=args["db"],
    filepath=str(in_filepath),
    page_size=args["page_size"],
).run(module.code)
