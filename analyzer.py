from pymystem3 import Mystem
import re
import sqlite3

mystem = Mystem()


def main():
    db = sqlite3.connect('CW2018.db')
    print('...DataBase connected...')
    for i in range(1, 585):
        try:
            line_num = 1
            text_num = i
            file = open('Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt', 'r',
                        encoding='utf-8')
            print('... TEXT ' + str(i) + ' OPENED...')
            lines = re.sub('[А-Я][А-Я]?.+[1-9]?: ', '', file.read()).split('\n')
            for line in lines:
                data = mystem.analyze(line)
                word_num = 1
                for el in data:
                    if 'analysis' in el:
                        sim = (str(text_num) + '.' + str(line_num) + '.' + str(word_num))
                        word = el['text']
                        data = el['analysis']
                        if data == []:
                            lex = '-'
                            qual = '-'
                            gr = '-'
                        else:
                            lex = data[0]['lex']
                            try:
                                qual = data[0]['qual']
                            except:
                                qual = 'normal'
                            gr = data[0]['gr']
                        db.execute('INSERT INTO words_ver2 VALUES (?, ?, ?, ?, ?)',
                                   (str(word), str(sim), str(lex), str(qual), str(gr)))
                        db.commit()
                        word_num += 1
                line_num += 1
            print('... TEXT ' + str(i) + ' ANALYSIS COMPLETE...')
        except FileNotFoundError:
            continue
    db.close()
    print('...DataBase closed...')

if __name__ == '__main__':
    main()
