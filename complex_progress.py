class ComplexProgres:
    def __init__(self, exercise_list, complex_id):
        self._exercise_index = 0
        self._exercise_list = exercise_list
        self._complex_id = complex_id

    def skip_current_exercise(self):
        if len(self._exercise_list) != 0:
            self._exercise_index += 1
            if self._exercise_index >= len(self._exercise_list):
                self._exercise_index = 0
            return True
        else:
            return False

    def current_exercise(self):
        if self._exercise_index < len(self._exercise_list):
            return self._exercise_list[self._exercise_index]
        else:
            raise IndexError('The list is empty, you can\'t get the value')

    def complete_current_exercise(self):
        if self._exercise_index < len(self._exercise_list):
            self._exercise_list.pop(self._exercise_index)
            self._exercise_index = 0
            return len(self._exercise_list) > 0
        else:
            return False

    def get_complex_id(self):
        return self._complex_id
