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
        user_name text UNIQUE,
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

def create_deck_table(deck_table):
    deck_connect = connect_or_create()
    deck_cursor = deck_connect.cursor()

def create_master_list():
    conn = connect_or_create()
    cu = conn.cursor()
    cu.execute("""CREATE TABLE full_card_list(
        id text,
        name text,
        supertype text,
        subtypes text,
        level text,
        hp real,
        types text,
        evolvesFrom text,
        abilities text,
        attacks text,
        nationalPokedexNumbers text,
        legalities text,
        images text,
        evolvesTo text,
        resistances text,
        rules text,
        regulationMark text)""")

    conn.commit()
    conn.close()

def create_user_deck_table(user_id):
    conn = connect_or_create()
    cu = conn.cursor()
    cu.execute(f'''CREATE TABLE {user_id}(
        deck_name text UNIQUE,
        user_id text,
        card_quantity integer,
        description text)''')
    conn.commit()
    conn.close()

def add_user(first_name, last_name, user_name):
    set_c = connect_or_create()
    s_cursor = set_c.cursor()
    table_name = "users"
    user_table = user_name + "_1"
    s_cursor.execute(f'''INSERT INTO {table_name}(
        first_name, last_name, user_name, user_table) VALUES
        (?,?,?,?)''',(first_name,last_name,user_name,user_table))
    set_c.commit()
    set_c.close()

def retrieve_users():
    conn = connect_or_create()
    cu = conn.cursor()

    cu.execute("SELECT *, oid FROM users")
    username_results = []
    all_users = cu.fetchall()
    for user in all_users:
        username_results.append(user[2])
    return username_results