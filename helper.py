import sqlite3
from bottle import request

###############################
# VARIOUS HELPERS
##############################
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

##########################
# HARDWARE HELPER
##########################
def insert_hardware():
  conn, c = get_connection()
  description = GET('description')
  serial_no   = request.GET.get('serial_number', '').strip()
  sap_no      = request.GET.get('sap_number', '').strip()
  zedat_no    = request.GET.get('zedat_number', '').strip()
  billing_no  = request.GET.get('billing_number', '').strip()
  buying_date = request.GET.get('buying_date', '').strip()
  article_no  = request.GET.get('article_number', '').strip()
  other       = request.GET.get('other', '').strip()
  room        = request.GET.get('room','').strip()
  socket      = request.GET.get('socket', '').strip()
  department  = request.GET.get('department', '').strip()
  c.execute('INSERT INTO hardwares(description, serial_number, sap_number, zedat_number, billing_number, buying_date, article_number, other, room, socket, department) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (description, serial_no, sap_no, zedat_no, billing_no, buying_date, article_no, other, room, socket, department))
  conn.commit()
  c.close()

def update_hardware(id):
  conn, c = get_connection()
  description = request.GET.get('description', '').strip()
  serial_no   = request.GET.get('serial_number', '').strip()
  sap_no      = request.GET.get('sap_number', '').strip()
  zedat_no    = request.GET.get('zedat_number', '').strip()
  billing_no  = request.GET.get('billing_number', '').strip()
  buying_date = request.GET.get('buying_date', '').strip()
  article_no  = request.GET.get('article_number', '').strip()
  other       = request.GET.get('other', '').strip()
  room        = request.GET.get('room','').strip()
  socket      = request.GET.get('socket', '').strip()
  department  = request.GET.get('department', '').strip()
  query = "UPDATE hardwares SET "
  query += "description = '"+ description + "', "
  query += "serial_number = '" + serial_no + "', "
  query += "sap_number = '" + sap_no + "', "
  query += "zedat_number = '" + zedat_no + "',"
  query += "billing_number = '" + billing_no + "', "
  query += "buying_date = '" + buying_date + "', "
  query += "article_number = '" + article_no + "', "
  query += "other = '" + other + "', "
  query += "room = '" + room + "', "
  query += "socket = '"+ socket + "', "
  query += "department = '"+ department + "' "
  query += "WHERE id = " + str(id)
  print query
  c.execute (query)
  conn.commit()
  c.close()

###################
# ROOM HELPER
##################
def insert_room():
  conn, c = get_connection()
  number = helper.GET('number')
  department = helper.GET('department')
  c.execute('INSERT INTO rooms(number, department) VALUES(?,?)', (number, department))
  conn.commit()
  c.close()
  helper.add_socket(number)

def update_room(id):
  conn, c = get_connection()
  number = helper.GET('number')
  department = helper.GET('department')
  query = "UPDATE rooms SET "
  query +="number = '"+number+"', "
  query +="department = '"+department+"' "
  query +="WHERE id = "+str(id)
  c.execute(query)
  conn.commit()
  c.close()
  edit_socket(id)

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

######################
# User Helper
#####################
def insert_user():
  conn, c = get_connection()
  first_name = GET('first_name')
  last_name = GET('last_name')
  room = GET('room')
  department = GET('department')
  telephone = GET('telephone')
  query = "INSERT INTO users(first_name, last_name, room, department, telephone) "
  query+= "VALUES('"+first_name+"', '"+last_name+"', '"+room+"', '"+department+"', '"+telephone+"')"
  c.execute(query)
  conn.commit()

def update_user(id):
  conn, c = get_connection()
  first_name = GET('first_name')
  last_name = GET('last_name')
  room = GET('room')
  department = GET('department')
  telephone = GET('telephone')
  query = "UPDATE users SET "
  query+= "first_name = '"+first_name+"', "
  query+= "last_name = '"+last_name+"', "
  query+= "room = '"+room+"', "
  query+= "department = '"+department+"', "
  query+= "telephone = '"+telephone+"' "
  query+= "WHERE id ="+str(id)
  c.execute(query)
  conn.commit()

####################
# SOFTWARE HELPER
####################
def insert_software():
  conn, c = get_connection()
  query = "INSERT INTO softwares(name, license_key, buying_date,  billing_number, department, other) "
  query+= "VALUES('"+GET('name')+"', "
  query+= "'"+GET('license_key')+"', "
  query+= "'"+GET('buying_date')+"', "
  query+= "'"+GET('billing_number')+"', "
  query+= "'"+GET('department')+"', "
  query+= "'"+GET('other')+"')"
  c.execute(query)
  conn.commit()
  c.close()

def update_software(id):
  conn, c = get_connection()
  query = "UPDATE softwares SET "
  query+= "name = '"+GET('name')+"', "
  query+= "license_key = '"+GET('license_key')+"', "
  query+= "buying_date = '"+GET('buying_date')+"', "
  query+= "billing_number = '"+GET('billing_number')+"', "
  query+= "department = '"+GET('department')+"', "
  query+= "other = '"+GET('other')+"' "
  query+= "WHERE id = "+str(id)
  c.execute(query)
  conn.commit()
