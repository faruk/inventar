import sqlite3
from bottle import route, run, debug, template, request

@route('/')
def start():
  message = '''this is a project realized in python with bottle'''
  output = template('main', content = message)
  return output

@route('/hardware')
def list_hardware():
  conn = sqlite3.connect('inventar.db')
  c = conn.cursor()
  c.execute("SELECT * FROM hardwares ORDER BY zedat_number, sap_number, serial_number, buying_date")
  result = c.fetchall()
  c.close()

  output = template('make_table', rows = result, name="hardware")
  return output

@route('/hardware/new')
def new_hardware():
  if request.GET.get('save', '').strip():
    description = request.GET.get('description', '').strip()


debug(True)
run(reloader = True, port=80, host='0.0.0.0')
