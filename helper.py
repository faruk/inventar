import sqlite3

def get_connection():
  conn = sqlite3.connect('inventar.db')
  conn.row_factory = sqlite3.Row
  c = conn.cursor()
  return conn, c

def dict_factory(cursor, row):
  d = {}
  for idx, cor in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

def get_rooms_departments_sockets(c):
  c.execute("SELECT number FROM rooms")
  rooms_result = c.fetchall()
  c.execute("SELECT name FROM departments")
  departments_result = c.fetchall()
  c.execute("SELECT number FROM sockets")
  sockets_result = c.fetchall()
  return rooms_result, departments_result, sockets_result

