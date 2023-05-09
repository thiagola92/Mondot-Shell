from typing import Callable

from pymongo import MongoClient
from pymongo.database import Database


class Runner:
    """
    Everything here can be seeing by the user code.
    """

    def __init__(self, uris: list[str], dbs: list[str]):
        self.clients: list[MongoClient] = []
        self.dbs: list[Database] = []

        for uri, db in zip(uris, dbs):
            client: MongoClient = MongoClient(uri)
            self.clients.append(client)
            self.dbs.append(client[db])

        # Create aliases to get the first connection
        self.client = self.clients[0]
        self.db = self.dbs[0]

    def run(self, code: Callable):
        return code(self)
