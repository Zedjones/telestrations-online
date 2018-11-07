import os
import psycopg2

PASSWD_FILE = os.path.join(os.path.dirname(__file__), "password")

PASSWD = open(PASSWD_FILE).read()

CONN_STR = "host='traphouse.us'" \
           " dbname='draw_it_together'" \
           " user='drawsite'" \
           " password='{}'".format(PASSWD) 

def connect():
    return psycopg2.connect(CONN_STR)

def db_add_user(user_id, user):
    insert_str = "INSERT INTO users (id, name)\n" \
                 "  VALUES ('{}', '{}');".format(user_id, user)
    conn = connect()
    cur = conn.cursor()
    cur.execute(insert_str)
    conn.commit()
    cur.close()

def db_clear_table(table):
    conn = connect()
    cur = conn.cursor()
    cur.execute('DELETE FROM {}'.format(table))
    conn.commit()
    cur.close()

def db_check_for_name(name):
    conn = connect()
    cur = conn.cursor()
    select_str = "SELECT name \n" \
                 "  FROM users \n" \
                 "  WHERE name = '{}'".format(name)
    cur.execute(select_str)
    return cur.fetchone() is not None