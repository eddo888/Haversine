#!/usr/bin/env python3

import os, re, sys, time, json, gc, logging, unittest

if '..' not in sys.path:
	sys.path.append("..") # Adds higher directory to python modules path.
	
from datetime import datetime

from Haversine.haversine import Waypoints, Routes, args

class WaypointTest(unittest.TestCase):

	def setUp(self):
		self.waypoints = Waypoints()
		self.waypoints.username = 'eddo888'
		self.waypoints.password = open('.password').read()
		
		
	def tearDown(self):
		del self.waypoints
		gc.collect()

	#args.parse(['waypoints','list'])
	#args.parse(['waypoints','create','-h'])
	#args.parse(['waypoints','create','0EDDO','daveedson','1.0','2.0'])
	#args.parse(['waypoints','create','-u','0EDDO',"dave edson",'2.0','3.0'])
	#args.parse(['waypoints','delete','0EDDO'])
	#args.parse(['waypoints','get','0EDDO'])

	#args.parse(['routes','suggest','YSSY','YMML'])
	#args.parse(['routes','list'])

	
	#____________________________________________________________________________________________
	def test_01_waypoint_create_and_get(self):
		'''
		create a new waypoint and confirm it can be retrieved with the list
		'''
		id = '0EDDO'
		
		if self.waypoints.get(id):
			self.waypoints.delete(id)

		time.sleep(5)

		waypoint = self.waypoints.create(id, 'David Edson', 1.0, 2,0)
		print(waypoint)

		assert waypoint['id'] == id
		assert waypoint['description'] == 'David Edson'
		assert waypoint['latitude'] == 1.0
		assert waypoint['longitude'] == 2.0

		waypoint = self.waypoints.get(id)
		print(waypoint)

		assert waypoint['id'] == id
		assert waypoint['description'] == 'David Edson'
		assert waypoint['latitude'] == 1.0
		assert waypoint['longitude'] == 2.0
		
		
	def _test_02_waypoint_create_and_get_using_args(self):
		'''
		# currently commended by putting a _ at the start of the test name

		create a waypoint and confirm it can be retrieved using command line version
		'''
		id = '0EDDO'

		if self.waypoints.get(id):
			args.parsed = args.parse(['waypoints','delete',id])
			args.execute()

		time.sleep(5)

		args.parsed = args.parse(['waypoints','create',id,'David Edson','1.0','2.0'])
		result = args.execute()
		print(result)
		waypoint = json.loads(result)
		print(waypoint)

		assert waypoint['id'] == id
		assert waypoint['description'] == 'David Edson'
		assert waypoint['latitude'] == 1.0
		assert waypoint['longitude'] == 2.0

		args.parsed = args.parse(['waypoints','get',id])
		wayoint = json.loads(args.execute())
		print(waypoint)

		assert waypoint['id'] == id
		assert waypoint['description'] == 'David Edson'
		assert waypoint['latitude'] == 1.0
		assert waypoint['longitude'] == 2.0

		
#________________________________________________________________________________________________
if __name__ == '__main__':
	level = logging.INFO
	#level = logging.DEBUG
	logging.basicConfig(level=level)
	unittest.main(exit=True)
