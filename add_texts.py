import sqlite3
import pandas

db = sqlite3.connect('CW2018.db')
print('...DataBase connected...')

TextData = pandas.read_csv('TextsData.csv')
print('...DataFrame created...')

for i in range(1, 585):
    try:
        file_name = 'Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt'
        text_name = 'Архив ВШЭ-ФЭ-69-14-2017-' + str(i)
        data = TextData[TextData['Имя файла'] == text_name].values.tolist()
        with open(str(file_name), 'r', encoding='utf-8') as file:
            text_data = file.read()
            db.execute('INSERT INTO texts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                       (i, text_data, data[0][1], data[0][4], data[0][5],
                        data[0][6], data[0][7], data[0][9], data[0][8]))
            db.commit()
            print('...' + str(file_name) + ' added to DataBase...')
    except FileNotFoundError:
        print('Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt')

db.close()
print('...DataBase closed...')
