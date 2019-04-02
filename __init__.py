from mycroft import MycroftSkill, intent_file_handler


class Pastteller(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('pastteller.intent')
    def handle_pastteller(self, message):
        self.speak_dialog('pastteller')


def create_skill():
    return Pastteller()

