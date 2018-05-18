import sqlite3
import re
import ast
from app import config

#db = sqlite3.connect('CW2018.db')
#print('...DataBase connected...')

base = '.+?'

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

#db.create_function("REGEXP", 2, regexp)

regexp_commnd = ''

#print(db.execute("SELECT id FROM words WHERE analysis REGEXP '.+?(,)?.+?(,)?.+?(,)?.+?(,)?'").fetchall())

#db.close()


def search_word(arg):
    print(arg)
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    print('...DataBase connected...')
    result = db.execute("SELECT * FROM words_ver3 WHERE word = " + "'" + str(arg) + "'").fetchall()
    if result == []:
        return print('...Search returned null result...')
    elif len(result) == 1:
        ids = ast.literal_eval(result[0][1])
        print(ids)
    else:
        ids = []
        for el in result:
            ids.append(ast.literal_eval(el[0][1]))
        print(ids)
    db.close()
    return ids


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
    return ids


def search_gram(args):
    db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
    print('...DataBase connected...')
    print(args.split(','))
    if args.split(',') == ['']:
        return print('...Null search...')
    cmd_line = ''
    for arg in args.split(','):
        if arg in config.pos:
            cmd_line = "WHERE gr REGEXP '^" + str(arg) + "(,|=)'" + cmd_line
            print(cmd_line)
        else:
            cmd_line += " AND gr REGEXP '(,|=)" + str(arg) + "(,|=)?'"
            print(cmd_line)

    db.create_function("REGEXP", 2, regexp)

    print(cmd_line)

    result = db.execute("SELECT id FROM words_ver3 " + cmd_line).fetchall()
    print(type(result))
    print(len(result))
    if result == []:
        return print('...Search returned null result...')
    elif len(result) == 1:
        print('JOPA')
        ids = ast.literal_eval(result[0][1])
    else:
        ids = []
        for el in result:
            print(el)
            #print(ast.literal_eval(el[1]))
            for item in ast.literal_eval(el[0]):
                ids.append(item)
        print(ids)
    db.close()
    return set(ids)
