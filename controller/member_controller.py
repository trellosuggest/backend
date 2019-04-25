from flask import Blueprint
from controller.Controller import Controller
from entity.member import Member
import typing


class MemberController(Controller):
    def __init__(self):
        super().__init__()
        self.member_controller = Blueprint('member_controller', __name__)

    @self.member_controller.route("/boards/<board_id:str>/members")
    def members_from_board(self, board_id) -> typing.List[Member]:
        return communication.get_members_from_board(board_id) \


    @self.member_controller.route("/cards/<card_id:str>/members")
    def members_from_card(self, card_id) -> typing.List[Member]:
        return communication.get_members_from_card(card_id)

    @self.member_controller.route("/members/<member_id:str>")
    def member(self, member_id) -> Member:
        return communication.get_member(member_id)
