import time

def calculate_time(time):
	time_start = float(time())
	time_end = float(time())
	total_time = time_end - time_start
	print ('Total time', total_time)

calculate_time(time.time)
