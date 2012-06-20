from ..utils import get_connection
from ..utils.request import saved

class Department:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def insert(self, data):
        assert data['name'] != ""
        sql = "INSERT INTO department(name) VALUE('"+data['name']+"')"
        self.cursor.execute(sql)

    def get(self, id):
        sql = "SELECT id, name FROM department"
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_all(self):
        sql = "SELECT id, name FROM department"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, data):
        assert data['name'] != ""
        sql = "UPDATE department SET name = '"+data['name']+"' WHERE id = "+data['id']
        self.cursor.execute(sql)

    def delete(self, id):
        sql = "DELETE FROM department WHERE id = "+id
        self.cursor.execute(sql)

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
