import sqlite3
import pandas
import re

db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
print('...DataBase connected...')

TextData = pandas.read_csv('TextsData.csv')
print('...DataFrame created...')

for i in range(1, 585):
    try:
        file_name = 'texts_UTF8/Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt'
        text_name = 'Архив ВШЭ-ФЭ-69-14-2017-' + str(i)
        data = TextData[TextData['Имя файла'] == text_name].values.tolist()
        with open(str(file_name), 'r', encoding='utf-8') as file:
            text_data = file.read()
            if 'youtube' in str(data[0][10]):
                try:
                    youtude_id = re.search('watch\?v=(.+?)&', str(data[0][10])).group(1)
                except AttributeError:
                    continue
            elif 'youtube' in str(data[0][12]):
                try:
                    youtude_id = re.search('watch\?v=(.+?)&', str(data[0][12])).group(1)
                except AttributeError:
                    continue
            else:
                youtude_id = None
            db.execute('INSERT INTO texts_plus VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (i, text_data, data[0][1], data[0][4], data[0][5],
                        data[0][6], data[0][7], data[0][9], data[0][8], youtude_id))
            db.commit()
            print('...' + str(file_name) + ' added to DataBase...')
    except FileNotFoundError:
        print('Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt')

db.close()
print('...DataBase closed...')
