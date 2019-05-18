from controller.Controller import Controller
from entity.board import Board
import typing


class BoardController(Controller):
    def __init__(self):
        super().__init__()
        # self.board_controller = Blueprint('board_controller', __name__)

    @app.route("/boards")
    def boards(self) -> typing.List[Board]:
        return communication.get_boards()
