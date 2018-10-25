

def main():
    for i in range(1, 585):
        try:
            line_num = 1
            text_num = i
            file = open('texts_UTF8/Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt', 'r',
                        encoding='utf-8')
            print('... TEXT ' + str(i) + ' OPENED...')
            lines = re.sub('[А-Я][А-Я]?.+[1-9]?: ', '', file.read()).split('\n')

if __name__ == '__main__':
    main()
