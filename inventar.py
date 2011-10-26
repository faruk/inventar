import sqlite3
from bottle import route, run, debug, template, request, static_file, validate, redirect
import helper

server = "http://lo-tek.de"

@route('/')
def start():
  message = '''this is a project realized in python with bottle'''
  output = template('main', content = message)
  return output

################
# Hardware Part
###############

#List all Hardware
@route('/hardware')
def list_hardware():
  conn, c = helper.get_connection()
  c.execute("SELECT zedat_number, sap_number, buying_date, id FROM hardwares ORDER BY zedat_number, sap_number, serial_number, buying_date")
  result = c.fetchall()
  c.close()

  output = template('show_hardwares', rows = result, name="hardware")
  return output

@route('/hardware/new', method='GET')
def new_hardware():
  conn, c = helper.get_connection()
  if request.GET.get('save', '').strip():
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
    c.execute('INSERT INTO hardwares(description, serial_number, sap_number, zedat_number, billing_number, buying_date, article_number, other, room, socket, department) VALUES (?,?,?,?,?,?,?,?,?,?,?)', (description, serial_no, sap_no, zedat_no, billing_no, buying_date, article_no, other, room, socket, department))
    conn.commit()
    c.close()
    redirect(server + "/hardware/new")
  else:
    r, d, s = helper.get_rooms_departments_sockets(c)
    c.close()
    # pass the rooms, departments and sockets    
    return template('new_hardware.tpl', rooms = r, departments = d, sockets = s)

@route('/hardware/:id', method="GET")
@validate(id=int)
def edit_hardware(id):
  conn, c = helper.get_connection()
  if request.GET.get('save', '').strip():
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
    c.execute (query)
    conn.commit()
    c.close()
    redirect(server + "/hardware/"+str(id))
  else:
    c.execute("SELECT * FROM hardwares WHERE id = ?", [id])
    result = c.fetchone()
    r, d, s = helper.get_rooms_departments_sockets(c)
    c.close()
    return template('show_hardware', id = id, row = result, rooms = r, departments = d, sockets = s )

@route('/hardware/delete/:id', method = "GET")
@validate(id=int)
def delete_hardware(id):
  helper.delete('hardwares', id)
  redirect(server + "/hardware")

###########################
# Department Section
#
@route('/department')
def list_departments():
  conn, c = helper.get_connection()
  c.execute("SELECT name, id FROM departments")
  result = c.fetchall()
  return template('show_departments', rows = result, name = "departments")

@route('/department/new')
def new_department():
  conn,c = helper.get_connection()
  if request.GET.get('save', '').strip():
    nam = request.GET.get('name', '').strip()
    c.execute('INSERT INTO departments(name) VALUES(?)', [nam])
    conn.commit()
    c.close()
    redirect(server + "/department/new")
  else:
    c.close()
    return template('new_department.tpl')

@route('/department/:id', method="GET")
@validate(id=int)
def edit_department(id):
  conn, c =helper.get_connection()
  if request.GET.get('save', '').strip():
    name = request.GET.get('name', '').strip()
    c.execute('UPDATE department SET name = ? WHERE id = ?', (name, id))
    conn.commit()
    c.close()
    redirect(server + "/department/"+str(id))
  else:
    c.execute("SELECT * FROM departments WHERE id = ?", [id])
    result = c.fetchone()
    return template('show_department', id=id, row = result)

@route('/department/delete/:id', method="GET")
@validate(id=int)
def delete_department(id):
  helper.delete('departments', id)
  redirect(server+"/department")

#############################
# ROOM SECTION
#
@route('/room')
def list_rooms():
  conn, c = helper.get_connection()
  c.execute("SELECT number, department, id FROM rooms")
  result = c.fetchall()
  c.close()
  return template('show_rooms', rows = result, name = "rooms")

@route('/room/new')
def new_room():
  conn, c = helper.get_connection()
  if request.GET.get('save', '').strip():
    number = helper.GET('number')
    department = helper.GET('department')
    c.execute('INSERT INTO rooms(number, department) VALUES(?,?)', (number, department))
    conn.commit()
    c.close()
    helper.add_socket(number)
    redirect(server + '/room')
  else:
    c.execute('SELECT name FROM departments')
    d = c.fetchall()
    c.close()
    return template('new_room', departments = d)

@route('/room/:id', method="GET")
@validate(id=int)
def edit_room(id):
  conn, c = helper.get_connection()
  if helper.GET('save'):
    number = helper.GET('number')
    department = helper.GET('department')
    query = "UPDATE rooms SET "
    query +="number = '"+number+"', "
    query +="department = '"+department+"' "
    query +="WHERE id = "+str(id)
    c.execute(query)
    conn.commit()
    helper.edit_socket(id)
    redirect(server+"/room/"+str(id))
  else:
    c.execute('SELECT * FROM rooms WHERE id = ?', [str(id)])
    r = c.fetchone()
    c.execute('SELECT name FROM departments')
    d = c.fetchall()
    return template('show_room', room = r, departments = d)

@route('/room/delete/:id', method="GET")
@validate(id=int)
def delete_room(id):
  helper.delete('rooms', id)
  helper.delete_sockets(id)
  redirect(server + "/room")


@route('/js/css/smoothness/jquery-ui-1.8.16.custom.css')
def serve_jquery_ui_css():
  static_file('/js/css/smoothness/jquery-ui-1.8.16.custom.css', root='.', mimetype='text/css')

@route('/js/ui/jquery-ui-1.8.16.custom.js')
def serve_jquery_ui():
  static_file('/js/ui/jquery-ui-1.8.16.custom.js', root = '.', mimetype='text/javascript')

@route('/js/ui/jquery.ui.widget.js')
def serve_jquery_ui_widget():
  static_file('/js/ui/jquery.ui.widget.js', root = '.', mimetype='text/javascript')

@route('/js/ui/jquery.ui.datepicker.js')
def server_jquery_ui_datepicker():
  static_file('/js/ui/jquery.ui.datepicker.js', root='.', mimetype='text/javascript')

debug(True)
run(reloader = True, port=80, host='0.0.0.0')
