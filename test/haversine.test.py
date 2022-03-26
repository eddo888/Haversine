#!/usr/bin/env python3

import os, re, sys, time, json, gc, logging, unittest

sys.path.insert(0, "..") # Adds higher directory to python modules path.
	
from datetime import datetime

from Haversine.haversine import Haversine as HaversineBase
from Haversine.haversine import Waypoints, Routes, args

#________________________________________________________________________________________________
class HaversineTest(unittest.TestCase):

	def setUp(self):
		self.verbose = '-v' in sys.argv
		self.haversine = HaversineBase()

	def tearDown(self):
		del self.haversine
		gc.collect()

	def test_01_commmon_bits(self):
		'''
		test parts of base class
		'''
		if self.verbose:
			print('hostname',haversine.hostname)

		assert self.haversine.hostname.startswith('https://')
				
#________________________________________________________________________________________________
class WaypointTest(unittest.TestCase):
	'''
	args.parse(['waypoints', '-vi', 'list'])
	args.parse(['waypoints', '-vi', 'get', '0EDDO'])
	args.parse(['waypoints', '-vi', 'create', '-h'])	
	args.parse(['waypoints', '-vi', 'create', '0EDDO','daveedson','1.0','2.0'])
 	args.parse(['waypoints', '-vi', 'update', '0EDDO',"dave edson",'2.0','3.0'])
	args.parse(['waypoints', '-vi', 'delete', '0EDDO'])
	'''
	
	id = '0EDDO'
	
	def setUp(self):
		self.verbose = '-v' in sys.argv
		self.waypoints = Waypoints()
		self.waypoints.verbose = False #self.verbose
		#self.waypoints.insecure = True
		self.waypoints.username = 'eddo888'
		with open('.password') as input:
			self.waypoints.password = input.read().rstrip('\n')
		
		
	def tearDown(self):
		del self.waypoints
		gc.collect()

	
	#____________________________________________________________________________________________
	def test_01_waypoint_create_and_get(self):
		'''
		remove any existing waypoint before starting the test
		'''		
		
		if self.waypoints.get(self.id):
			self.waypoints.delete(self.id)
			# give it time to delete
			time.sleep(5)


	#____________________________________________________________________________________________
	def test_02_waypoint_create_and_get(self):
		'''
		create a new waypoint and confirm it can be retrieved with the list
		'''		
		
		waypoint = self.waypoints.create(self.id, 'Dave Edson', 1.0, 2.0)
		if self.verbose:
			print('waypoint',waypoint)

		assert waypoint['id'] == self.id
		assert waypoint['description'] == 'Dave Edson'
		assert waypoint['latitude'] == 1.0
		assert waypoint['longitude'] == 2.0
		assert waypoint['elevation'] == 0.0

		waypoint = self.waypoints.get(self.id)
		if self.verbose:
			print('waypoint',waypoint)

		assert waypoint['id'] == self.id
		assert waypoint['description'] == 'Dave Edson'
		assert waypoint['latitude'] == 1.0
		assert waypoint['longitude'] == 2.0
		assert waypoint['elevation'] == 0.0
		
		
	def test_03_waypoint_update_and_get(self):
		'''
		update and get, presumes test 01 succeeded
		'''
		
		waypoint = self.waypoints.update(self.id, 'David Edson', 2.0, 3.0, elevation=1.0)
		if self.verbose:
			print('waypoint',waypoint)

		assert waypoint['id'] == self.id
		assert waypoint['description'] == 'David Edson'
		assert waypoint['latitude'] == 2.0
		assert waypoint['longitude'] == 3.0
		assert waypoint['elevation'] == 1.0

		waypoint = self.waypoints.get(self.id)
		if self.verbose:
			print('waypoint',waypoint)

		assert waypoint['id'] == self.id
		assert waypoint['description'] == 'David Edson'
		assert waypoint['latitude'] == 2.0
		assert waypoint['longitude'] == 3.0
		assert waypoint['elevation'] == 1.0

		
	def test_04_clean_up_created_waypoint(self):
		'''
		tidy up after ourselves and check it worked
		'''
		
		result = self.waypoints.delete(self.id)
		
		assert result['result'] == 'success'
		
		waypoint = self.waypoints.get(self.id)
		
		assert waypoint == None
		
				
