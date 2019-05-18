from flask import Flask, request
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


@app.route('/authorize')
def authorize():
    auth_config = (
        'callback_method=fragment',
        'return_url=http://127.0.0.1:5000/setToken',
        'scope=read,write',
        'expiration=1day',
        'name=Suggest',
        'key=dfe27ae204fc44ddaac9cd606a4527fa',
        'response_type=token'
    )
    full_auth_url = 'http://trello.com/1/authorize/?' + '&'.join(auth_config)
    return communication.authorize(full_auth_url)


if __name__ == '__main__':
    app.run()
