def sort_list():
	list_f = [90, 70, 31, 32, 33, 10, 11, 93, 105]


	n = len(list_f)
	print("Input:", list_f)
	print("The list length", n)

	hold = 0
	i = 0
	j = 0

	while i < n:
		while j < n-i-1:
			if list_f[j] > list_f[j+1]:
				hold = list_f[j]
				list_f[j] = list_f[j+1]
				list_f[j+1] = hold
			j += 1
		i = i+1
		j = 0
	print("Output:", list_f)


sort_list()
