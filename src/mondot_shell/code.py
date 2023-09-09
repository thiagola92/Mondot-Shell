import ast
from ast import Module
from pathlib import Path

BASE_CODE = """
def code(self):
    from bson import ObjectId  # Implicit import for the user
"""


def rewrite_user_code(input_path: Path, output_path: Path):
    user_code = ast.parse(input_path.read_text())
    base_code = ast.parse(BASE_CODE)

    _inject_inside_base_code(base_code, user_code)
    _recalculate_lines_and_columns_positions(base_code)

    output_path.write_text(ast.unparse(base_code))


def _inject_inside_base_code(base_code: Module, user_code: Module):
    function = base_code.body[0]

    # Insert all user code inside the function
    # and add a return to the last expression
    function.body.extend([exp for exp in user_code.body])

    if hasattr(function.body[-1], "value"):
        function.body[-1] = ast.Return(value=function.body[-1].value)


def _recalculate_lines_and_columns_positions(first_node: Module):
    attributes_to_remove = ["lineno", "end_lineno", "col_offset", "end_col_offset"]

    # Remove attributes so they can be recalculated
    for node in ast.walk(first_node):
        node._attributes = tuple(
            attribute
            for attribute in node._attributes
            if attribute not in attributes_to_remove
        )

    # Recalculate attributes
    ast.fix_missing_locations(first_node)
