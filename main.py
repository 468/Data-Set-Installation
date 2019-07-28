from pyimagesearch.centroidtracker import CentroidTracker
from pyimagesearch.trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import argparse
import imutils
import time
import sched
import schedule
import threading
import dlib
import cv2
import datetime
import sqlite3
import random
#stuff for emotion detection
from keras.models import load_model
from statistics import mode
from utils.datasets import get_labels
from utils.inference import detect_faces
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.inference import load_detection_model
from utils.preprocessor import preprocess_input
#imports
import audio_control_vlc
import video_control
import bulb_control
import scent_control
import photo_control
import lavalamp_control

someone_in_room = False
audio_update_frequency_probability = 0.5
audio_update_play_best_probability = 0.25
audio_autoplay_change_frequency = 5
video_update_frequency_probability = 0.5
video_update_play_best_probability = 0.25
video_autoplay_change_frequency = 5
bulb_update_frequency_probability = 0.5
bulb_update_play_best_probability = 0.25
bulb_autoplay_change_frequency = 5
scent_update_frequency_probability = 0.5
scent_update_play_best_probability = 0.25
scent_autoplay_change_frequency = 5
photo_update_frequency_probability = 0.5
photo_update_play_best_probability = 0.25
photo_autoplay_change_frequency = 5
lavalamp_autoplay_change_frequency = 2

scent_last_updated = datetime.datetime.now() - datetime.timedelta(seconds=5)
bulb_last_updated = datetime.datetime.now() - datetime.timedelta(seconds=5)

def audio_autoplay():
	print("updating audio")
	if(someone_in_room == False):
		if(random.random() < audio_update_frequency_probability):
			print('rolled heads, random update')
			audio_test_vlc.play_random_audio_file()

		else:
			print('rolled tails, no random update here')
	elif(someone_in_room == True):
		print('do nothing; should be reactive')
		pass

def video_autoplay():
	print("updating video")
	if(someone_in_room == False):
		if(random.random() < video_update_frequency_probability):
			print('rolled heads, random update')
			video_test.play_random_video_file()

		else:
			print('rolled tails, no random video update here')
	elif(someone_in_room == True):
		print('do nothing; should be reactive')
		pass

def bulb_autoplay():
	print("updating bulb")
	if(someone_in_room == False):
		if(random.random() < bulb_update_frequency_probability):
			print('rolled heads, random update')
			bulb_test.play_random_bulb_properties()

		else:
			print('rolled tails, no random video update here')
	elif(someone_in_room == True):
		print('do nothing; should be reactive')
		pass

def scent_autoplay():
	print("updating scent")
	if(someone_in_room == False):
		if(random.random() < scent_update_frequency_probability):
			print('rolled heads, random scent update')
			scent_test.play_random_scent()

		else:
			print('rolled tails, no random scent update here')
	elif(someone_in_room == True):
		print('do nothing; should be reactive')
		pass

def photo_autoplay():
	print("updating photo")
	if(someone_in_room == False):
		if(random.random() < photo_update_frequency_probability):
			print('rolled heads, random update')
			photo_test.play_random_photo_file()
			photo_test.play_random_photo_file_two()

		else:
			print('rolled tails, no random video update here')
	elif(someone_in_room == True):
		print('do nothing; should be reactive')
		pass

def lavalamp_autoplay():
	print('updating lavalamp')
	if(someone_in_room == False):
		try:
			lavalamp_test.turn_off_lavalamp()
		except:
			print('failed to turn off lavalamp')
	else:
		try:
			lavalamp_test.turn_on_lavalamp()
		except:
			print('failed to turn on lavalamp')

def audio_update(current_emotion):
	print('updating audio')
	if(random.random() < audio_update_play_best_probability):
		curated_audio_file = audio_test_vlc.pick_curated_audio_file(current_emotion)
	else:
		curated_audio_file = audio_test_vlc.pick_random_audio_file()
	print('playing audio from audio update')
	audio_test_vlc.play_audio(curated_audio_file)

	return curated_audio_file

