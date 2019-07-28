from tplink_smartplug import SmartPlug
import time
import sqlite3
import numpy as numpy
import random
import datetime

scent_db_path = './scent.sqlite'
scent_db_con = sqlite3.connect(scent_db_path)
scent_db_cursor = scent_db_con.cursor()

scent1 = SmartPlug('0.0.0.0')
scent2 = SmartPlug('0.0.0.0')
scent3 = SmartPlug('0.0.0.0')

scent_combinations = ['xoo', 'xxo', 'xox', 'xxx', 'ooo', 'oxo', 'oxx', 'oox']

def update_scent_entry(properties, dominant_emotion_recorded, visit_duration):
	scent_db_cursor.execute('''SELECT id FROM scent WHERE properties = ?''',(properties,))
	row = scent_db_cursor.fetchone()
	print('ROW COUNT:::')
	print(row)
	if row is None:
		print ("It Does Not Exist, creating filename data")
		if(dominant_emotion_recorded=='happy'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,1,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0))
		elif(dominant_emotion_recorded=='sad'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,0,1,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0))
		elif(dominant_emotion_recorded=='surprise'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,0,0,1,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0))
		elif(dominant_emotion_recorded=='neutral'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,0,0,0,1,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0))
		elif(dominant_emotion_recorded=='disgust'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,0,0,0,0,1,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0))
		elif(dominant_emotion_recorded=='fear'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,0,0,0,0,0,1,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0))
		elif(dominant_emotion_recorded=='angry'):
			scent_db_cursor.execute('''INSERT INTO scent(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (properties,1,0,0,0,0,0,0,1,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration))
	else:
		print('It exists, updating this filename data')
		filename_id = row[0]
		#cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
		scent_db_cursor.execute('''SELECT total_display_count FROM scent WHERE id=?''',(filename_id,))
		current_display_count_for_file = scent_db_cursor.fetchone()[0]

		scent_db_cursor.execute('''SELECT ''' + dominant_emotion_recorded + '''_triggers FROM scent WHERE id=?''',(filename_id,))
		current_mood_triggers_for_file = scent_db_cursor.fetchone()[0]

		scent_db_cursor.execute('''SELECT total_visit_duration FROM scent WHERE id=?''',(filename_id,))
		current_total_visit_duration_for_file = scent_db_cursor.fetchone()[0]

		scent_db_cursor.execute('''SELECT total_average_visit_duration FROM scent WHERE id=?''',(filename_id,))
		current_total_average_visit_duration_for_file = scent_db_cursor.fetchone()[0]
		
		scent_db_cursor.execute('''SELECT total_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM scent WHERE id=?''',(filename_id,))
		current_total_mood_visit_duration_for_file = scent_db_cursor.fetchone()[0]

		scent_db_cursor.execute('''SELECT total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM scent WHERE id=?''',(filename_id,))
		current_total_mood_average_visit_duration_for_file = scent_db_cursor.fetchone()[0]

		new_display_count_for_file = current_display_count_for_file + 1
		new_mood_triggers_for_file = current_mood_triggers_for_file + 1
		new_total_visit_duration_for_file = current_total_visit_duration_for_file + visit_duration
		new_average_visit_duration_for_file = new_total_visit_duration_for_file / new_display_count_for_file
		new_total_mood_visit_duration_for_file = current_total_mood_visit_duration_for_file + visit_duration
		new_average_mood_visit_duration_for_file = new_total_mood_visit_duration_for_file / new_mood_triggers_for_file

		scent_db_cursor.execute('''UPDATE scent SET total_display_count = ? WHERE id = ?''',(new_display_count_for_file, filename_id))
		scent_db_cursor.execute('''UPDATE scent SET ''' + dominant_emotion_recorded + '''_triggers = ? WHERE id = ?''',(new_mood_triggers_for_file, filename_id))
		scent_db_cursor.execute('''UPDATE scent SET total_visit_duration = ? WHERE id = ?''',(new_total_visit_duration_for_file, filename_id))
		scent_db_cursor.execute('''UPDATE scent SET total_average_visit_duration = ? WHERE id = ?''',(new_average_visit_duration_for_file, filename_id))
		scent_db_cursor.execute('''UPDATE scent SET total_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
		scent_db_cursor.execute('''UPDATE scent SET total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
	scent_db_con.commit()

def pick_curated_scent(current_dominant_emotion):
	scent_db_cursor.execute('''SELECT properties FROM scent ORDER BY total_average_visit_duration_''' + current_dominant_emotion + '''_sessions DESC''')
	top_ten_rated_files = scent_db_cursor.fetchmany(10)
	print('top ten:')
	print(top_ten_rated_files)
	if(top_ten_rated_files):
		random_file_generated = random.choice(top_ten_rated_files)[0]
	else:
		random_file_generated = pick_random_scent()
	print('random choice from top ten: ' + random_file_generated )
	return(random_file_generated)

def pick_random_scent():
	random_scent = random.choice(scent_combinations)
	return random_scent

def play_random_scent():
	random_scent = pick_random_scent()
	play_scent(random_scent)

def play_scent(combination):

	try:
		if(combination=='xoo'):
			scent1.turn_on()
			scent2.turn_off()
			scent3.turn_off()
		elif(combination=='xxo'):
			scent1.turn_on()
			scent2.turn_on()
			scent3.turn_off()
		elif(combination=='xox'):
			scent1.turn_on()
			scent2.turn_off()
			scent3.turn_on()
		elif(combination=='xxx'):
			scent1.turn_on()
			scent2.turn_on()
			scent3.turn_on()
		elif(combination=='ooo'):
			scent1.turn_off()
			scent2.turn_off()
			scent3.turn_off()
		elif(combination=='oxo'):
			scent1.turn_off()
			scent2.turn_on()
			scent3.turn_off()
		elif(combination=='oxx'):
			scent1.turn_off()
			scent2.turn_on()
			scent3.turn_on()
		elif(combination=='oox'):
			scent1.turn_off()
			scent2.turn_off()
			scent3.turn_on()
	except:
		print('scent failed to update')
