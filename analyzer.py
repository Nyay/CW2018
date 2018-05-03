from pymystem3 import Mystem
import re

mystem = Mystem()

output = open('analyzer.txt', 'w', encoding='UTF-8')


def main():
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
                        yield str(text_num) + '.' + str(line_num) + '.' + str(word_num) + ' ' + str(el)
                        word_num += 1
                line_num += 1
            print('... TEXT ' + str(i) + ' ANALYSIS COMPLETE...')
        except FileNotFoundError:
            continue

output.write('\n'.join(main()))
