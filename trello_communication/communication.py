from flask import redirect
import requests
import json
import re
from db_model.list import List
from db_model.board import Board
from busyness_calculation.busyness_calculation import BusynessCalculation


class _Communication:

    def __init__(self):
        self.base_url = "https://api.trello.com/1"
        self.token = ""
        self.user_id = ""
        self.key = "dfe27ae204fc44ddaac9cd606a4527fa"
        self.is_in_name = False

    def get_boards(self):
        return json.dumps(
            [x for x in json.loads(self._doRequest("/members/" + str(self.user_id) + "/boards")) if not x['closed']])

    def get_members_from_board(self, board_id: str):
        return self._doRequest("/boards/" + board_id + "/members")

    def get_members_form_card(self, card_id: str):
        return self._doRequest("/cards/" + card_id + "/members")

    def get_member(self, member_id: str):
        return self._doRequest("/members/" + member_id)

    def get_lists(self, board_id: str):
        b = Board[board_id]
        db_lists = List.select().where(List.board == b)
        lists_content = self._doRequest("/boards/" + board_id + "/lists")
        lists = json.loads(lists_content)

        for _list in lists:
            for db_list in db_lists:
                if _list['id'] == db_list.list_id:
                    _list['isIgnored'] = db_list.is_ignored

        return json.dumps(lists)

    def get_cards_from_board(self, board_id: str):
        return self._doRequest("/boards/" + board_id + "/cards")

    def get_cards_from_list(self, list_id: str):
        return self._doRequest("/lists/" + list_id + "/cards")

    def get_story_points_from_card(self, card_id: str):
        res = {}
        if self.is_in_name:
            storypoints = self._doRequest("/cards/" + card_id)
            card_dict = json.loads(storypoints)
            name: str = card_dict['name']

            if '(' in name and ')' in name:
                point = re.search(r'\(\d+\)', name).group(0)

                if point:
                    res['points'] = int(point[1: -1])

        else:
            storypoints = self._doRequest("/cards/" + card_id + "/pluginData")
            point_list = json.loads(storypoints)

            if len(point_list) > 0:
                point_dict = [x for x in point_list if x['idPlugin'] == '59d4ef8cfea15a55b0086614'][0]
                tmp: dict = json.loads(point_dict['value'])
                if 'points' in tmp.keys():
                    res['points'] = tmp['points']

        return json.dumps(res)

    def rearrange(self, user_json):
        return json.dumps(BusynessCalculation.calculate(json.loads(user_json['body'])))

    def ignore(self, list_json):
        list_list = list_json['lists']
        board_id = list_list[0]['idBoard']

        try:
            Board[board_id]
        except:
            Board.insert(board_id=list_list[0]['idBoard']).execute()
        board = Board[board_id]

        for _list in list_list:
            try:
                db_l = List[_list['id']]
                db_l.is_ignored = _list['isIgnored']
                db_l.save()
            except:
                List.insert(list_id=_list['id'], is_ignored=_list['isIgnored'], board=board).execute()

        return '200'

    def authorize(self, auth_url):
        return redirect(auth_url, 302)

    def _doRequest(self, url: str):
        return requests.request("GET", self.base_url + url
                                + '?key=' + str(self.key)
                                + '&token=' + str(self.token)
                                ).content


communication = _Communication()
