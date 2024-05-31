from complex_progress import *


class ComplexProgressCache:
    def __init__(self):
        self._cache = {}

    def remove_by(self, user_id: int):
        if user_id in self._cache.keys():
            del self._cache[user_id]

    def add(self, user_id: int, complex_progress: ComplexProgres):
        self._cache[user_id] = complex_progress

    def get_by(self, user_id: int) -> ComplexProgres:
        return self._cache[user_id]