import MySQLdb
from ..config import mysql

def setup():
    return MySQLdb.connect(host = mysql['host'],
                           user = mysql['user'],
                           passwd = mysql['password'],
                           db = mysql['db'],
                           port = mysql['port'])
