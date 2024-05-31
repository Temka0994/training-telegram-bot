class HistoryDao:

    def __init__(self, conman):
        self.conman = conman

    def save(self, user_id, complex_id, date):
        cursor = self.conman.current().cursor()
        cursor.execute("INSERT INTO history "
                       "(user_id, complex_id, date)"
                       "VALUES"
                       "(%s, %s, %s)", (user_id, complex_id, date))
        self.conman.current().commit()
        cursor.close()

    def find_by_id(self, user_id):
        cursor = self.conman.current().cursor()
        cursor.execute("SELECT h.user_id, h.complex_id, h.date "
                       "FROM history h "
                       "JOIN complex c "
                       "ON h.complex_id = c.complex_id "
                       "WHERE h.user_id = %s", (user_id,))
        result = cursor.fetchall()
        cursor.close()
        return result
