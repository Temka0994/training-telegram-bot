class ComplexDao:

    def __init__(self, conman):
        self.conman = conman

    def find_all_exercise_by_id(self, id):
        cursor = self.conman.current().cursor()
        cursor.execute("SELECT e.exercise_name "
                       "FROM exercise e "
                       "JOIN complex c "
                       "ON c.complex_id = e.complex_id "
                       "WHERE c.complex_id = %s", (id,))
        result = cursor.fetchall()
        cursor.close()
        return result

    def find_exercise_ids_by_id(self, id):
        cursor = self.conman.current().cursor()
        cursor.execute("SELECT e.exercise_id "
                       "FROM exercise e "
                       "JOIN complex c "
                       "ON c.complex_id = e.complex_id "
                       "WHERE c.complex_id = %s", (id,))
        result = cursor.fetchall()
        cursor.close()
        result = [id for sublist in result for id in sublist]
        return result
