def doubler(func):
	def wrapper():
		print("Fxn called once")
		func()
		print("Fxn called twice")
		func()
	return wrapper

def value(x=10,y=10):
	print(x+y)

value = doubler(value)
value()
