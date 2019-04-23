import datetime
from typing import List


class Card:
    def __init__(self, _id: str, closed: bool, id_board: str, id_list: str,
                 name: str, due: datetime, id_members: List[str]):
        self._id = _id
        self.closed = closed
        self.id_board = id_board
        self.id_list = id_list
        self.name = name
        self.due = due
        self.id_members = id_members
