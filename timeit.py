import time

def calculate_time(func):
	def wrapper():
        	time_start = time.time()
		func()
		time_end = time.time()
		total_time = time_end - time_start
		print ('Total time', total_time)
	return wrapper

@calculate_time
def function():
	n = 0
	while n < 1000:
		n +=1

function()
