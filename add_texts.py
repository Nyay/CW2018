import sqlite3

db = sqlite3.connect('CW2018.db')
print('...DataBase connected...')

for i in range(1, 585):
    try:
        file_name = 'Архив ВШЭ-ФЭ-69-14-2017-' + str(i) + '-utf-8.txt'
        with open(str(file_name), 'r', encoding='utf-8') as file:
            text_data = file.read()
            db.execute('INSERT INTO texts VALUES (?, ?)', (None, text_data))
            db.commit()
            print('...' + str(file_name) + ' added to DataBase...')
    except FileNotFoundError:
        continue
db.close()
print('...DataBase closed...')
