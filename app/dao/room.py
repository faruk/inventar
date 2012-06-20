from ..utils import get_connection

class Room:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def insert(self, data):
        assert data['name'] != ""
        assert data['id_department'] != ""
        sql = "INSERT INTO room(name, id_department) VALUE(%s, %s)"
        self.cursor.execute(sql, (data['name'], data['id_department']))

    def get_all(self):
        sql = """
            SELECT room.id, room.name, department.name
            FROM room JOIN department
            ON room.id_department = department.id
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get(self, id):
        sql = """
            SELECT room.id, room.name, room.id_department, department.name
            FROM room JOIN department
            ON room.id_department = department.id
            WHERE room.id = %s
            """
        self.cursor.execute(sql, (id))
        return self.cursor.fetchone()

    def update(self, data):
        assert data['name'] != ""
        assert data['id_department'] != ""
        assert data['id'] != ""
        sql = """
            UPDATE room SET name = %s, id_department = %s
            WHERE id = %s
            """
        self.cursor.execute(sql, (data['name'], data['id_department'], data['id']))

    def delete(self, id):
        sql = "DELETE FROM room WHERE id = %s"
        self.cursor.execute(sql, (id))

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()
