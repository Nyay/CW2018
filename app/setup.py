from app import search
import sqlite3
import re


def setup_line(arg):
    output = {}
    for line in arg:
        text = line.split()
        try:
            for item in set(arg[line]):
                text[int(item.split('.')[2]) - 1] = "<b>" + str(text[int(item.split('.')[2]) - 1]) + str("</b>")
                text_out = ' '.join(text)
                num = item.split('.')[0]
                conn = sqlite3.connect('/home/dtatarinov/folklore_corpus/app/CW2018.db')
                data = conn.execute("SELECT genre, respondent_bd FROM texts_plus WHERE id ='" + num + "'").fetchall()
                line = "<i>[" + str(data[0][0]) + ", (" + str(data[0][1]) + str(")]</i>")
            output[text_out] = [line, num]
        except IndexError:
            continue
    return output
