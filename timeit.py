import time

def calculate_time(func):
    def wrapper():
        time_start = time.time()
        time_end = time.time()
        total_time = time_end - time_start
        print ('Total time', total_time)
    return wrapper

@calculate_time
def print_time():
    print ('Total time')
    
print_time()
