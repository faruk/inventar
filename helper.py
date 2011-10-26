import sqlite3
from bottle import request

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

def GET(x):
  return request.GET.get(x, '').strip()


def delete(table, id):
  conn, c  = get_connection()
  query = "DELETE FROM "+table+" WHERE id = " +str(id)
  c.execute(query)
  conn.commit()
  c.close()

#####################
# Socket Helper
#####################
def add_socket(room):
  conn, c = get_connection()
  c.execute("SELECT number, id FROM rooms WHERE number = ?", [str(room)])
  result = c.fetchone()
  number = result['number']
  roomid = result['id']
  c.execute("INSERT INTO sockets(number, room_id) VALUES(?,?)", (number+"/1", roomid))
  c.execute("INSERT INTO sockets(number, room_id) VALUES(?,?)", (number+"/2", roomid))
  conn.commit()
  c.close()

def edit_socket(room):
  conn, c = get_connection()
  c.execute("SELECT id, number FROM rooms WHERE id = ?", [str(room)])
  result = c.fetchone()
  number = result['number']
  c.execute("SELECT id FROM sockets WHERE room_id = ?", [str(room)])
  result = c.fetchone()
  id = result['id']
  c.execute("UPDATE sockets SET number = '"+number+"/1"+"' WHERE id = "+str(id))
  c.execute("UPDATE sockets SET number = '"+number+"/2"+"' WHERE id = "+str(int(id)+1))
  conn.commit()
  c.close()

def delete_sockets(room):
  conn, c = get_connection()
  c.execute("DELETE FROM sockets WHERE room_id = ?", [str(room)])
  conn.commit()
  c.close()

