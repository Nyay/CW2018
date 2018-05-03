for i in range(1, 585):
    try:
        file = open('/Users/macbook/Desktop/CW2018/texts/Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '.txt', 'r',
                    encoding='UTF-8')
        text = file.read()
        file2 = open('Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt', 'w', encoding='utf-8')
        file2.write(text)
    except UnicodeDecodeError:
        file = open('/Users/macbook/Desktop/CW2018/texts/Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '.txt', 'r',
                    encoding='cp1251')
        text = file.read()
        file2 = open('Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt', 'w', encoding='utf-8')
        file2.write(text)
    except FileNotFoundError:
        continue
