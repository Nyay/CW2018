import sqlite3
import re
import ast
from app import config


def get_lines(args):
    print('LINES HERE')
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    print('...Lines connected...')
    result = {}
    result_2 = []
    for arg in args:
        line_id = '.'.join(arg.split('.')[:2])
        result[arg] = db.execute("SELECT Field2 FROM lines WHERE id ='" + str(line_id) + "'").fetchall()[0][0]
        result_2.append(db.execute("SELECT Field2 FROM lines WHERE id ='" + str(line_id) + "'").fetchall()[0][0])
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


def lexgram_search(gramms, lex):

    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    db.create_function("REGEXP", 2, regexp)

    if lex != '' and gramms.split(',') != ['']:
        cmd_line = ''
        for gramm in gramms.split(','):
            if gramm in config.pos:
                cmd_line = "WHERE gr REGEXP '^" + str(gramm) + "(,|=)'" + cmd_line
            else:
                cmd_line += " AND gr REGEXP '(,|=)" + str(gramm) + "(,|=)?'"
        cmd_line += " AND lex = '" + str(lex) + "'"
        result = db.execute("SELECT id FROM words_ver3 " + cmd_line).fetchall()
        db.close()
        return get_lines(compile_ids(result, 0, 1))
    elif lex == '' and gramms.split(',') != ['']:
        cmd_line = ''
        for gramm in gramms.split(','):
            if gramm in config.pos:
                cmd_line = "WHERE gr REGEXP '^" + str(gramm) + "(,|=)'" + cmd_line
            else:
                cmd_line += " AND gr REGEXP '(,|=)" + str(gramm) + "(,|=)?'"
        result = db.execute("SELECT id FROM words_ver3 " + cmd_line).fetchall()
        db.close()
        return get_lines(compile_ids(result, 0, 1))
    elif lex != '' and gramms.split(',') == ['']:
        result = db.execute("SELECT id FROM words_ver3 WHERE lex = " + "'" + str(lex) + "'").fetchall()
        return get_lines(compile_ids(result, 0, 1))
    else:
        return []


