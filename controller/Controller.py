from trello_communication.communication import _Communication
from trello_communication.communication import communication as cmnct
from app import app


class Controller:
    def __init__(self):
        self.communication = cmnct
