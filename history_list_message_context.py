class HistoryListMessageContext:
    def __init__(self, history_tuples, complex_dict):
        self.description = ''
        for index, complex_tuple in enumerate(history_tuples, start=0):
            self.complex = next(key for key, value in complex_dict.items() if value == history_tuples[index][1])
            self.description += f"{index + 1}. {self.complex} - {history_tuples[index][2]}.\n"



