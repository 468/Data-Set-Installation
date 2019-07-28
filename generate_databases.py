import sqlite3

db_path = './visits.sqlite'
con = sqlite3.connect(db_path)
cursor = con.cursor()
cursor.execute('''
    CREATE TABLE visits(id INTEGER PRIMARY KEY, visit_count INTEGER, happy_visit_count INTEGER, sad_visit_count INTEGER, surprise_visit_count INTEGER, neutral_visit_count INTEGER, disgust_visit_count INTEGER, fear_visit_count INTEGER, angry_visit_count INTEGER,
    					total_visit_duration INTEGER, total_visit_duration_happy_sessions INTEGER, total_visit_duration_sad_sessions INTEGER,total_visit_duration_surprise_sessions INTEGER, total_visit_duration_neutral_sessions INTEGER, total_visit_duration_disgust_sessions INTEGER,total_visit_duration_fear_sessions INTEGER,total_visit_duration_angry_sessions INTEGER,
                    	total_average_visit_duration INTEGER, total_average_visit_duration_happy_sessions INTEGER, total_average_visit_duration_sad_sessions INTEGER,total_average_visit_duration_surprise_sessions INTEGER, total_average_visit_duration_neutral_sessions INTEGER, total_average_visit_duration_disgust_sessions INTEGER,total_average_visit_duration_fear_sessions INTEGER,total_average_visit_duration_angry_sessions INTEGER)
''')

