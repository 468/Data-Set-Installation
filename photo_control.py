#!/usr/local/bin/python3
import numpy as np
import cv2
import random
import os
from PIL import Image
import sched, time
import matplotlib.pyplot as plt
import threading
import socket
import sqlite3

photo_db_path = './photo.sqlite'
photo_db_con = sqlite3.connect(photo_db_path)
photo_db_cursor = photo_db_con.cursor()

TCP_IP = '0.0.0.0'
TCP_PORT = 54321
BUFFER_SIZE = 1024

TCP_IP_2 = '0.0.0.0'
TCP_PORT_2 = 12345

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2.connect((TCP_IP_2, TCP_PORT_2))

def send_message_to_pi(message):

    s.send(message.encode('utf-8'))
    data = s.recv(BUFFER_SIZE)
    print("received data: " + str(data))
    return(data)

def send_message_to_pi_two(message):
    s2.send(message.encode('utf-8'))
    data = s2.recv(BUFFER_SIZE)
    print("received data: " + str(data))
    return(data)

def update_photo_entry(filename, dominant_emotion_recorded, visit_duration):
    photo_db_cursor.execute('''SELECT id FROM photo WHERE filename = ?''',(filename,))
    row = photo_db_cursor.fetchone()

    if row is None:
        print ("It Does Not Exist, creating filename data")
        if(dominant_emotion_recorded=='happy'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,1,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0))
        elif(dominant_emotion_recorded=='sad'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,1,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0))
        elif(dominant_emotion_recorded=='surprise'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,1,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0))
        elif(dominant_emotion_recorded=='neutral'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,1,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0,visit_duration,0,0,0))
        elif(dominant_emotion_recorded=='disgust'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,1,0,0,visit_duration,0,0,0,0,visit_duration,0,0,visit_duration,0,0,0,0,visit_duration,0,0))
        elif(dominant_emotion_recorded=='fear'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,0,1,0,visit_duration,0,0,0,0,0,visit_duration,0,visit_duration,0,0,0,0,0,visit_duration,0))
        elif(dominant_emotion_recorded=='angry'):
            photo_db_cursor.execute('''INSERT INTO photo(filename, total_display_count, happy_triggers, sad_triggers, surprise_triggers, neutral_triggers, disgust_triggers, fear_triggers, angry_triggers, total_visit_duration, total_visit_duration_happy_sessions, total_visit_duration_sad_sessions, total_visit_duration_surprise_sessions, total_visit_duration_neutral_sessions, total_visit_duration_disgust_sessions,total_visit_duration_fear_sessions,total_visit_duration_angry_sessions, total_average_visit_duration, total_average_visit_duration_happy_sessions, total_average_visit_duration_sad_sessions, total_average_visit_duration_surprise_sessions, total_average_visit_duration_neutral_sessions, total_average_visit_duration_disgust_sessions,total_average_visit_duration_fear_sessions,total_average_visit_duration_angry_sessions)
                              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (filename,1,0,0,0,0,0,0,1,visit_duration,0,0,0,0,0,0,visit_duration,visit_duration,0,0,0,0,0,0,visit_duration))
    else:
        print('It exists, updating this filename data')
        filename_id = row[0]
        photo_db_cursor.execute('''SELECT total_display_count FROM photo WHERE id=?''',(filename_id,))
        current_display_count_for_file = photo_db_cursor.fetchone()[0]

        photo_db_cursor.execute('''SELECT ''' + dominant_emotion_recorded + '''_triggers FROM photo WHERE id=?''',(filename_id,))
        current_mood_triggers_for_file = photo_db_cursor.fetchone()[0]

        photo_db_cursor.execute('''SELECT total_visit_duration FROM photo WHERE id=?''',(filename_id,))
        current_total_visit_duration_for_file = photo_db_cursor.fetchone()[0]

        photo_db_cursor.execute('''SELECT total_average_visit_duration FROM photo WHERE id=?''',(filename_id,))
        current_total_average_visit_duration_for_file = photo_db_cursor.fetchone()[0]
        
        photo_db_cursor.execute('''SELECT total_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM photo WHERE id=?''',(filename_id,))
        current_total_mood_visit_duration_for_file = photo_db_cursor.fetchone()[0]

        photo_db_cursor.execute('''SELECT total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions FROM photo WHERE id=?''',(filename_id,))
        current_total_mood_average_visit_duration_for_file = photo_db_cursor.fetchone()[0]

        new_display_count_for_file = current_display_count_for_file + 1
        new_mood_triggers_for_file = current_mood_triggers_for_file + 1
        new_total_visit_duration_for_file = current_total_visit_duration_for_file + visit_duration
        new_average_visit_duration_for_file = new_total_visit_duration_for_file / new_display_count_for_file
        new_total_mood_visit_duration_for_file = current_total_mood_visit_duration_for_file + visit_duration
        new_average_mood_visit_duration_for_file = new_total_mood_visit_duration_for_file / new_mood_triggers_for_file

        photo_db_cursor.execute('''UPDATE photo SET total_display_count = ? WHERE id = ?''',(new_display_count_for_file, filename_id))
        photo_db_cursor.execute('''UPDATE photo SET ''' + dominant_emotion_recorded + '''_triggers = ? WHERE id = ?''',(new_mood_triggers_for_file, filename_id))
        photo_db_cursor.execute('''UPDATE photo SET total_visit_duration = ? WHERE id = ?''',(new_total_visit_duration_for_file, filename_id))
        photo_db_cursor.execute('''UPDATE photo SET total_average_visit_duration = ? WHERE id = ?''',(new_average_visit_duration_for_file, filename_id))
        photo_db_cursor.execute('''UPDATE photo SET total_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
        photo_db_cursor.execute('''UPDATE photo SET total_average_visit_duration_''' + dominant_emotion_recorded + '''_sessions = ? WHERE id = ?''',(new_total_mood_visit_duration_for_file, filename_id))
        photo_db_con.commit()

def pick_curated_photo_file(current_dominant_emotion):
  
    photo_db_cursor.execute('''SELECT filename FROM photo ORDER BY total_average_visit_duration_''' + current_dominant_emotion + '''_sessions DESC''')
    top_ten_rated_files = photo_db_cursor.fetchmany(10)
    print('top ten:')
    print(top_ten_rated_files)
    if(top_ten_rated_files):
        random_file_generated = random.choice(top_ten_rated_files)[0]
    else:
        random_file_generated = pick_random_photo_file()
    return(random_file_generated)

def pick_random_photo_file():
    filename = send_message_to_pi('pick_random_photo_file')
    decoded_filename = str(filename, 'utf-8')
    return(decoded_filename)

def pick_random_photo_file_two():
    filename = send_message_to_pi_two('pick_random_photo_file')
    decoded_filename = str(filename, 'utf-8')
    return(decoded_filename)

def play_curated_photo_file(current_dominant_emotion):
    curated_file = pick_curated_photo_file(current_dominant_emotion)
    play_photo(curated_file)

def play_curated_photo_file_two(current_dominant_emotion):
    curated_file = pick_curated_photo_file(current_dominant_emotion)
    play_photo_two(curated_file)

def play_random_photo_file():
    random_file = pick_random_photo_file()
    play_photo(random_file)

def play_random_photo_file_two():
    random_file = pick_random_photo_file_two()
    play_photo_two(random_file)

def play_photo(filename):
    send_message_to_pi('play_file:' + str(filename))

def play_photo_two(filename):
    send_message_to_pi_two('play_file:' + str(filename))