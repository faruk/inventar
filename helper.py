import sqlite3

def get_connection():
  conn = sqlite3.connect('inventar.db')
  c = conn.cursor()
  return conn, c
