import sqlite3
from flask import g
from enum import Enum


class ReturnType(Enum):
    SUCCESS = True
    FAIL = False


DATABASE = "DB.sqlite"
db = sqlite3.connect(DATABASE)
curser = db.cursor()


def add_user(username, password, renterpassword):
    curser.execute("SELECT * FROM user WHERE username = ?", ("test",))
    answer = curser.fetchall()
    print(answer)
    if not answer and password == renterpassword:
        curser.execute("INSERT INTO user(username, password) VALUES (?, ?)", ("test", "test"))
        db.commit()
        return ReturnType.SUCCESS
    else:
        return ReturnType.FAIL
