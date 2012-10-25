from bottle import route, template, static_file, run, debug, request, redirect, FlupFCGIServer
from app.dao.department import Department
from app.dao.room import Room
from app.dao.hardware import Hardware
from app.dao.software import Software
from app.dao.user import User
from app.utils.request import *

@route('/')
def index():
    return template("welcome")


### HARDWARE ROUTES

@route('/hardware/new')
def hardware_new():
    if saved(request.GET):
        dao = Hardware()
        dao.insert(request.GET)
        redirect('/hardware/all')
    else:
        return template("hardware/new", rooms=Room().get_all(), 
            departments=Department().get_all(), users=User().get_all())

@route('/hardware/edit/:id')
def hardware_edit(id):
    if saved(request.GET):
        Hardware().update(request.GET)
        redirect('/hardware/all')
    print Hardware().get(id)
    return template("hardware/edit", hardware=Hardware().get(id), rooms=Room().get_all(),
        departments = Department().get_all(), users = User().get_all())

@route('/hardware/delete/:id')
def hardware_delete(id):
    Hardware().delete(id)
    redirect('/hardware/all')

@route('/hardware/all')
def hardware_all():
    return template("hardware/all", hardwares = Hardware().get_all())


### SOFTWARE ROUTES

@route('/software/new')
def software_new():
    if saved(request.GET):
        Software().insert(request.GET)
        redirect('/software/all')
    else:
        return template("software/new", departments = Department().get_all())

@route('/software/edit/:id')
def software_edit(id):
    if saved(request.GET):
        Software().update(request.GET)
        redirect("/software/all")
    else:
        return template("software/edit", software = Software().get(id),
            departments = Department().get_all())

@route('/software/delete/:id')
def software_delete():
    Software().delete(id)
    redirect('/software/all')

@route('/software/all')
def software_all():
    return template("software/all", softwares = Software().get_all())


### ROOM ROUTES

@route('/room/new')
def room_new():
    if saved(request.GET):
        dao = Room()
        dao.insert(request.GET)
        redirect('/room/all')
    else:
        dao = Department()
        return template("room/new", departments = dao.get_all())

@route('/room/edit/:id')
def room_edit(id):
    dao = Room()
    if saved(request.GET):
        dao.update(request.GET)
        redirect('/room/all')
    else:
        return template("room/edit", room = dao.get(id), departments = Department().get_all())

@route('/room/delete/:id')
def room_delete(id):
    Room().delete(id)
    redirect('/room/all')

@route('/room/all')
def room_all():
    dao = Room()
    return template("room/all", rooms = dao.get_all())


### USER ROUTES

@route('/user/new')
def user_new():
    if saved(request.GET):
        User().insert(request.GET)
        redirect('/user/all')
    else:
        return template("user/new", departments = Department().get_all())

@route('/user/edit/:id')
def user_edit(id):
    if saved(request.GET):
        User().update(request.GET)
        redirect('/user/all')
    else:
        return template("user/edit", user = User.get(id), departments = Department().get_all())

@route('/user/delete/:id')
def user_delete(id):
    User().delete(id)
    redirect('/user/all')

@route('/user/all')
def user_all():
    dao = User()
    return template("user/all", users = dao.get_all())


### DEPARTMENT ROUTES

@route('/department/new')
def department_new():
    if saved(request.GET):
        dao = Department()
        dao.insert(request.GET)
        redirect('/department/all')
    else:
        return template("department/new")

@route('/department/edit/:id')
def department_edit(id):
    dao = Department()
    if saved(request.GET):
        dao.update(request.GET)
        redirect('/department/all')
    else:
        return template("department/edit", department = dao.get(id))

@route('/department/delete/:id')
def department_delete(id):
    dao = Department()
    dao.delete(id)
    redirect('/department/all')

@route('/department/all')
def department_all():
    dao = Department()
    return template("department/all", departments = dao.get_all())


### OTHER

@route('/css/<path:path:path>')
def css(path):
    return static_file(path, root='./css')

@route('/js/<path:path:path>')
def js(path):
    return static_file(path, root='./js')

@route('/images/<path:path:path>')
def images(path):
    return static_file(path, root='./images')

@route('/img/<path:path:path>')
def img(path):
    return static_file(path, root='./images')

#debug(True)
#run(host='localhost', port='8888', reloader=True)
debug(True)
run(server = FlupFCGIServer, port=10000, host="127.0.0.1")

