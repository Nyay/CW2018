import sqlite3

db = sqlite3.connect('/Users/macbook/Desktop/CW2018/CW2018.db')
db.execute('CREATE TABLE "texts_plus" ( `id` INTEGER NOT NULL, `text` TEXT, `genre` TEXT, `location` TEXT, `respondent` TEXT, `respondent_bd` TEXT, `respondent_bp` TEXT, `correspondent` TEXT, `place_of_recording` TEXT, `youtube_id` TEXT )')

db.commit()
db.close()