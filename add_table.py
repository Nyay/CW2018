import sqlite3

db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
db.execute('CREATE TABLE `words_ver6` ( `word` TEXT, `id` TEXT, `lex` TEXT, `gr` TEXT )')

db.commit()
db.close()