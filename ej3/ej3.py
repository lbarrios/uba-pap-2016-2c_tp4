#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict

# Global variables
historical_count = 0
enemies_count = 0
historical_points = []
enemies_points = []

_points_inside_triangle = dict()

_calculated_best_polygon_for_first_triangle = dict()
_best_polygon_for_first_triangle = dict()

def parse_input():
	"""
	Parses the input
	"""
	global historical_count,enemies_count,historical_points,enemies_points
	historical_count,enemies_count = map(int,raw_input().split())
	for h in range(historical_count):
		x,y = map(int,raw_input().split())
		historical_points.append(Point(x,y))
	historical_points.sort()
	for e in range(enemies_count):
		x,y = map(int,raw_input().split())
		enemies_points.append(Point(x,y))
	enemies_points.sort()

def precalculate_triangles():
	global _calculated_best_polygon_for_first_triangle
	for p1 in historical_points:
		for p2 in historical_points:
			for p3 in historical_points:
				# check if the triangle is valid
				if p1<p2 and p2<p3:
					t = Triangle(p1,p2,p3)
					total = 0

					# if triangle cointains an enemy, it is not valid
					for p in enemies_points:
						if p in t:
							total = -1
					
					# if triangle does not contains an enemy, calculates the historical points count
					if total != -1:
						for p in historical_points:
							if p != p1 and p != p2 and p != p3:
								if p in t:
									total += 1
					
					_points_inside_triangle[t] = total
					_calculated_best_polygon_for_first_triangle[t] = False

def print_output():
	print historical_count,enemies_count
	print historical_points
	print enemies_points
	pass

def best_polygon_for_pivot(p1):
	best = 0
	for p2 in historical_points:
		for p3 in historical_points:
			if p1<p2 and p2<p3:
				t = Triangle(p1,p2,p3)
				b = best_polygon_for_first_triangle(t)
				best = b if b > best else best
	return best

def best_polygon_for_first_triangle(t):
	if _calculated_best_polygon_for_first_triangle[t]:
		return _best_polygon_for_first_triangle[t]
	if _points_inside_triangle == -1:
		_best_polygon_for_first_triangle[t] = -1
		_calculated_best_polygon_for_first_triangle[t] = True
		return _best_polygon_for_first_triangle[t]
	p2,p3 = t.p2,t.p3
	# Recorro todos los puntos a la derecha de estos puntos, 
	# que puedan formar triàngulos con los dos puntos de màs a la derecha de este triàngulo

class Point:
	""" Point class represents and manipulates x,y coords. """

	def __init__(self,x,y):
		""" Create a new point at the origin """
		self.x = x
		self.y = y

	def __repr__(self):
		return "Point({0},{1})".format(self.x,self.y)

	def __hash__(self):
		return hash((self.x,self.y))

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

	#def __hash__(self):
	#	return hash("({0},{1},{2})".format(self.p1, self.p2, self.p3))

	def __init__(self,p1,p2,p3):
		""" Create a new triangle instance """
		points = [p1,p2,p3]
		points.sort()
		self.p1 = points[0]
		self.p2 = points[1]
		self.p3 = points[2]

	def __repr__(self):
		return "Triangle({0},{1},{2})".format(self.p1,self.p2,self.p3)

	def __hash__(self):
		return hash((self.p1,self.p2,self.p3))

	def __eq__(self, t2):
		return self.p1==t2.p1 and self.p2==t2.p2 and self.p3==t2.p3 

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

def main():
	parse_input()
	precalculate_triangles()
	best_polygon = 2 # the minimum best polygon is a triangle with two points inside
	for pivot in historical_points:
		actual_polygon = best_polygon_for_pivot(pivot)
		best_polygon = actual_polygon if (actual_polygon>best_polygon) else best_polygon
	#print_output()

if __name__ == '__main__':
	main()