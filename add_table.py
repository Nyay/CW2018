import sqlite3

db = sqlite3.connect('../app/CW2018.db')
db.execute('CREATE TABLE `words_ver6_v2` ( `word` TEXT, `id` TEXT, `lex` TEXT, `gr` TEXT )')

db.commit()
db.close()