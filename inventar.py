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
#
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
  if request.GET.get('save', '').strip():
    helper.insert_hardware()
    redirect(server + "/hardware/new")
  else:
    conn, c = helper.get_connection()
    r, d, s = helper.get_rooms_departments_sockets(c)
    c.close()
    return template('new_hardware.tpl', rooms = r, departments = d, sockets = s)

@route('/hardware/:id', method="GET")
@validate(id=int)
def edit_hardware(id):
  if request.GET.get('save', '').strip():
    helper.update_hardware(id)
    redirect(server + "/hardware/"+str(id))
  else:
    conn, c = helper.get_connection()
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
  if request.GET.get('save', '').strip():
    helper.insert_room()
    redirect(server + '/room')
  else:
    conn, c = helper.get_connection()
    c.execute('SELECT name FROM departments')
    d = c.fetchall()
    c.close()
    return template('new_room', departments = d)

@route('/room/:id', method="GET")
@validate(id=int)
def edit_room(id):
  if helper.GET('save'):
    helper.update_room(id)
    redirect(server+"/room/"+str(id))
  else:
    conn, c = helper.get_connection()
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

######################
# USER SECTION
#
@route('/user')
def list_users():
  conn, c = helper.get_connection()
  c.execute('SELECT * FROM users')
  result = c.fetchall()
  c.close()
  return template('show_users', rows = result)

@route('/user/new', method="GET")
def new_user():
  if helper.GET('save'):
    helper.insert_user()
    redirect(server + "/user")
  else:
    conn, c = helper.get_connection()
    c.execute("SELECT * FROM departments")
    d = c.fetchall()
    c.execute("SELECT * FROM rooms")
    r = c.fetchall()
    return template('new_user', departments = d, rooms = r)

@route('/user/:id', method="GET")
@validate(id=int)
def edit_user(id):
  if helper.GET('save'):
    helper.update_user(id)
    redirect(server + "/user/"+str(id))
  else:
    conn, c = helper.get_connection()
    c.execute("SELECT * FROM users WHERE id = "+str(id))
    result = c.fetchone()
    c.execute("SELECT * FROM departments")
    d = c.fetchall()
    c.execute("SELECT * FROM rooms")
    r = c.fetchall()
    c.close()
    return template('show_user.tpl', user = result, rooms=r, departments = d)

@route('/user/delete/:id', method="GET")
@validate(id=int)
def delete_user(id):
  helper.delete('users', id)
  redirect(server+"/user")

######################
# SOFTWARE PART
#
@route('/software')
def list_software():
  conn, c = helper.get_connection()
  c.execute("SELECT * FROM softwares")
  result = c.fetchall()
  c.close()
  return template('show_softwares.tpl', rows = result)

@route('/software/new', method="GET")
def new_software():
  if helper.GET('save'):
    helper.insert_software()
    redirect(server+"/software")
  else:
    conn, c = helper.get_connection()
    c.execute("SELECT * FROM departments")
    d = c.fetchall()
    c.close()
    return template('new_software.tpl', departments = d)

@route('/software/:id', method="GET")
@validate(id = int)
def edit_software(id):
  if helper.GET('save'):
    helper.update_software(id)
    redirect(server+"/software/"+str(id))
  else:
    conn, c = helper.get_connection()
    c.execute("SELECT * FROM departments")
    d = c.fetchall()
    c.execute("SELECT * FROM softwares WHERE id = "+str(id))
    sw = c.fetchone()
    c.close()
    return template('show_software', software = sw, departments = d)

@route('/software/delete/:id', method="GET")
@validate(id = int)
def delete_software(id):
  helper.delete('softwares', id)
  redirect(server+"/software")

######################
# SOFTWARE-USER PART
#
@route('/software/user')
def show_software_user_assignment():
  conn, c = helper.get_connection()
  c.execute('SELECT u.first_name, u.last_name, s.name, su.id, u.id, s.id FROM users u, softwares s, software_user su WHERE u.id = su.user_id AND s.id = su.software_id')
  result = c.fetchall()
  return template('show_software_user.tpl', rows = result)

@route('/software/user/new', method = "GET")
def new_software_user_assignment():
  conn, c = helper.get_connection()
  if helper.GET('save'):
    user_id = helper.GET('user_id')
    software_id = helper.GET('software_id')
    c.execute('INSERT INTO software_user(software_id, user_id) VALUES(?,?)', (software_id, user_id))
    conn.commit()
    c.close()
    redirect(server + "/software/user")
  else:
    c.execute('SELECT * FROM users')
    u = c.fetchall()
    c.execute('SELECT * FROM softwares')
    s = c.fetchall()
    c.close()
    return template('new_software_user.tpl', users = u, softwares = s)

#####################################################################
# STATIC HELPER PART
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
