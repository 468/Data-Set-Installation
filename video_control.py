import vlc
import sys
import cv2
import time
import sqlite3
import numpy as numpy
import random
import os

video_db_path = './video.sqlite'
video_db_con = sqlite3.connect(video_db_path)
video_db_cursor = video_db_con.cursor()

Instance = vlc.Instance('--fullscreen --input-repeat=-1 --no-audio --video-on-top')
vlc.Position = 100
player = Instance.media_player_new()
vlc.PlaybackMode(1) #loop

def update_video_entry(filename, dominant_emotion_recorded, visit_duration):

	print("UPDATING VIDEO ENTRY FROM WITHIN VIDEO TEST")

	video_db_cursor.execute('''SELECT id FROM video WHERE filename = ?''',(filename,))
	row = video_db_cursor.fetchone()
	print('ROW COUNT:::')
	print(row)

	if row is None:
		print ("It Does Not Exist, creating filename data")
		if(dominant_emotion_recorded=='happy'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,1,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0))
		elif(dominant_emotion_recorded=='sad'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,1,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0))
		elif(dominant_emotion_recorded=='surprise'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,1,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0))
		elif(dominant_emotion_recorded=='neutral'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,1,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0))
		elif(dominant_emotion_recorded=='disgust'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,1,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0))
		elif(dominant_emotion_recorded=='fear'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,0,1,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0))
		elif(dominant_emotion_recorded=='angry'):
			video_db_cursor.execute('''INSERT INTO video(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,0,0,1,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration))
	else:
		print('It exists, updating this filename data')
		filename_id = row[0]
		#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
		video_db_cursor.execute('''SELECT total_display_count FROM video WHERE id=?''',(filename_id,))
		current_display_count_for_file = video_db_cursor.fetchone()[0]

		video_db_cursor.execute('''SELECT ''' + dominant_emotion_recorded + '''_triggers FROM video WHERE id=?''',(filename_id,))
		current_mood_triggers_for_file = video_db_cursor.fetchone()[0]

		video_db_cursor.execute('''SELECT total_visit_duration FROM video WHERE id=?''',(filename_id,))
		current_total_visit_duration_for_file = video_db_cursor.fetchone()[0]

		video_db_cursor.execute('''SELECT total_average_visit_duration FROM video WHERE id=?''',(filename_id,))
		current_total_average_visit_duration_for_file = video_db_cursor.fetchone()[0]
		
		video_db_cursor.execute('''SELECT total_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM video WHERE id=?''',(filename_id,))
		current_total_mood_visit_duration_for_file = video_db_cursor.fetchone()[0]

		video_db_cursor.execute('''SELECT total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM video WHERE id=?''',(filename_id,))
		current_total_mood_average_visit_duration_for_file = video_db_cursor.fetchone()[0]

		new_display_count_for_file = current_display_count_for_file + 1
		new_mood_triggers_for_file = current_mood_triggers_for_file + 1
		new_total_visit_duration_for_file = current_total_visit_duration_for_file + visit_duration
		new_average_visit_duration_for_file = new_total_visit_duration_for_file / new_display_count_for_file
		new_total_mood_visit_duration_for_file = current_total_mood_visit_duration_for_file + visit_duration
		new_average_mood_visit_duration_for_file = new_total_mood_visit_duration_for_file / new_mood_triggers_for_file

		video_db_cursor.execute('''UPDATE video SET total_display_count = ? WHERE id = ?''',(new_display_count_for_file, filename_id))
		video_db_cursor.execute('''UPDATE video SET ''' + dominant_emotion_recorded + '''_triggers = ? WHERE id = ?''',(new_mood_triggers_for_file, filename_id))
		video_db_cursor.execute('''UPDATE video SET total_visit_duration = ? WHERE id = ?''',(new_total_visit_duration_for_file, filename_id))
		video_db_cursor.execute('''UPDATE video SET total_average_visit_duration = ? WHERE id = ?''',(new_average_visit_duration_for_file, filename_id))
		video_db_cursor.execute('''UPDATE video SET total_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
		video_db_cursor.execute('''UPDATE video SET total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))

	video_db_con.commit()

def pick_curated_video_file(current_dominant_emotion):

	print("total_average_visit_duration_" + current_dominant_emotion + "_sessions")
	video_db_cursor.execute('''SELECT filename FROM video ORDER BY total_average_visit_duration_''' + current_dominant_emotion + '''_sessions DESC''')
	top_ten_rated_files = video_db_cursor.fetchmany(10)
	print('top ten videos:')
	print(top_ten_rated_files)

	#random_file_from_top_ten = top_ten_rated_files[0][0]
	if(top_ten_rated_files):
		random_file_generated = random.choice(top_ten_rated_files)[0]
	else:
		random_file_generated = pick_random_video_file()

	print('random choice from top ten: ' + random_file_generated )
	return(random_file_generated)

def pick_random_video_file():
	path = r"../../../media/alex/0206-ECAE/videos/"
	random_dir = random.choice(next(os.walk(path))[1])
	random_path = path + random_dir + '/'
	random_filename = random.choice([
		x for x in os.listdir(random_path)
		if not x.startswith('.') and os.path.isfile(os.path.join(random_path, x))
	])
	selection_path = (random_path + random_filename).split("/videos/",1)[1]
	print('RANDOM FILENAME SELECTED: ' + selection_path)
	return(selection_path)

def play_random_video_file():
	random_file = pick_random_video_file()
	play_video(random_file)

def play_video(filename):
	Media = Instance.media_new_path('../../../media/alex/0206-ECAE/videos/' + filename)
	player.set_fullscreen(1)
	player.set_media(Media)
	player.play()
