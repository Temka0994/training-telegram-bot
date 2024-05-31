class ExerciseDao:

    def __init__(self, conman):
        self.conman = conman

    def find_by_id(self, id):
        cursor = self.conman.current().cursor()
        cursor.execute("SELECT image_name, description "
                       "FROM exercise e "
                       "JOIN complex c "
                       "ON c.complex_id = e.complex_id "
                       "WHERE exercise_id = %s", (id, ))
        result = cursor.fetchall()
        cursor.close()
        return result