#________________________________________________________________________________________________
class RoutesTest(unittest.TestCase):
	'''
	args.parse(['routes', '-vi', 'list'])
	args.parse(['routes', '-vi', 'get', 'YSSY-YMML'])
	args.parse(['routes', '-vi', 'suggest', 'YSSY', 'YMML'])
	args.parse(['routes', 'sample'])
	args.parse(['routes', 'create', '-h'])
	args.parse(['routes', '-vi', 'suggest', '-fo', '~/Documents/route.json', 'YSSY', 'YMML'])
	args.parse(['routes', '-vi', 'create', '-r', '~/Documents/route.json'])
	args.parse(['routes', '-vi', 'delete', 'YSSY-YMML'])
	'''

	origin='YSSY'
	destination='YMML'
	file = '~/Documents/route.json'
	
					
	def setUp(self):
		self.verbose = '-v' in sys.argv
		self.routes = Routes()
		self.routes.verbose = False #self.verbose
		#self.routes.insecure = True
		self.routes.username = 'eddo888'
		with open('.password') as input:
			self.routes.password = input.read().rstrip('\n')
		self.name=f'{self.origin}-{self.destination}'
				
		
	def tearDown(self):
		del self.routes
		gc.collect()
	
	
	def test_01_remove_any_existing_route(self):
		'''
		delete any previous test data
		'''
		
		if os.path.exists(os.path.expanduser(self.file)):
			os.unlink(os.path.expanduser(self.file))
			
		if self.routes.get(self.name):
			self.routes.delete(self.name)
			# give it time to delete
			time.sleep(5)
			
		
	def test_02_suggest_then_create_and_get_route(self):
		'''
		get a suggested route, then create a route with that and get it back
		'''

		routes = self.routes.suggest(self.origin, self.destination)
		if self.verbose:
			print('routes',routes)
		
		assert routes['result'] == 'success'
		
		route = self.routes.suggest(self.origin, self.destination, first=True, output=self.file)
		if self.verbose:
			print('route',route)

		path = route['path'].split(' ')
		if self.verbose:
			print('path',path)
		assert len(path)

		assert os.path.exists(os.path.expanduser(self.file))
		assert route['name'] == self.name
		
		result = self.routes.create(input=self.file)
		if self.verbose:
			print('result',result)
		
		assert result['result'] == 'success'
		assert result['route']['name'] == self.name
				
		waypoints = result['route']['points']
		assert waypoints[0]['id'] == self.origin
		assert waypoints[-1]['id'] == self.destination
		
		if self.verbose:
			print('waypoints;')
			for index, waypoint in enumerate(waypoints[1:-1]):
				print(index,waypoint)
		
		
	def test_03_create_then_update_route(self):
		'''
		test the create then update of a route, uses same base code
		'''
		path = 'YSSY WOL H65 RAZZI Q29 LIZZI YMML'
		parts = path.split(' ')
		name = f'{parts[0]}-{parts[-1]}'

		if self.verbose:
			print(name)
		if self.routes.get(name):
			self.routes.delete(name)

		result = self.routes.create(path=path)
		if self.verbose:
			print('result',result)

		assert result['result'] == 'success'

		if self.verbose:
			for point in result['route']['points']:
				print(point['id'])
			
		path = 'YSSY WOL YMML'

		result = self.routes.update(path=path)
		if self.verbose:
			print('result',result)

		assert result['result'] == 'success'

		if self.verbose:
			for point in result['route']['points']:
				print(point['id'])

		updated =  ' '.join(map( lambda x: x['id'], result['route']['points']))

		if self.verbose:
			print('updated',updated)
			
		assert updated == path
		
				
	def test_04_clean_up_created_route(self):
		'''
		tidy up after ourselves and check it worked
		'''
		
		result = self.routes.delete(self.name)
		if self.verbose:
			print('result',result)
		assert result['result'] == 'success'
		
		route = self.routes.get(self.name)
		if self.verbose:
			print('route',route)
		assert route == None

		
		
#________________________________________________________________________________________________
if __name__ == '__main__':
	level = logging.INFO
	#level = logging.DEBUG
	logging.basicConfig(level=level)
	unittest.main(exit=True)
