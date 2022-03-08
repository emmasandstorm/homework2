def doubler(func):
	def wrapper():
		print("Fxn called once")
		func()
		print("Fxn called twice")
		func()
	return wrapper

