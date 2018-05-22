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
            output[text_out] = num
        except IndexError:
            for item in set(arg[line]):
                text[int(item.split('.')[2]) - 2] = "<b>" + str(text[int(item.split('.')[2]) - 2]) + str("</b>")
                text_out = ' '.join(text)
                num = item.split('.')[0]
            output[text_out] = num
    return output
