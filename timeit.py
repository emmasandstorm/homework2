import time

def calculate_time(time):
	time_start = int(time())
	time_end = int(time())
	total_time = time_end - time_start
	print ('Total time', total_time)

calculate_time(time.time)
