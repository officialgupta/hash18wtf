f = open('a_example.in')
yourList = f.readlines() # returns a list of lines
# yourList = [line.rstrip('\n') for line in f]

details = yourList[:] # copy
details = details[:1] # first element(line) (string)
rides = yourList[1:] # the rest

details = details[0].split() # list

print 'details'
print details

print 'rides'
for a in rides:
	a = a.split()
	print a
