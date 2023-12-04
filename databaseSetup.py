from people import Friend
from datetime import datetime
import sqlite3


def setupdb(filename: str) -> sqlite3.Connection:
    con = sqlite3.connect(filename)
    cur = con.cursor()

    # Create empty people table
    create_people_table(con, False)

    return con


def create_people_table(con, drop: bool) -> None:
    """
    Create a tbale people in connection sql db, if drop is True will drop
    the table if it already exists otherwise will not drop table.
    :param con: SQL db
    :param drop:
    """
    con.cursor()
    cur = con.cursor()
    if drop:
        cur.execute("""
            DROP IF EXISTS People CASCADE
        """)
    cur.execute("""
        CREATE TABLE People (
            id SERIAL NOT NULL,
            phone VARCHAR(15) NOT NULL,
            birthdateMonth INTEGER NOT NULL,
            birthdateDay INTEGER NOT NULL,
            message VARCHAR(511) NOT NULL,
            PRIMARY KEY (id)
        )
    """)
    con.commit()


def db_insert_friend(con: sqlite3.Connection, friend: Friend) -> int:
    """

    :param con: SQL connection to db
    :param friend:
    :return: id assigned
    """

    cur = con.cursor()
    res = cur.execute("""
        INSERT INTO People(phone, birthdateMonth, birthdateDay, message) 
        VALUES (?, ?, ?, ?) RETURNING id""",
        [friend.number, friend.month, friend.day, friend.msg])
    id = res.fetchone()[0]

    return id
