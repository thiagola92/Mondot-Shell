from typing import Callable

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection


class Runner:
    """
    Everything here can be seeing by the user code.
    """

    def __init__(self, uris: list[str], dbs: list[str], cols: list[str]):
        self.clients: list[MongoClient] = []
        self.dbs: list[Database] = []
        self.cols: list[Collection] = []

        for uri, db, col in zip(uris, dbs, cols):
            client: MongoClient = MongoClient(uri)
            self.clients.append(client)
            self.dbs.append(client[db])
            self.cols.append(client[db][col])

        # Create aliases to get the first connection
        self.client = self.clients[0]
        self.db = self.dbs[0]
        self.col = self.cols[0]

    def run(self, code: Callable):
        return code(self)
