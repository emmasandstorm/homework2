def func_counter(func):
	def wrapper(*args):
		wrapper.counter += 1
		return func(*args)
	wrapper.counter = 0
	return wrapper

@func_counter
def foo(y):
	return y+2**3-34

foo(10)
foo(12)
foo(9)

print(foo.counter)
