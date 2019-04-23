from typing import List


class Member:
    def __init__(self, _id: str, avatar_url: str, full_name, username: str, id_boards:  List[str], url: str):
        self.id = _id
        self.avatar_url = avatar_url
        self.full_name = full_name
        self.username = username
        self.id_boards = id_boards
        self.url = url
