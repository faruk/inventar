from ..utils import get_connection

class User:
    def __init__(self):
        self.conn = get_connection.setup()
        self.cursor = self.conn.cursor()

    def insert(self, data):
        if data['forename'] == "":
            data['forename'] == None
        if data['lastname'] == "":
            data['lastname'] == None
        if data['username'] == "":
            data['username'] == None
        assert data['id_department'] != ""
        sql = """
            INSERT INTO user (forename, lastname, username, id_department)
            VALUES (%s, %s, %s, %s)
            """
        self.cursor.execute(sql, (data['forename'], data['lastname'], data['username'],
            data['id_department']))

    def update(self, data):
        if data['forename'] == "":
            data['forename'] == None
        if data['lastname'] == "":
            data['lastname'] == None
        if data['username'] == "":
            data['username'] == None
        assert data['id_department'] != ""

        sql = """
            UPDATE user
            SET forename = %s, lastname = %s, username = %s, id_department = %s
            WHERE id = %s
            """
        self.cursor.execute(sql, (data['forename'], data['lastname'], data['username'],
            data['id_department'], data['id']))

    def delete(self, id):
        sql = "DELETE FROM user WHERE id = %s"
        self.cursor.execute(sql, (id))
        
    def get(self, id):
        sql = """
            SELECT user.id, user.forename, user.lastname, user.username, user.id_department,
                department.name
            FROM user JOIN department ON user.id_department = department.id
            WHERE user.id = %s
            """
        self.cursor.execute(sql, (id))
        return self.cursor.fetchone()

    def get_all(self):
        sql = """
            SELECT user.id, forename, lastname, username, department.name 
            FROM user JOIN department ON user.id_department = department.id
            """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __del__(self):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()

        
