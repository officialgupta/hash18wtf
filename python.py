f = open('a_example.in')
yourList = f.readlines()
# yourList = [line.rstrip('\n') for line in f]

details = yourList[:]
details = details[:1]
rides = yourList[1:]

details = details[0].split()

print 'details'
print details

print 'rides'
for a in rides:
	a = a.split()
	print a

