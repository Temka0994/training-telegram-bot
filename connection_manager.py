from mysql.connector import connect


class ConnectionManager:
    def __init__(self):
        self.connection = connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='telebot_db')

    def current(self):
        return self.connection

    def close(self):
        self.connection.close()
