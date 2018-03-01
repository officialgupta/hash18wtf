import math
import numpy as np
import operator

fname = "d"

class Ride(object):
	def __init__(self, number, start_r, start_c, end_r, end_c, start_t, finish_t):
		self.number = number
		self.start_pos = np.array((start_r, start_c))
		self.end_pos = np.array((end_r, end_c))
		self.time = np.array((start_t, finish_t))

	def getDistance(self):
		return np.sum(np.abs(self.end_pos - self.start_pos))

	def printCoords(self):
		return "going from %s -> %s" % (self.start_pos, self.end_pos)

	def getStartTime(self):
		return (self.number, self.time[0])


class Car(object):
	def __init__(self):
		self.position = np.array((0,0))
		self.destination = np.array((0,0))
		self.assigned = False
		self.rides_taken = []

	def goTo(self, coords):
		self.destination = np.array(coords)

	def distToRide(self, ride):
		return np.sum(np.abs(self.position - ride.start_pos))

	def takeRide(self, ride):
		if not self.assigned:
			# if ride can be made in time
			if (global_time + self.distToRide(ride) < ride.time[1] - ride.getDistance()):
				# taking this ride
				self.assigned = True
				self.destination = ride.end_pos
				self.rides_taken.append(ride.number)

	def simulate(self):
		p = self.position
		d = self.destination
		if (p.all() == d.all()):
			self.assigned = False
			return True

		# favour x direction
		if d[0] > p[0]:
			p[0] += 1
			return True
		elif d[0] < p[0]:
			p[0] -= 1
			return True

		# move in y direction if able to
		if d[1] > p[1]:
			p[1] += 1
			return True
		elif d[1] < p[1]:
			p[1] -= 1
			return True


global_time = 0

rides = []

with open(fname + ".in", 'r') as f:
	f_lines = f.readlines()

(rows, cols, fleet_n, rides_n, bonus, time_steps) = map(int, tuple(f_lines[0].strip().split()))

curr_ride_no = 0

for line in f_lines[1:]:
	(start_r, start_c, end_r, end_c, start_t, finish_t) = map(int, line.strip().split())
	rides.append(Ride(curr_ride_no, start_r, start_c, end_r, end_c, start_t, finish_t))
	curr_ride_no += 1

rides = sorted(rides, key=lambda x: x.getStartTime()[1])
rides_done = 0

assignments = [[] for n in range(fleet_n)]

split = math.ceil(rides_n / fleet_n)

print("fleet size: %d" % fleet_n)
print("total rides: %d" % rides_n)
print("split: %d" % split)

cars = [Car() for car in range(fleet_n)]

while global_time < time_steps and rides_done < rides_n:
	for i in range(fleet_n):
		car = cars[i]
		if car.takeRide(rides[rides_done]):
			pass
		else:

		car.takeRide()
		car.simulate()
		rides_done += 1


# print(assignments[:10])

with open(fname + ".out", 'w') as f:
	for car in cars:
		rides_taken = car.rides_taken
		f.write("%d %s\n" % (len(rides_taken), " ".join(map(str, rides_taken))))
