if __name__ == "__main__":
    pass
import sqlite3
import json
import re
from config import ROOT_DIR
import os

def connect_or_create():
    dbaseFile = os.path.join(ROOT_DIR,'databases','deckmanager.db')
    connection = sqlite3.connect(dbaseFile)
    #cursor_c = connection.cursor()
    return connection

def create_user_table(user):
    user_c = connect_or_create()
    u_cursor = user_c.cursor()
    u_cursor.execute("""CREATE TABLE users (
        first_name text,
        last_name text,
        user_name text,
        user_table text
    )""")
    user_c.commit()
    user_c.close()

def create_set_table():
    set_c = connect_or_create()
    s_cursor = set_c.cursor()
    table_name = "sets"
    s_cursor.execute(f"""CREATE TABLE {table_name} (
        set_name text,
        user_name text,
        description text
    )""")
    set_c.commit()
    set_c.close()