from app import app
from controller.Controller import Controller
from entity.card import Card
import typing


class CardController(Controller):
    def __init__(self):
        super().__init__()
        # self.card_controller = Blueprint('card_controller', __name__)

    @app.route("/lists/<list_id:str>/cards")
    def cards_from_list(self, list_id) -> typing.List[Card]:
        return self.communication.get_cards_from_list(list_id)

    @app.route("/boards/<board_id:str>/cards")
    def cards_from_board(self, board_id) -> typing.List[Card]:
        return self.communication.get_cards_from_board(board_id)
