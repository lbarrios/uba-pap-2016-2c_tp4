#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

# Global variables
historical_count = 0
enemies_count = 0
historical_points = []
enemies_points = []

#_points_inside_triangle = defaultdict(lambda : defaultdict(dict))
_points_inside_triangle = dict()

#def points_inside_triangle(a,b,c):
#	return _points_inside_triangle[_a][_b][_c]

def parse_input():
	"""
	Parses the input
	"""
	global historical_count,enemies_count,historical_points,enemies_points
	historical_count,enemies_count = map(int,raw_input().split())
	for h in range(historical_count):
		x,y = map(int,raw_input().split())
		historical_points.append(Point(x,y))
	for e in range(enemies_count):
		x,y = map(int,raw_input().split())
		enemies_points.append(Point(x,y))

def precalculate_triangles():
	for p1 in historical_points:
		for p2 in historical_points:
			for p3 in historical_points:
				# check if the triangle is valid
				if p1<p2 and p2<p3:
					t = Triangle(p1,p2,p3)
					
					# if triangle cointains an enemy, it is not valid
					total = 0
					for p in enemies_points:
						if p in t:
							total = -1
					
					if total != -1:
						for p in historical_points:
							if p != p1 and p != p2 and p != p3:
								if p in t:
									total += 1
					
					_points_inside_triangle[t] = total
	print _points_inside_triangle

def print_output():
	print historical_count,enemies_count
	print historical_points
	print enemies_points
	pass

def main():
	parse_input()
	precalculate_triangles()
	#print_output()

class Point:
	""" Point class represents and manipulates x,y coords. """

	def __init__(self,x,y):
		""" Create a new point at the origin """
		self.x = x
		self.y = y

	def __repr__(self):
		return "Point({0},{1})".format(self.x,self.y)

	def __lt__(self, point2):
		if self.x < point2.x:
			return True
		if self.x == point2.x and self.y < point2.y:
			return True
		return False

	def __eq__(self, point2):
		return self.x == point2.x and self.y == point2.y

class Triangle:
	""" Triangle class represents and manipulates 3 points figure. """

	def __init__(self,p1,p2,p3):
		""" Create a new triangle instance """
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3

	def __repr__(self):
		return "Triangle({0},{1},{2})".format(self.p1,self.p2,self.p3)

	def __contains__(self, p):
		if isinstance(p, Point):
			t1 = Triangle(p, self.p1, self.p2)
			t2 = Triangle(p, self.p2, self.p3)
			t3 = Triangle(p, self.p3, self.p1)
			return self.area_X2() == t1.area_X2() + t2.area_X2() + t3.area_X2()
		raise Exception("p parameter has to be a Point")

	def area_X2(self):
		""" given a triangle returns its area * 2
		Area = [ x1(y2 - y3) + x2(y3 - y1) + x3(y1-y2)] / 2
		"""
		a1 = self.p1.x * (self.p2.y - self.p3.y)
		a2 = self.p2.x * (self.p3.y - self.p1.y)
		a3 = self.p3.x * (self.p1.y - self.p2.y)
		return abs(a1+a2+a3)


if __name__ == '__main__':
	main()