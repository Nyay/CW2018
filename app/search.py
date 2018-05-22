import sqlite3
import re
import ast
from app import config


def get_lines_2(args):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    db.create_function("REGEXP", 2, regexp)
    result = {}
    for arg in args:
        line_id = '.'.join(arg.split('.')[:2])
        line = db.execute("SELECT Field2 FROM lines WHERE id ='" + str(line_id) + "'").fetchall()[0][0]
        if line in result:
            result[line].append(arg)
        else:
            result[line] = [arg]
    return result


def get_lines(args):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    result = {}
    result_2 = []
    for arg in args:
        line_id = '.'.join(arg.split('.')[:2])
        result[arg] = db.execute("SELECT Field2 FROM lines2 WHERE id ='" + str(line_id) + "'").fetchall()[0][0]
        if result[arg] in result_2:
            continue
        else:
            result_2.append(result[arg])
    return result_2


def compile_ids(ids, index_y, index_x):
    if ids == []:
        return ids
    elif len(ids) == 1:
        result = ast.literal_eval(ids[index_y][index_x])
    else:
        result = []
        for el in ids:
            for item in ast.literal_eval(el[index_y]):
                result.append(item)
    return result


def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


def func_name(ids_1, ids_2, num):
    result = []
    for el in ids_1:
        el_list = el.split('.')
        el_list[2] = str(int(el_list[2]) + num)
        if '.'.join(el_list) in ids_2:
            result.append('.'.join(el_list))
            result.append(el)
    return result


def search_word(arg):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    result = db.execute("SELECT ids FROM words_ids WHERE word = " + "'" + str(arg) + "'").fetchall()
    if result == []:
        return []
    elif len(result) == 1:
        ids = ast.literal_eval(result[0][0])
    else:
        ids = []
        for el in result:
            ids.append(ast.literal_eval(el[0]))
    db.close()
    return ids


def lexgram_search(gramms, lex):

    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    db.create_function("REGEXP", 2, regexp)

    if lex != '' and gramms.split(',') != ['']:
        cmd_line = ''
        for gramm in gramms.split(','):
            if gramm in config.pos:
                cmd_line = " gr REGEXP '^" + str(gramm) + "(,|=)'" + cmd_line
            else:
                cmd_line += " AND gr REGEXP '(,|=)" + str(gramm) + "(,|=)?'"
        cmd_line += " AND lex = '" + str(lex) + "'"
        if cmd_line.startswith(' AND ') is True:
            cmd_line = cmd_line.strip(' AND ')
        result = db.execute("SELECT id FROM words_ver6 WHERE " + cmd_line).fetchall()
        db.close()
        return compile_ids(result, 0, 1)
    elif lex == '' and gramms.split(',') != ['']:
        cmd_line = ''
        for gramm in gramms.split(','):
            if gramm in config.pos:
                cmd_line = " gr REGEXP '^" + str(gramm) + "(,|=)'" + cmd_line
            else:
                cmd_line += " AND gr REGEXP '(,|=)" + str(gramm) + "(,|=)?'"
        if cmd_line.startswith(' AND ') is True:
            cmd_line = cmd_line.strip(' AND ')
        result = db.execute("SELECT id FROM words_ver6 WHERE " + cmd_line).fetchall()
        db.close()
        return compile_ids(result, 0, 1)
    elif lex != '' and gramms.split(',') == ['']:
        result = db.execute("SELECT id FROM words_ver6 WHERE lex = " + "'" + str(lex) + "'").fetchall()
        return compile_ids(result, 0, 1)
    else:
        return []


def get_text(arg):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    data = db.execute("SELECT * FROM texts WHERE id ='" + str(arg) + "'")
    return data