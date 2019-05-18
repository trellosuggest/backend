from flask import redirect
import requests
import typing
from entity.board import Board
from entity.list import List
from entity.card import Card
from entity.member import Member


class _Communication:

    def __init__(self):
        self.base_url = "https://api.trello.com/1"
        self.current_user = Member("user44594125", "", "", "", list(), "")  # MOCK

    def get_boards(self) -> typing.List[Board]:
        return requests.request("GET", self.base_url + "/members/" + str(self.current_user.id) + "/boards").content

    def get_members_from_board(self, board_id: str) -> typing.List[Member]:
        return requests.request("GET", self.base_url + "/boards/" + board_id + "/members").content

    def get_members_form_card(self, card_id: str) -> typing.List[Member]:
        return requests.request("GET", self.base_url + "/cards/" + card_id + "/members").content

    def get_member(self, member_id: str) -> typing.List[Member]:
        return requests.request("GET", self.base_url + "/members/" + member_id).content

    def get_lists(self, board_id: str) -> typing.List[List]:
        return requests.request("GET", self.base_url + "/boards/" + board_id + "/lists").content

    def get_cards_from_board(self, board_id: str) -> typing.List[Card]:
        return requests.request("GET", self.base_url + "/boards/" + board_id + "/cards").content

    def get_cards_from_list(self, list_id: str) -> typing.List[Card]:
        return requests.request("GET", self.base_url + "/boards/" + list_id + "/cards").content

    def authorize(self, auth_url):
        return redirect(auth_url, 302)


communication = _Communication()




