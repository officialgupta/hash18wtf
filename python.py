with open('a_example.in', 'r') as f:
	f_lines = f.readlines()
	params = [line.strip().split() for line in f_lines]

	details = params[0]
	rides = params[1:]

	print('details')
	print(details)

	print('rides')
	for a in rides:
		print(a)
