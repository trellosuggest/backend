from app import app
from controller.Controller import Controller
from entity.list import List
import typing


class ListController(Controller):
    def __init__(self):
        super().__init__()
        # self.list_controller = Blueprint('list_controller', __name__)

    @app.route("/boards/<board_id:str>/lists")
    def lists(self, board_id) -> typing.List[List]:
        return self.communication.get_lists(board_id)
