from controller.Controller import Controller
from entity.list import List
import typing


class ListController(Controller):
    def __init__(self):
        super().__init__()
        # self.list_controller = Blueprint('list_controller', __name__)

    @app.route("/lists")
    def lists(self) -> typing.List[List]:
        return communication.get_lists()