cursor.execute('''INSERT INTO visits(visit_count, happy_visit_count, sad_visit_count, surprise_visit_count, neutral_visit_count, disgust_visit_count, fear_visit_count, angry_visit_count, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
print('Visits database created, row inserted')
cursor.execute('''SELECT visit_count FROM visits''')
visit_count = cursor.fetchone()[0] #retrieve the first row
print(visit_count) #Print the first column retrieved(user's name)
con.commit()

audio_db_path = './audio.sqlite'
audio_con = sqlite3.connect(audio_db_path)
audio_cursor = audio_con.cursor()
audio_cursor.execute('''
    CREATE TABLE audio(id INTEGER PRIMARY KEY, filename STRING, total_display_count INTEGER, happy_triggers INTEGER, sad_triggers INTEGER, surprise_triggers INTEGER, neutral_triggers INTEGER, disgust_triggers INTEGER, fear_triggers INTEGER, angry_triggers INTEGER,
    					total_visit_duration INTEGER, total_visit_duration_happy_sessions INTEGER, total_visit_duration_sad_sessions INTEGER,total_visit_duration_surprise_sessions INTEGER, total_visit_duration_neutral_sessions INTEGER, total_visit_duration_disgust_sessions INTEGER,total_visit_duration_fear_sessions INTEGER,total_visit_duration_angry_sessions INTEGER,
                    	total_average_visit_duration INTEGER, total_average_visit_duration_happy_sessions INTEGER, total_average_visit_duration_sad_sessions INTEGER,total_average_visit_duration_surprise_sessions INTEGER, total_average_visit_duration_neutral_sessions INTEGER, total_average_visit_duration_disgust_sessions INTEGER,total_average_visit_duration_fear_sessions INTEGER,total_average_visit_duration_angry_sessions INTEGER)
''')

print('Audio database created')

audio_con.commit()

video_db_path = './video.sqlite'
video_con = sqlite3.connect(video_db_path)
video_cursor = video_con.cursor()
video_cursor.execute('''
    CREATE TABLE video(id INTEGER PRIMARY KEY, filename STRING, total_display_count INTEGER, happy_triggers INTEGER, sad_triggers INTEGER, surprise_triggers INTEGER, neutral_triggers INTEGER, disgust_triggers INTEGER, fear_triggers INTEGER, angry_triggers INTEGER,
    					total_visit_duration INTEGER, total_visit_duration_happy_sessions INTEGER, total_visit_duration_sad_sessions INTEGER,total_visit_duration_surprise_sessions INTEGER, total_visit_duration_neutral_sessions INTEGER, total_visit_duration_disgust_sessions INTEGER,total_visit_duration_fear_sessions INTEGER,total_visit_duration_angry_sessions INTEGER,
                    	total_average_visit_duration INTEGER, total_average_visit_duration_happy_sessions INTEGER, total_average_visit_duration_sad_sessions INTEGER,total_average_visit_duration_surprise_sessions INTEGER, total_average_visit_duration_neutral_sessions INTEGER, total_average_visit_duration_disgust_sessions INTEGER,total_average_visit_duration_fear_sessions INTEGER,total_average_visit_duration_angry_sessions INTEGER)
''')

print('Video database created')

video_con.commit()

bulb_db_path = './bulb.sqlite'
bulb_con = sqlite3.connect(bulb_db_path)
bulb_cursor = bulb_con.cursor()
bulb_cursor.execute('''
    CREATE TABLE bulb(id INTEGER PRIMARY KEY, properties STRING, total_display_count INTEGER, happy_triggers INTEGER, sad_triggers INTEGER, surprise_triggers INTEGER, neutral_triggers INTEGER, disgust_triggers INTEGER, fear_triggers INTEGER, angry_triggers INTEGER,
    					total_visit_duration INTEGER, total_visit_duration_happy_sessions INTEGER, total_visit_duration_sad_sessions INTEGER,total_visit_duration_surprise_sessions INTEGER, total_visit_duration_neutral_sessions INTEGER, total_visit_duration_disgust_sessions INTEGER,total_visit_duration_fear_sessions INTEGER,total_visit_duration_angry_sessions INTEGER,
                    	total_average_visit_duration INTEGER, total_average_visit_duration_happy_sessions INTEGER, total_average_visit_duration_sad_sessions INTEGER,total_average_visit_duration_surprise_sessions INTEGER, total_average_visit_duration_neutral_sessions INTEGER, total_average_visit_duration_disgust_sessions INTEGER,total_average_visit_duration_fear_sessions INTEGER,total_average_visit_duration_angry_sessions INTEGER)
''')

print('Bulb database created')

bulb_con.commit()

scent_db_path = './scent.sqlite'
scent_con = sqlite3.connect(scent_db_path)
scent_cursor = scent_con.cursor()
scent_cursor.execute('''
    CREATE TABLE scent(id INTEGER PRIMARY KEY, properties STRING, total_display_count INTEGER, happy_triggers INTEGER, sad_triggers INTEGER, surprise_triggers INTEGER, neutral_triggers INTEGER, disgust_triggers INTEGER, fear_triggers INTEGER, angry_triggers INTEGER,
    					total_visit_duration INTEGER, total_visit_duration_happy_sessions INTEGER, total_visit_duration_sad_sessions INTEGER,total_visit_duration_surprise_sessions INTEGER, total_visit_duration_neutral_sessions INTEGER, total_visit_duration_disgust_sessions INTEGER,total_visit_duration_fear_sessions INTEGER,total_visit_duration_angry_sessions INTEGER,
                    	total_average_visit_duration INTEGER, total_average_visit_duration_happy_sessions INTEGER, total_average_visit_duration_sad_sessions INTEGER,total_average_visit_duration_surprise_sessions INTEGER, total_average_visit_duration_neutral_sessions INTEGER, total_average_visit_duration_disgust_sessions INTEGER,total_average_visit_duration_fear_sessions INTEGER,total_average_visit_duration_angry_sessions INTEGER)
''')

print('Scent database created')

scent_con.commit()

photo_db_path = './photo.sqlite'
photo_con = sqlite3.connect(photo_db_path)
photo_cursor = photo_con.cursor()
photo_cursor.execute('''
    CREATE TABLE photo(id INTEGER PRIMARY KEY, filename STRING, total_display_count INTEGER, happy_triggers INTEGER, sad_triggers INTEGER, surprise_triggers INTEGER, neutral_triggers INTEGER, disgust_triggers INTEGER, fear_triggers INTEGER, angry_triggers INTEGER,
    					total_visit_duration INTEGER, total_visit_duration_happy_sessions INTEGER, total_visit_duration_sad_sessions INTEGER,total_visit_duration_surprise_sessions INTEGER, total_visit_duration_neutral_sessions INTEGER, total_visit_duration_disgust_sessions INTEGER,total_visit_duration_fear_sessions INTEGER,total_visit_duration_angry_sessions INTEGER,
                    	total_average_visit_duration INTEGER, total_average_visit_duration_happy_sessions INTEGER, total_average_visit_duration_sad_sessions INTEGER,total_average_visit_duration_surprise_sessions INTEGER, total_average_visit_duration_neutral_sessions INTEGER, total_average_visit_duration_disgust_sessions INTEGER,total_average_visit_duration_fear_sessions INTEGER,total_average_visit_duration_angry_sessions INTEGER)
''')

print('Photo database created')

photo_con.commit()