from pymongo import MongoClient
from collections.abc import Iterable

from mondot.pages import Pages
from mondot.error import Error


class Shell:
    def __init__(self, uri, db, filepath, page_size):
        self.uri = uri
        self.client = MongoClient(self.uri)
        self.db = self.client[db]

        self._pages = Pages(filepath, int(page_size))

    def run(self, code):
        try:
            obj = code(self)
        except Exception as e:
            obj = Error.get_exception_message()
            self._pages.error = Error.ERR_SCRIPT_FAILED

        self._process_output(obj)

    def _process_output(self, obj):
        # Prevent iterating over this types
        if isinstance(obj, (str, dict)):
            obj = [obj]

        # Make sure that the obj is iterable at the end
        if not isinstance(obj, Iterable):
            obj = [obj]

        self._save_output(obj)

    def _save_output(self, obj):
        for doc in obj:
            self._pages.append_document(doc)
        self._pages.write_current_page()
        self._pages.write_last_page()
