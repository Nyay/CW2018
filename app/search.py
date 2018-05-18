import sqlite3
import re
import ast
from app import config


def get_lines(args):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    print('...Lines connected...')
    result = {}
    result_2 = []
    for arg in args:
        line_id = '.'.join(arg.split('.')[:2])
        result[arg] = db.execute("SELECT Field2 FROM lines WHERE id ='" + str(line_id) + "'").fetchall()[0][0]
        result_2.append(db.execute("SELECT Field2 FROM lines WHERE id ='" + str(line_id) + "'").fetchall()[0][0])
    return result_2



def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None


def search_word(arg):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    print('...DataBase connected...')
    result = db.execute("SELECT ids FROM words_ids WHERE word = " + "'" + str(arg) + "'").fetchall()
    if result == []:
        return print('...Search returned null result...')
    elif len(result) == 1:
        ids = ast.literal_eval(result[0][0])
        print(ids)
    else:
        ids = []
        for el in result:
            ids.append(ast.literal_eval(el[0]))
        print(ids)
    db.close()
    print(get_lines(ids))
    return get_lines(set(ids))


def search_lex(arg):
    print(arg)
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    print('...DataBase connected...')
    result = db.execute("SELECT * FROM words_ver3 WHERE lex = " + "'" + str(arg) + "'").fetchall()
    if result == []:
        return print('...Search returned null result...')
    elif len(result) == 1:
        ids = ast.literal_eval(result[0][1])
    else:
        ids = []
        for el in result:
            for item in ast.literal_eval(el[1]):
                ids.append(item)
        print(ids)
    db.close()
    print(get_lines(ids))
    return get_lines(set(ids))

def search_gram(args):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    if args.split(',') == ['']:
        return print('... NOTHING FOUND ...')
    cmd_line = ''
    for arg in args.split(','):
        if arg in config.pos:
            cmd_line = "WHERE gr REGEXP '^" + str(arg) + "(,|=)'" + cmd_line
        else:
            cmd_line += " AND gr REGEXP '(,|=)" + str(arg) + "(,|=)?'"
    db.create_function("REGEXP", 2, regexp)
    result = db.execute("SELECT id FROM words_ver3 " + cmd_line).fetchall()
    if result == []:
        return print('...Search returned null result...')
    elif len(result) == 1:
        ids = ast.literal_eval(result[0][1])
    else:
        ids = []
        for el in result:
            for item in ast.literal_eval(el[0]):
                ids.append(item)
    db.close()
    return get_lines(set(ids))
