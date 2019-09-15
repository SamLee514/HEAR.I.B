import math

speedOfSound = 343
radius = 6 #inches

#assumes 2 microphones 12 inches apart, with theoretical receiver halfway inbetween

radius_m = radius * 0.0254

def calculate_delay_from_angle(radius, angle):
	return calculate_delays(radius*math.cos(math.radians(angle)), radius*math.sin(math.radians(angle)))
def calculate_delays(x, y):
	return (calc_time(x-radius_m, y), calc_time(x+radius_m, y))
def calc_time(x, y):
	dist = math.sqrt(math.pow(x, 2)+math.pow(y,2))
	return dist/speedOfSound
