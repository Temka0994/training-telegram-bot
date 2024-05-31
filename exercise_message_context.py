class MessageContext:

    def __init__(self, message_row):

        self.image = message_row[0]
        self.description = message_row[1]
        self.url = f"https://ucarecdn.com/{message_row[0]}/"
