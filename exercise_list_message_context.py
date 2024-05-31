class ExerciseListMessageContext:
    def __init__(self, complex_tuples):
        self.description = ''
        for index, complex_tuple in enumerate(complex_tuples, start=1):
            self.description += f"{index}. {complex_tuple[0]}.\n"