def video_update(current_emotion):
	print('updating video')
	if(random.random() < video_update_play_best_probability):
		curated_video_file = video_test.pick_curated_video_file(current_emotion)
	else:
		curated_video_file = video_test.pick_random_video_file()
	print('playing video from video update')
	video_test.play_video(curated_video_file)

	return curated_video_file

def bulb_update(current_emotion):
	print('updating bulb')


	if(random.random() < bulb_update_play_best_probability):
		curated_bulb_properties = bulb_test.pick_curated_bulb_properties(current_emotion)
	else:
		curated_bulb_properties = bulb_test.pick_random_bulb_properties()
	print('playing bulb from bulb update')
	bulb_test.play_bulb_properties(curated_bulb_properties)

	return curated_bulb_properties

def scent_update(current_emotion):
	print('updating scent')

	if(random.random() < scent_update_play_best_probability):
		curated_scent_properties = scent_test.pick_curated_scent(current_emotion)
	else:
		curated_scent_properties = scent_test.pick_random_scent()
	print('playing scent from scent update')
	scent_test.play_scent(curated_scent_properties)

	return curated_scent_properties

def photo_update(current_emotion):
	print('updating photo')
	if(random.random() < photo_update_play_best_probability):
		print('nothing right now 213')
		curated_photo_file = photo_test.pick_curated_photo_file(current_emotion)
	else:
		curated_photo_file = photo_test.pick_random_photo_file()
		print('nothing right now')
	print('playing video from video update')
	photo_test.play_photo(curated_photo_file)

def photo_update_two(current_emotion):
	print('updating photo')
	if(random.random() < photo_update_play_best_probability):
		print('nothing right now 213')
		curated_photo_file = photo_test.pick_curated_photo_file(current_emotion)
	else:
		curated_photo_file = photo_test.pick_random_photo_file_two()
		print('nothing right now')
	print('playing video from video update')
	photo_test.play_photo_two(curated_photo_file)

def start_autoplay_schedulers():
	schedule.every(audio_autoplay_change_frequency).seconds.do(audio_autoplay)
	schedule.every(video_autoplay_change_frequency).seconds.do(video_autoplay)
	schedule.every(bulb_autoplay_change_frequency).seconds.do(bulb_autoplay)
	schedule.every(scent_autoplay_change_frequency).seconds.do(scent_autoplay)
	schedule.every(photo_autoplay_change_frequency).seconds.do(photo_autoplay)
	schedule.every(lavalamp_autoplay_change_frequency).seconds.do(lavalamp_autoplay)

start_autoplay_schedulers()

#database connection
visits_db_path = './visits.sqlite'
visits_db_con = sqlite3.connect(visits_db_path)
visits_db_cursor = visits_db_con.cursor()
#load emotion models etc
emotion_model_path = './models/emotion_model.hdf5'
emotion_labels = get_labels('fer2013')
# hyper-parameters for bounding boxes shape
frame_window = 10
emotion_offsets = (20, 40)
# loading models
face_cascade = cv2.CascadeClassifier('./models/haarcascade_frontalface_default.xml')
emotion_classifier = load_model(emotion_model_path)
# getting input model shapes for inference
emotion_target_size = emotion_classifier.input_shape[1:3]
# starting lists for calculating modes
emotion_window = []
color = 5 * np.asarray((255, 0, 0))
# initialize the list of class labels MobileNet SSD was trained to
# detect
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

#active_time_trackers =	{}
total_time_in_frame = 0;
total_visits = 0;
average_time_in_frame = 0;
last_visit_time = 0
active_visitors = {}
object_id_to_emotion = {}
centroid_to_emotion = []
face_coordinates_to_emotion = []
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("mobilenet_ssd/MobileNetSSD_deploy.prototxt", "mobilenet_ssd/MobileNetSSD_deploy.caffemodel")
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
time.sleep(2.0)
writer = None
W = None
H = None
ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
trackers = []
trackableObjects = {}
totalFrames = 0
totalDown = 0
totalUp = 0

