def sort_list(list):
	
	n = len(list)
	print("Input:", list)
	print("The list length", n)

	hold = 0
	i = 0
	j = 0

	while i < n:
		while j < n-i-1:
			if list[j] > list[j+1]:
				hold = list[j]
				list[j] = list[j+1]
				list[j+1] = hold
			j += 1
		i = i+1
		j = 0
	print("Output:", list)
	return list


sort_list([1,2,3,1,0,0])
