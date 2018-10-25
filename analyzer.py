from pymystem3 import Mystem
import re
import sqlite3

mystem = Mystem()


def main():
    db = sqlite3.connect('../app/CW2018.db')
    print('...DataBase connected...')
    output = {}
    for i in range(1, 585):
        try:
            line_num = 1
            text_num = i
            file = open('texts_UTF8/Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt', 'r',
                        encoding='utf-8')
            print('... TEXT ' + str(i) + ' OPENED...')
            lines = re.sub('[А-Я][А-Я]?.+[1-9]?: ', '', file.read()).split('\n')
            for line in lines:
                data = mystem.analyze(line)
                word_num = 1
                for el in data:
                    print(el)
                    if 'analysis' in el:
                        sim = (str(text_num) + '.' + str(line_num) + '.' + str(word_num))
                        word = el['text'].lower()
                        data = el['analysis']
                        if data == []:
                            lex = '-'
                            gr = '-'
                        else:
                            lex = data[0]['lex']
                            gr = data[0]['gr']
                        if '|' in gr:
                            items = re.search('(.+?)=\((.+?)\)', gr)
                            front = items.group(1)
                            for item in items.group(2).split('|'):
                                gr = front + ',' + item
                                token = str(word) + str(gr)
                                if token in output:
                                    output[token][1].append(str(sim))
                                else:
                                    output[token] = [str(word), [str(sim)], str(lex), str(gr)]
                        else:
                            token = str(word) + str(gr)
                            if token in output:
                                output[token][1].append(str(sim))
                            else:
                                output[token] = [str(word), [str(sim)], str(lex), str(gr)]
                        word_num += 1
                    elif ' - ' in el['text'] or ' – ' in el['text'] or ' - ' in el['text']:
                        word_num += 1
                line_num += 1
            print('... TEXT ' + str(i) + ' ANALYSIS COMPLETE...')
        except FileNotFoundError:
            continue
    for el in output:
        db.execute('INSERT INTO words_ver6_v2 VALUES (?, ?, ?, ?)', (str(output[el][0]), str(output[el][1]),
                                                                 str(output[el][2]), str(output[el][3])))
        db.commit()
    db.close()
    print('...DataBase closed...')

if __name__ == '__main__':
    main()
