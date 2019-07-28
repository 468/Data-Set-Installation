import vlc
import time
import sqlite3
import numpy as numpy
import random
import os

audio_db_path = './audio.sqlite'
audio_db_con = sqlite3.connect(audio_db_path)
audio_db_cursor = audio_db_con.cursor()

Instance2 = vlc.Instance('--fullscreen --input-repeat=-1')
player2 = Instance2.media_player_new()

vlc.PlaybackMode(1) #loop

def update_audio_entry(filename, dominant_emotion_recorded, visit_duration):

	print("UPDATING AUDIO ENTRY FROM WITHIN AUDIO TEST")

	audio_db_cursor.execute('''SELECT id FROM audio WHERE filename = ?''',(filename,))
	row = audio_db_cursor.fetchone()
	print('ROW COUNT:::')
	print(row)

	if row is None:
		print ("It Does Not Exist, creating filename data")
		if(dominant_emotion_recorded=='happy'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,1,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0))
		elif(dominant_emotion_recorded=='sad'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,1,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0))
		elif(dominant_emotion_recorded=='surprise'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,1,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0))
		elif(dominant_emotion_recorded=='neutral'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,1,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0))
		elif(dominant_emotion_recorded=='disgust'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,1,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0))
		elif(dominant_emotion_recorded=='fear'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,0,1,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0))
		elif(dominant_emotion_recorded=='angry'):
			audio_db_cursor.execute('''INSERT INTO audio(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,0,0,1,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration))
	else:
		print('It exists, updating this filename data')
		filename_id = row[0]
		#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
		audio_db_cursor.execute('''SELECT total_display_count FROM audio WHERE id=?''',(filename_id,))
		current_display_count_for_file = audio_db_cursor.fetchone()[0]

		audio_db_cursor.execute('''SELECT ''' + dominant_emotion_recorded + '''_triggers FROM audio WHERE id=?''',(filename_id,))
		current_mood_triggers_for_file = audio_db_cursor.fetchone()[0]

		audio_db_cursor.execute('''SELECT total_visit_duration FROM audio WHERE id=?''',(filename_id,))
		current_total_visit_duration_for_file = audio_db_cursor.fetchone()[0]

		audio_db_cursor.execute('''SELECT total_average_visit_duration FROM audio WHERE id=?''',(filename_id,))
		current_total_average_visit_duration_for_file = audio_db_cursor.fetchone()[0]
		
		audio_db_cursor.execute('''SELECT total_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM audio WHERE id=?''',(filename_id,))
		current_total_mood_visit_duration_for_file = audio_db_cursor.fetchone()[0]

		audio_db_cursor.execute('''SELECT total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM audio WHERE id=?''',(filename_id,))
		current_total_mood_average_visit_duration_for_file = audio_db_cursor.fetchone()[0]

		new_display_count_for_file = current_display_count_for_file + 1
		new_mood_triggers_for_file = current_mood_triggers_for_file + 1
		new_total_visit_duration_for_file = current_total_visit_duration_for_file + visit_duration
		new_average_visit_duration_for_file = new_total_visit_duration_for_file / new_display_count_for_file
		new_total_mood_visit_duration_for_file = current_total_mood_visit_duration_for_file + visit_duration
		new_average_mood_visit_duration_for_file = new_total_mood_visit_duration_for_file / new_mood_triggers_for_file

		audio_db_cursor.execute('''UPDATE audio SET total_display_count = ? WHERE id = ?''',(new_display_count_for_file, filename_id))
		audio_db_cursor.execute('''UPDATE audio SET ''' + dominant_emotion_recorded + '''_triggers = ? WHERE id = ?''',(new_mood_triggers_for_file, filename_id))
		audio_db_cursor.execute('''UPDATE audio SET total_visit_duration = ? WHERE id = ?''',(new_total_visit_duration_for_file, filename_id))
		audio_db_cursor.execute('''UPDATE audio SET total_average_visit_duration = ? WHERE id = ?''',(new_average_visit_duration_for_file, filename_id))
		audio_db_cursor.execute('''UPDATE audio SET total_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
		audio_db_cursor.execute('''UPDATE audio SET total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))

	audio_db_con.commit()

def pick_curated_audio_file(current_dominant_emotion):
	print("total_average_visit_duration_" + current_dominant_emotion + "_sessions")
	audio_db_cursor.execute('''SELECT filename FROM audio ORDER BY total_average_visit_duration_''' + current_dominant_emotion + '''_sessions DESC''')
	top_ten_rated_files = audio_db_cursor.fetchmany(10)
	print('top ten:')
	print(top_ten_rated_files)
	if(top_ten_rated_files):
		random_file_generated = random.choice(top_ten_rated_files)[0]
	else:
		random_file_generated = pick_random_audio_file()
	return(random_file_generated)

def pick_random_audio_file():
	path = r"../../../media/your/path_for/audio/"
	random_dir = random.choice(next(os.walk(path))[1])
	random_path = path + random_dir + '/'
	random_filename = random.choice([
		x for x in os.listdir(random_path)
		if not x.startswith('.') and os.path.isfile(os.path.join(random_path, x))
	])
	selection_path = (random_path + random_filename).split("/audio/",1)[1]
	print('RANDOM FILENAME SELECTED: ' + selection_path)
	return(selection_path)

def play_curated_audio_file(current_dominant_emotion):
	curated_file = pick_curated_audio_file(current_dominant_emotion)
	play_audio(curated_file)

def play_random_audio_file():
	random_file = pick_random_audio_file()
	play_audio(random_file)

def play_audio(filename):
	Media2 = Instance2.media_new_path('../../../path/to/media/audio/' + filename)
	player2.set_media(Media2)
	player2.play()

