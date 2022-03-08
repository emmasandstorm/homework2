import time

def calculate_time(func):
	def wrapper():
		time_start = func()
		time_end = func()
		total_time = time_end - time_start
	return wrapper
	print ('Total time', total_time)

