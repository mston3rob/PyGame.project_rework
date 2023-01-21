import pygame
import datetime as dt
import sqlite3

class Player_End:
    def __init__(self):
        self.con = sqlite3.connect('DataBase_to_scores.sqlite')
        self.create_bd()

    def create_bd(self):
        cur = self.con.cursor()
        cur.execute("""create table if not exists RECORDS(
        time text,
        score integer
        )""")
        self.con.commit()
        cur.close()

    def new_score(self, score):
        self.con = sqlite3.connect('DataBase_to_scores.sqlite')
        cur = self.con.cursor()
        time = dt.datetime.now()
        cur.execute("""INSERT INTO RECORDS(time, score) 
                       VALUES (?,?);""", (time, score))
        self.con.commit()
        cur.close()

    def info(self):
        cur = self.con.cursor()
        cur.execute("""SELECT max(score) score from RECORDS
        ORDER by score DESC
        limit 5""")
        self.scores = cur.fetchall()
        cur.close()
        return self.scores


