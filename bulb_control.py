import yeelight
from yeelight import Bulb
import time
import sqlite3
import random
import datetime

bulb = Bulb("0.0.0.0")
bulb.auto_on = True

bulb_colours = ['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white']

bulb_db_path = './bulb.sqlite'
bulb_db_con = sqlite3.connect(bulb_db_path)
bulb_db_cursor = bulb_db_con.cursor()

def update_bulb_entry(properties, dominant_emotion_recorded, visit_duration):
	print('nothing yet')
	print("UPDATING bulb ENTRY FROM WITHIN bulb TEST")
	print('PROPERTIES: + properties')
	brightness = str(properties[0])
	colour = properties[1]
	joined_properties = '|'.join([brightness, colour])
	print('JOINED PROPERTIES: ' + joined_properties)
	bulb_db_cursor.execute('''SELECT id FROM bulb WHERE properties = ?''',(joined_properties,))
	row = bulb_db_cursor.fetchone()
	print('ROW COUNT:::')
	print(row)

	if row is None:
		print ("Property Does Not Exist, creating property data")
		if(dominant_emotion_recorded=='happy'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,1,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0))
		elif(dominant_emotion_recorded=='sad'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,0,1,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0))
		elif(dominant_emotion_recorded=='surprise'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,0,0,1,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0))
		elif(dominant_emotion_recorded=='neutral'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,0,0,0,1,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0))
		elif(dominant_emotion_recorded=='disgust'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,0,0,0,0,1,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0))
		elif(dominant_emotion_recorded=='fear'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,0,0,0,0,0,1,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0))
		elif(dominant_emotion_recorded=='angry'):
			bulb_db_cursor.execute('''INSERT INTO bulb(properties, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
			                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (joined_properties,1,0,0,0,0,0,0,1,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration))
	else:
		print('It exists, updating this filename data')
		filename_id = row[0]
		bulb_db_cursor.execute('''SELECT total_display_count FROM bulb WHERE id=?''',(filename_id,))
		current_display_count_for_file = bulb_db_cursor.fetchone()[0]

		bulb_db_cursor.execute('''SELECT ''' + dominant_emotion_recorded + '''_triggers FROM bulb WHERE id=?''',(filename_id,))
		current_mood_triggers_for_file = bulb_db_cursor.fetchone()[0]

		bulb_db_cursor.execute('''SELECT total_visit_duration FROM bulb WHERE id=?''',(filename_id,))
		current_total_visit_duration_for_file = bulb_db_cursor.fetchone()[0]

		bulb_db_cursor.execute('''SELECT total_average_visit_duration FROM bulb WHERE id=?''',(filename_id,))
		current_total_average_visit_duration_for_file = bulb_db_cursor.fetchone()[0]
		
		bulb_db_cursor.execute('''SELECT total_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM bulb WHERE id=?''',(filename_id,))
		current_total_mood_visit_duration_for_file = bulb_db_cursor.fetchone()[0]

		bulb_db_cursor.execute('''SELECT total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM bulb WHERE id=?''',(filename_id,))
		current_total_mood_average_visit_duration_for_file = bulb_db_cursor.fetchone()[0]

		new_display_count_for_file = current_display_count_for_file + 1
		new_mood_triggers_for_file = current_mood_triggers_for_file + 1
		new_total_visit_duration_for_file = current_total_visit_duration_for_file + visit_duration
		new_average_visit_duration_for_file = new_total_visit_duration_for_file / new_display_count_for_file
		new_total_mood_visit_duration_for_file = current_total_mood_visit_duration_for_file + visit_duration
		new_average_mood_visit_duration_for_file = new_total_mood_visit_duration_for_file / new_mood_triggers_for_file

		bulb_db_cursor.execute('''UPDATE bulb SET total_display_count = ? WHERE id = ?''',(new_display_count_for_file, filename_id))
		bulb_db_cursor.execute('''UPDATE bulb SET ''' + dominant_emotion_recorded + '''_triggers = ? WHERE id = ?''',(new_mood_triggers_for_file, filename_id))
		bulb_db_cursor.execute('''UPDATE bulb SET total_visit_duration = ? WHERE id = ?''',(new_total_visit_duration_for_file, filename_id))
		bulb_db_cursor.execute('''UPDATE bulb SET total_average_visit_duration = ? WHERE id = ?''',(new_average_visit_duration_for_file, filename_id))
		bulb_db_cursor.execute('''UPDATE bulb SET total_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
		bulb_db_cursor.execute('''UPDATE bulb SET total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))

	bulb_db_con.commit()

def pick_curated_bulb_properties(current_dominant_emotion): 
	print("total_average_visit_duration_" + current_dominant_emotion + "_sessions")
	bulb_db_cursor.execute('''SELECT properties FROM bulb ORDER BY total_average_visit_duration_''' + current_dominant_emotion + '''_sessions DESC''')
	top_ten_rated_files = bulb_db_cursor.fetchmany(10)
	print('top ten properties:')
	print(top_ten_rated_files)

	if(top_ten_rated_files):
		joined_random_file_generated = random.choice(top_ten_rated_files)[0]
		random_file_generated = joined_random_file_generated.split('|')
	else:
		random_file_generated = pick_random_bulb_properties()

	return(random_file_generated)

def pick_random_bulb_properties():

	new_random_brightness = random.randint(5, 100)
	new_random_bulb_colour = random.choice(bulb_colours)

	return [new_random_brightness, new_random_bulb_colour]

def play_random_bulb_properties():
	random_properties = pick_random_bulb_properties()

	play_bulb_properties(random_properties)


def play_bulb_properties(properties):
	brightness = int(properties[0])
	colour = properties[1]

	try:
		if(colour=='red'):
			bulb.set_rgb(0, 255, 255, duration=4000)
		elif(colour=='yellow'):
			bulb.set_rgb(255,255,0, duration=4000)
		elif(colour=='blue'):
			bulb.set_rgb(0,0,255, duration=4000)
		elif(colour=='green'):
			bulb.set_rgb(0,255,0, duration=4000)
		elif(colour=='orange'):
			bulb.set_rgb(255,165,0, duration=4000)
		elif(colour=='purple'):
			bulb.set_rgb(128,0,128, duration=4000)
		elif(colour=='white'):
			bulb.set_rgb(255,255,255, duration=4000)

		bulb.set_brightness(brightness, duration=4000)
	except:
		print("bulb (yeelight) failed to update")
