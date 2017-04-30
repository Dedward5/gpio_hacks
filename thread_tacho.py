import time
import threading

global last_pulse
last_pulse = time.time()
global pulse_gap
pulse_gap = 1

def get_pulse_gap ():
	global pulse_gap
	global last_pulse
	while True:
		GPIO.wait_for_edge(17, GPIO.RISING)
		time_now = time.time()
		pusle_gap = last_pulse - time_now
		last_pulse = time_now
	

gap_thread = threading.Thread (target=get_pulse_gap, args=())
gap_thread.start()


# get_pulse_gap()


while True:
	#global pulse_gap
	print (pulse_gap)
	print("nothing")

    

