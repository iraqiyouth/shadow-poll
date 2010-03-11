from UserDict import UserDict
from apps.poll.messages import FINAL_APPRECIATION_MESSAGE,TRIGGER_INCORRECT_MESSAGE

class Responders(UserDict):
    pass

class Responder(object) :
    def __init__(self,kwargs):
        self.trigger = kwargs.get("trigger","poll")
        self.parsers = kwargs.get("parsers", [])
        self.user = kwargs.get("user", None)
        self.next_question =  kwargs.get("next_question", None)
        self.session = kwargs.get("session", None)


    def proceed_to_next_question(self):
        self.session.question = self.next_question
