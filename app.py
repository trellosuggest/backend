from flask import Flask
from controller.board_controller import BoardController
from controller.card_controller import CardController
from controller.list_controller import ListController
from controller.member_controller import MemberController

bc = BoardController()
cc = CardController()
lc = ListController()
mc = MemberController()

app = Flask(__name__)
app.register_blueprint(bc.board_controller, mc.member_controller,
                       lc.list_controller, cc.card_controller)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
