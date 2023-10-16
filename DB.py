import sqlite3
from enum import Enum


class ReturnType(Enum):
    SUCCESS = True
    FAIL = False


DATABASE = "../DB.sqlite"
db = sqlite3.connect(DATABASE, check_same_thread=False)
curser = db.cursor()


def add_user(username, password, renterpassword):
    curser.execute("SELECT * FROM user WHERE username = ?", (username,))
    answer = curser.fetchall()
    if not answer and password == renterpassword:
        curser.execute("INSERT INTO user(username, password) VALUES (?, ?)", (username, password))
        db.commit()
        return ReturnType.SUCCESS
    else:
        return ReturnType.FAIL


def check_user(username, password):
    answer = curser.execute("SELECT * FROM WHERE username = ? AND password = ?", (username, password))
    if answer:
        return ReturnType.SUCCESS
    else:
        return ReturnType.FAIL






