from flask import Flask, request
from flask_cors import cross_origin

from trello_communication.communication import communication
import requests

# from controller.board_controller import BoardController
# from controller.card_controller import CardController
# from controller.list_controller import ListController
# from controller.member_controller import MemberController

# bc = BoardController()
# cc = CardController()
# lc = ListController()
# mc = MemberController()

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


@app.route('/test', methods=["POST", "GET"])
@cross_origin()
def test():
    if request.method == "POST":
        # communication.token = request.form[]
        print(request.form)
    return "OK"


if __name__ == '__main__':
    app.run()
