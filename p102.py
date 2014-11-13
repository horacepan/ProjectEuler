import pdb
import math

X=0
Y=1

def containsOrigin(p1, p2, p3, tol=1e-6):
# tolerance is a bit iffy. If difference in area is less than tol, then
# the two values should be 0.
	tri_area = area(p1, p2, p3)

	origin = (0,0)
	area1 = area(p1, p2, origin)
	area2 = area(p2, p3, origin)
	area3 = area(p1, p3, origin)
	
	return abs(tri_area-(area1+area2+area3)) < tol
	
def area(p1, p2, p3):
	a = dist(p1, p2)
	b = dist(p2, p3)
	c = dist(p1, p3)
	s = 0.5*(a+b+c)
	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
	return area

def dist(p1, p2):
	x_delta = p1[X] - p2[X]
	y_delta = p1[Y] - p2[Y]
	return math.sqrt(x_delta*x_delta + y_delta*y_delta)

if __name__ == "__main__":
	count = 0
	for line in open('triangles.txt', 'r'):
		coords = map(lambda r: int(r), line[:-1].split(','))
		p1 = (coords[0], coords[1])
		p2 = (coords[2], coords[3])
		p3 = (coords[4], coords[5])

		if containsOrigin(p1,p2,p3):
			count += 1
	print count
