import typing

from flask import Flask, request
from flask_cors import cross_origin

from entity.board import Board
from entity.card import Card
from entity.list import List
from entity.member import Member
from trello_communication.communication import communication
import requests

app = Flask(__name__)


# @app.route('/authorize')
# def authorize():
#     auth_config = (
#         'callback_method=fragment',
#         'return_url=http://' + request.remote_addr,
#         'scope=read,write',
#         'expiration=1day',
#         'name=TrelloSuggest',
#         'key=dfe27ae204fc44ddaac9cd606a4527fa',
#         'response_type=token'
#     )
#     full_auth_url = 'http://trello.com/1/authorize/?' + '&'.join(auth_config)
#     return communication.authorize(full_auth_url)


@app.route('/token', methods=["POST"])
@cross_origin()
def token():
    if request.method == "POST":
        communication.token = request.json['token']
        communication.user_id = request.json['user_id']
        print('Token: ' + communication.token)
        print('UserId: ' + communication.user_id)
        return '200'
    print('/token misstake')
    return '405'


@app.route("/boards")
@cross_origin()
def boards() -> typing.List[Board]:
    return communication.get_boards()


@app.route("/lists/<string:list_id>/cards")
@cross_origin()
def cards_from_list(list_id) -> typing.List[Card]:
    return communication.get_cards_from_list(list_id)


@app.route("/boards/<string:board_id>/cards")
@cross_origin()
def cards_from_board(board_id) -> typing.List[Card]:
    return communication.get_cards_from_board(board_id)


@app.route("/boards/<string:board_id>/lists")
@cross_origin()
def lists(board_id) -> typing.List[List]:
    return communication.get_lists(board_id)


@app.route("/boards/<string:board_id>/members")
@cross_origin()
def members_from_board(board_id) -> typing.List[Member]:
    return communication.get_members_from_board(board_id)


@app.route("/cards/<string:card_id>/members")
@cross_origin()
def members_from_card(card_id) -> typing.List[Member]:
    return communication.get_members_from_card(card_id)


@app.route("/members/<string:member_id>")
@cross_origin()
def member(member_id) -> Member:
    return communication.get_member(member_id)


@app.route("/cards/<string:card_id>/storyPoints")
@cross_origin()
def story_points_from_card(card_id):
    return communication.get_story_points_from_card(card_id)


if __name__ == '__main__':
    app.debug = True
    app.run()
