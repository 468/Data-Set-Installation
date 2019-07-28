import socket 
from _thread import *
import threading 
import numpy as np
import cv2
import random
import os
from PIL import Image
import sched, time, threading
import socket

screen_res = 1280, 720
path = r"/home/pi/yourfolder/images"

print_lock = threading.Lock()

cv2.namedWindow('dst_rt', cv2.WINDOW_NORMAL)
print('window named')
cv2.setWindowProperty('dst_rt',cv2.WND_PROP_FULLSCREEN,1)
print('setting window property')
current_file = ""
imgFile = cv2.imread(r"")

def grabRandomPhoto():
    random_filename = random.choice([
        x for x in os.listdir(path)
        if not x.startswith('.') and os.path.isfile(os.path.join(path, x))
    ])
    return(random_filename)
 
def displayPhoto(filename):
    print("DISPLAYING PHOTO:" + filename)
    print("DECODED PATH BELOW:")
    path = "/home/pi/final_piece/images/" + filename
    print(path)
    current_file = filename
    imgFile = cv2.imread(r"/home/pi/final_piece/images/" + filename)
    print('photo read')
    cv2.imshow('dst_rt', imgFile)

# thread fuction 
def threaded(c): 
	while True: 
		data = str(c.recv(1024), 'utf-8')
		if not data: 
			print('Bye') 
			print_lock.release() 
			break
		print('got some data')
		if("pick_random_photo_file" in data):
			random_pick = grabRandomPhoto()
			print('sending rand')
			c.send(random_pick.encode('utf-8'))
		elif("play_file" in data):
			filename = data.split("play_file:",1)[1]
			print('playing file')
			print(filename)
			displayPhoto(filename)
			c.send('playing file'.encode('utf-8'))
	c.close() 

def Main(): 
	host = "192.168.0.107" 
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("socket binded to post", port) 

	s.listen(5) 
	print("socket is listening") 

	while True:
		c, addr = s.accept() 
		# lock acquired by client 
		print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 
		# Start a new thread and return its identifier 
		start_new_thread(threaded, (c,)) 
		while True:
			#cv2.imshow('dst_rt', imgFile)
			cv2.waitKey(0)
		
	s.close() 

if __name__ == '__main__': 
	Main() 
