from collections.abc import Iterator

from mondot_shell.error import ERR_FILE_EOF
from mondot_shell.page import Page

# Prevent iterating over this types
PROTECTED_TYPES = (str, dict)


class Paginator:
    """
    Control the pagination of the user code.
    """

    def __init__(self, page_size: int):
        self._page_size = page_size

        self._current_page = 0
        self._current_docs = []

    def paginate(self, obj) -> Iterator[Page]:
        if isinstance(obj, PROTECTED_TYPES):
            yield Page(error_code=ERR_FILE_EOF, result=obj)
        elif isinstance(obj, Iterator):
            for p in self._paginate_iterator(obj):
                yield p
        else:
            yield Page(error_code=ERR_FILE_EOF, result=obj)

    def _paginate_iterator(self, obj: Iterator) -> Page:
        for item in obj:
            self._current_docs.append(item)

            if len(self._current_docs) >= self._page_size:
                yield Page(result=self._current_docs, number=self._current_page)

                # Start new page
                self._current_page += 1
                self._current_docs.clear()

        # Leftover that didn't complete a full page or an empty list
        yield Page(
            error_code=ERR_FILE_EOF,
            result=self._current_docs,
            number=self._current_page,
        )
