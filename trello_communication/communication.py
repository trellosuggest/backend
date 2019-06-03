from flask import redirect
import requests
import typing
import json
import re
from entity.board import Board
from entity.list import List
from entity.card import Card
from entity.member import Member


class _Communication:

    def __init__(self):
        self.base_url = "https://api.trello.com/1"
        self.token = ""
        self.user_id = ""
        self.is_in_name = False

    def get_boards(self) -> typing.List[Board]:
        return requests.request("GET", self.base_url + "/members/" + str(self.user_id) + "/boards").content

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
        return requests.request("GET", self.base_url + "/lists/" + list_id + "/cards").content

    def get_story_points_from_card(self, card_id: str):
        res = {}
        if self.is_in_name:
            storypoints = requests.request("GET", self.base_url + "/cards/" + card_id).content
            card_dict = json.loads(storypoints)
            name: str = card_dict['name']

            if '(' in name and ')' in name:
                point = re.search(r'\(\d+\)', name).group(0)

                if point:
                    res['points'] = int(point[1: -1])

        else:
            storypoints = requests.request("GET", self.base_url + "/cards/" + card_id + "/pluginData").content
            point_list = json.loads(storypoints)

            if len(point_list) != 0:
                point_dict = [x for x in point_list if x['idPlugin'] == '59d4ef8cfea15a55b0086614'][0]
                res['points'] = int(json.loads(point_dict['value'])['points'])

        return json.dumps(res)

    def authorize(self, auth_url):
        return redirect(auth_url, 302)


communication = _Communication()