fps = FPS().start()

def keywithmaxval(d):
     v=list(d.values())
     k=list(d.keys())
     return k[v.index(max(v))]
while True:
	frame = vs.read()
	frame = imutils.resize(frame, width=500)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	# if the frame dimensions are empty, set them
	if W is None or H is None:
		(H, W) = frame.shape[:2]
	status = "Waiting"
	rects = []

	if totalFrames % 60 == 0:
		
		face_coordinates_to_emotion = []

		status = "Detecting"
		trackers = []
		gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5,
				minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

		for face_coordinates in faces:

		    x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
		    gray_face = gray_image[y1:y2, x1:x2]
		    try:
		        gray_face = cv2.resize(gray_face, (emotion_target_size))
		    except:
		        continue

		    gray_face = preprocess_input(gray_face, True)
		    gray_face = np.expand_dims(gray_face, 0)
		    gray_face = np.expand_dims(gray_face, -1)
		    emotion_prediction = emotion_classifier.predict(gray_face)
		    emotion_probability = np.max(emotion_prediction)
		    emotion_label_arg = np.argmax(emotion_prediction)
		    emotion_text = emotion_labels[emotion_label_arg]
		    emotion_window.append(emotion_text)

		    if len(emotion_window) > frame_window:
		        emotion_window.pop(0)
		    try:
		        emotion_mode = mode(emotion_window)
		    except:
		        continue

		    if emotion_text == 'angry':
		        color = emotion_probability * np.asarray((255, 0, 0))
		    elif emotion_text == 'disgust':
		        color = emotion_probability * np.asarray((0, 0, 255))
		    elif emotion_text == 'fear':
		        color = emotion_probability * np.asarray((0, 0, 255))
		        
		    elif emotion_text == 'happy':
		        color = emotion_probability * np.asarray((0, 0, 255))
		    elif emotion_text == 'sad':
		        color = emotion_probability * np.asarray((255, 255, 0))
		    elif emotion_text == 'surprise':
		        color = emotion_probability * np.asarray((0, 255, 255))
		    elif emotion_text == 'neutral':
		        color = emotion_probability * np.asarray((0, 255, 0))
		   
		    color = color.astype(int)
		    color = color.tolist()

		    draw_bounding_box(face_coordinates, frame, color)
		    draw_text(face_coordinates, frame, emotion_text,
		              color, 0, -45, 1, 1)
		    
		    tracker = dlib.correlation_tracker()
		
		    rect = dlib.rectangle(int(x1), int(y1), int(x2), int(y2))
		    tracker.start_track(rgb, rect)
		    trackers.append(tracker)
		    pos = tracker.get_position()
		    startX = int(pos.left())
		    startY = int(pos.top())
		    endX = int(pos.right())
		    endY = int(pos.bottom())
		    rects.append((startX, startY, endX, endY))
		    temp_cX = int((startX + endX) / 2.0)
		    temp_cY = int((startY + endY) / 2.0)
		    temp_centroid = [temp_cX, temp_cY]
		    centroid_to_emotion.append([temp_centroid, emotion_text])
		    face_coordinates_to_emotion.append([face_coordinates, emotion_text])
		if( active_visitors ):
			someone_in_room = True
			print("setting someone in room to TRUE")
		else:
			someone_in_room = False
			print("setting someone in room to FALSE")
	else:
		centroid_to_emotion = []
		for tracker in trackers:
			status = "Tracking"
			tracker.update(rgb)
			pos = tracker.get_position()
			startX = int(pos.left())
			startY = int(pos.top())
			endX = int(pos.right())
			endY = int(pos.bottom())
			rects.append((startX, startY, endX, endY))
		for face_coordinate_arrays in face_coordinates_to_emotion:
			this_face_coordinate = face_coordinate_arrays[0]
			this_face_emotion = face_coordinate_arrays[1]
			draw_bounding_box(this_face_coordinate, frame, color)
			draw_text(this_face_coordinate, frame, this_face_emotion, color, 0, -45, 1, 1)
	objects = ct.update(rects)

	if(status == "Detecting"):

		print("CENTROID TO EMOTION")
		print(centroid_to_emotion)
		print("OBJECT ITEMS")
		print(objects.items())
		for centroid_arrays in centroid_to_emotion:
			this_centroid = centroid_arrays[0]
			this_centroids_emotion = centroid_arrays[1]
			for key,value in objects.items():

				if not key in active_visitors:
					print('ADDING THIS VISITOR LINE 389')
					active_visitors[key] = {}
					active_visitors[key]['time_entered'] = datetime.datetime.now()
					active_visitors[key]['time_exited'] = 0
					active_visitors[key]['sad_detections'] = 0
					active_visitors[key]['happy_detections'] = 0
					active_visitors[key]['neutral_detections'] = 0
					active_visitors[key]['surprise_detections'] = 0
					active_visitors[key]['angry_detections'] = 0
					active_visitors[key]['fear_detections'] = 0
					active_visitors[key]['disgust_detections'] = 0
					active_visitors[key]['last_emotion_detected'] = 'none'
					active_visitors[key]['dominant_emotion_detected'] = 'none'
					active_visitors[key]['audio_experienced'] = []
					active_visitors[key]['video_experienced'] = []
					active_visitors[key]['bulb_experienced'] = []
					active_visitors[key]['scent_experienced'] = []
					active_visitors[key]['photo_experienced'] = []

				print("THESE SHOULD MATCH???")
				j = list(value)
				k = this_centroid
				print(j)
				print(k)

				if(np.array_equal(j,k)):
					print("THEY MATCH")
					#add last emotion detected to this particular key
					active_visitors[key][this_centroids_emotion + '_detections'] +=1
					current_emotion_tally = {}
					current_emotion_tally['sad'] = active_visitors[key]['sad_detections']
					current_emotion_tally['happy'] = active_visitors[key]['happy_detections']
					current_emotion_tally['neutral'] = active_visitors[key]['neutral_detections']
					current_emotion_tally['disgust'] = active_visitors[key]['disgust_detections']
					current_emotion_tally['fear'] = active_visitors[key]['fear_detections']
					current_emotion_tally['surprise'] = active_visitors[key]['surprise_detections']
					current_emotion_tally['angry'] = active_visitors[key]['angry_detections']
					current_dominant_emotion = keywithmaxval(current_emotion_tally)
					if(current_dominant_emotion != active_visitors[key]['dominant_emotion_detected']):
						print('new dominant emotion detected! playing relevent audio...')
						audio_filename_now_playing = audio_update(current_dominant_emotion)
						if(audio_filename_now_playing not in active_visitors[key]['audio_experienced']):
							active_visitors[key]['audio_experienced'].append(audio_filename_now_playing)
						video_filename_now_playing = video_update(current_dominant_emotion)
						if(video_filename_now_playing not in active_visitors[key]['video_experienced']):
							active_visitors[key]['video_experienced'].append(video_filename_now_playing)
						current_time = datetime.datetime.now()
						time_since_last_scent_api_call = (current_time - scent_last_updated).total_seconds()
						time_since_last_bulb_api_call = (current_time - bulb_last_updated).total_seconds()
						if(time_since_last_bulb_api_call > 4):
							bulb_properties_now_playing = bulb_update(current_dominant_emotion)
							if(bulb_properties_now_playing not in active_visitors[key]['bulb_experienced']):
								active_visitors[key]['bulb_experienced'].append(bulb_properties_now_playing)
							bulb_last_updated = current_time
						if(time_since_last_scent_api_call > 4):
							scent_properties_now_playing = scent_update(current_dominant_emotion)
							if(scent_properties_now_playing not in active_visitors[key]['scent_experienced']):
								active_visitors[key]['scent_experienced'].append(scent_properties_now_playing)
							scent_last_updated = current_time
						photo_filename_now_playing = photo_update(current_dominant_emotion)
						if(photo_filename_now_playing not in active_visitors[key]['photo_experienced']):
							active_visitors[key]['photo_experienced'].append(photo_filename_now_playing)
						photo_filename_two_now_playing = photo_update_two(current_dominant_emotion)
						if(photo_filename_two_now_playing not in active_visitors[key]['photo_experienced']):
							active_visitors[key]['photo_experienced'].append(photo_filename_two_now_playing)
					active_visitors[key]['dominant_emotion_detected'] = current_dominant_emotion
					active_visitors[key]['last_emotion_detected'] = this_centroids_emotion
	for k, v in list(active_visitors.items()):
			if not k in objects:
				active_visitors[k]['time_exited'] = datetime.datetime.now()
				time_spent_this_visit = (active_visitors[k]['time_exited'] - active_visitors[k]['time_entered']).total_seconds()
				if(time_spent_this_visit > 1):
					total_visits +=1;
					visits_db_cursor.execute('''SELECT visit_count FROM visits''')
					visit_count = visits_db_cursor.fetchone()[0] #retrieve the first row
					visit_count +=1
					visits_db_cursor.execute('''UPDATE visits SET visit_count = ? WHERE id = ?''',(visit_count, 1))
					visits_db_con.commit()
					print("TOTAL TIME SPENT FOR THIS VISIT: " + str(time_spent_this_visit))
					visits_db_cursor.execute('''SELECT total_visit_duration FROM visits''')
					total_time_spent = visits_db_cursor.fetchone()[0] #retrieve the first row
					new_total_time_spent = total_time_spent + time_spent_this_visit
					visits_db_cursor.execute('''UPDATE visits SET total_visit_duration = ? WHERE id = ?''',(new_total_time_spent, 1))
					new_average_time_spent = new_total_time_spent / visit_count 
					visits_db_cursor.execute('''UPDATE visits SET total_average_visit_duration = ? WHERE id = ?''',(new_average_time_spent, 1))
					visits_db_con.commit()
					emotion_tally = {}
					emotion_tally['sad'] = active_visitors[k]['sad_detections']
					emotion_tally['happy'] = active_visitors[k]['happy_detections']
					emotion_tally['neutral'] = active_visitors[k]['neutral_detections']
					emotion_tally['disgust'] = active_visitors[k]['disgust_detections']
					emotion_tally['fear'] = active_visitors[k]['fear_detections']
					emotion_tally['surprise'] = active_visitors[k]['surprise_detections']
					emotion_tally['angry'] = active_visitors[k]['angry_detections']
					dominant_emotion = keywithmaxval(emotion_tally)
					visits_db_cursor.execute('''SELECT ''' + dominant_emotion + '''_visit_count FROM visits''')
					emotion_visit_count = visits_db_cursor.fetchone()[0] #retrieve the first row
					emotion_visit_count +=1
					visits_db_cursor.execute('''UPDATE visits SET ''' + dominant_emotion + '''_visit_count = ? WHERE id = ?''',(emotion_visit_count, 1))
					visits_db_con.commit()
					visits_db_cursor.execute('''SELECT total_visit_duration_''' + dominant_emotion + '''_sessions FROM visits''')
					total_time_spent_this_emotion = visits_db_cursor.fetchone()[0]
					new_total_time_spent_this_emotion = total_time_spent_this_emotion + time_spent_this_visit
					visits_db_cursor.execute('''UPDATE visits SET total_visit_duration_''' + dominant_emotion + '''_sessions = ? WHERE id = ?''',(new_total_time_spent_this_emotion, 1))
					new_average_time_spent_this_emotion = new_total_time_spent_this_emotion / emotion_visit_count 
					visits_db_cursor.execute('''UPDATE visits SET total_average_visit_duration_''' + dominant_emotion + '''_sessions = ? WHERE id = ?''',(new_average_time_spent_this_emotion, 1))
					visits_db_con.commit()
					#log media experienced by this visitor to relevent media bits....
					for filename in active_visitors[k]['audio_experienced']:
						print('ITERATING OVER ARRAY OF THINGIES.')
						print(filename)
						audio_test_vlc.update_audio_entry(filename, dominant_emotion, time_spent_this_visit)
					for filename in active_visitors[k]['video_experienced']:
						print('ITERATING OVER ARRAY OF video THINGIES.')
						print(filename)
						video_test.update_video_entry(filename, dominant_emotion, time_spent_this_visit)
					for filename in active_visitors[k]['bulb_experienced']:
						print('ITERATING OVER ARRAY OF bulb THINGIES.')
						print(filename)
						bulb_test.update_bulb_entry(filename, dominant_emotion, time_spent_this_visit)
					for filename in active_visitors[k]['scent_experienced']:
						print('ITERATING OVER ARRAY OF scent THINGIES.')
						print(filename)
						scent_test.update_scent_entry(filename, dominant_emotion, time_spent_this_visit)
					for filename in active_visitors[k]['photo_experienced']:
						print('ITERATING OVER ARRAY OF photo THINGIES.')
						print(filename)
				active_visitors.pop(k, None)
				trackableObjects.pop(k, None)
			else:	
				pass

	print(active_visitors)
	for (objectID, centroid) in objects.items():
		to = trackableObjects.get(objectID, None)
		if not objectID in active_visitors:
			active_visitors[key] = {}
			active_visitors[key]['time_entered'] = datetime.datetime.now()
			active_visitors[key]['time_exited'] = 0
			active_visitors[key]['sad_detections'] = 0
			active_visitors[key]['happy_detections'] = 0
			active_visitors[key]['neutral_detections'] = 0
			active_visitors[key]['surprise_detections'] = 0
			active_visitors[key]['angry_detections'] = 0
			active_visitors[key]['fear_detections'] = 0
			active_visitors[key]['disgust_detections'] = 0
			active_visitors[key]['last_emotion_detected'] = 'none'
			active_visitors[key]['dominant_emotion_detected'] = 'none'
			active_visitors[key]['audio_experienced'] = []
			active_visitors[key]['video_experienced'] = []
			active_visitors[key]['bulb_experienced'] = []
			active_visitors[key]['scent_experienced'] = []
			active_visitors[key]['photo_experienced'] = []
		if to is None:
			to = TrackableObject(objectID, centroid)
		else:
			y = [c[1] for c in to.centroids]
			direction = centroid[1] - np.mean(y)
			to.centroids.append(centroid)
			# check to see if the object has been counted or not
			if not to.counted:
				# if the direction is negative (indicating the object
				# is moving up) AND the centroid is above the center
				# line, count the object
				if direction < 0 and centroid[1] < H // 2:
					totalUp += 1
					to.counted = True
				# if the direction is positive (indicating the object
				# is moving down) AND the centroid is below the
				# center line, count the object
				elif direction > 0 and centroid[1] > H // 2:
					totalDown += 1
					to.counted = True
		# store the trackable object in our dictionary
		trackableObjects[objectID] = to
		# draw both the ID of the object and the centroid of the
		# object on the output frame
		text = "ID {}".format(objectID)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
	# construct a tuple of information we will be displaying on the
	# frame
	info = [
		("Up", totalUp),
		("Down", totalDown),
		("Status", status),
	]
	# loop over the info tuples and draw them on our frame
	for (i, (k, v)) in enumerate(info):
		text = "{}: {}".format(k, v)
		cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
			cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
	# check to see if we should write the frame to disk
	if writer is not None:
		writer.write(frame)
	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
	# increment the total number of frames processed thus far and
	# then update the FPS counter
	totalFrames += 1
	fps.update()
	schedule.run_pending()
# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

# check to see if we need to release the video writer pointer
if writer is not None:
	writer.release()

# if we are not using a video file, stop the camera video stream
vs.stop()

# close any open windows
cv2.destroyAllWindows()