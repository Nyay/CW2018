import sqlite3
import re


def main():
    db = sqlite3.connect('CW2018.db')
    for i in range(1, 585):
        try:
            line_num = 1
            text_num = i
            file = open('Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt', 'r',
                        encoding='utf-8')
            lines = re.sub('[А-Я][А-Я]?.+[1-9]?: ', '', file.read()).split('\n')
            for line in lines:
                sim = (str(text_num) + '.' + str(line_num))
                db.execute('INSERT INTO lines VALUES (?, ?)',
                           (str(sim), str(line)))
                db.commit()
                line_num += 1
        except FileNotFoundError:
            continue
    db.close()

if __name__ == '__main__':
    main()
