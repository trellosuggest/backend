from flask import redirect
import requests
import typing
import json
from entity.board import Board
from entity.list import List
from entity.card import Card
from entity.member import Member


class _Communication:

    def __init__(self):
        self.base_url = "https://api.trello.com/1"
        self.token = ""
        self.user_id = ""
        self.key = "dfe27ae204fc44ddaac9cd606a4527fa"

    def get_boards(self) -> typing.List[Board]:
        return json.dumps(
            [x for x in json.loads(self._doRequest("/members/" + str(self.user_id) + "/boards")) if not x['closed']])

    def get_members_from_board(self, board_id: str) -> typing.List[Member]:
        return self._doRequest("/boards/" + board_id + "/members")

    def get_members_form_card(self, card_id: str) -> typing.List[Member]:
        return self._doRequest("/cards/" + card_id + "/members")

    def get_member(self, member_id: str) -> typing.List[Member]:
        return self._doRequest("/members/" + member_id)

    def get_lists(self, board_id: str) -> typing.List[List]:
        return self._doRequest("/boards/" + board_id + "/lists")

    def get_cards_from_board(self, board_id: str) -> typing.List[Card]:
        return self._doRequest("/boards/" + board_id + "/cards")

    def get_cards_from_list(self, list_id: str) -> typing.List[Card]:
        return self._doRequest("/lists/" + list_id + "/cards")

    def get_story_points_from_card(self, card_id: str):
        return self._doRequest("/cards/" + card_id + "/pluginData")

    def authorize(self, auth_url):
        return redirect(auth_url, 302)

    def _doRequest(self, url: str):
        return requests.request("GET", self.base_url + url
                                + '?key=' + str(self.key)
                                + '&token=' + str(self.token)
                                ).content


communication = _Communication()




