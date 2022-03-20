# haversine API python command line wrapper and client

This is a simple python wrapper around the excellent new haversine waypoint REST API
can be used from within python or from the unix command line (cygwin as well)

# install

pip3 install --upgrade HaversineAPI


# help

```
$ haversine.py -h

usage: haversine.py [-h] {Haversine,waypoints,routes,args} ...

positional arguments:
  {Haversine,waypoints,routes,args}
                        commands
    Haversine           wrapper around the most excellent REST API for
                        waypoints by joao @ haversine
                        https://haversine.com/webapi
    waypoints           wrapper around the most excellent REST API for
                        waypoints by joao @ haversine
                        https://haversine.com/webapi
    routes              wrapper around the most excellent REST API for routes
                        by joao @ haversine https://haversine.com/webapi
    args                print the values for the args

optional arguments:
  -h, --help            show this help message and exit
```

___

# jupyter

[Jupyter Notebook](https://jupyter.org/)

if you like jupyter notebook, you can see some python examples of how to get routes and waypoints
[HaversineAPI.ipynb](HaversineAPI.ipynb)

there is also a Flight Plan converter that will read an x-plane FMS file and upload it to navigraph, great for batch uploads.
[Flight Plans.ipynb](Flight Plans.ipynb)

___

# waypoints

```
$ haversine.py waypoints -h

usage: haversine.py waypoints [-h] [--hostname HOSTNAME] [-i]
                              [--password PASSWORD] [--username USERNAME] [-v]
                              {create,delete,get,list,update} ...

positional arguments:
  {create,delete,get,list,update}
                        operations
    create              create a single waypoint
    delete              delete a single waypoint by id
    get                 get a single waypoint by id, todo
    list                return the full list of waypoints in json format
    update              update a single waypoint

optional arguments:
  -h, --help            show this help message and exit
  --hostname HOSTNAME   default=https://haversine.com
  -i, --insecure        use insecure mode for old clients with old cert trees,
                        will remove later, developing on Pythonista
  --password PASSWORD   obtained from credstash, AWS dynamodb and crypto keys
  --username USERNAME   default=eddo888
  -v, --verbose         display verbose output
```

## create

```
$ haversine.py waypoints create -h

usage: haversine.py waypoints create [-h] [-e ELEVATION]
                                     id description latitude longitude

positional arguments:
  id                    The point ID, max 7 chars
  description           The point description, max 63 chars
  latitude              y=DDD.DDDDDDD
  longitude             x=DDD.DDDDDDD

optional arguments:
  -h, --help            show this help message and exit
  -e ELEVATION, --elevation ELEVATION
                        EEEE.EEEE in feet, type=float
```

## update

```
$ haversine.py waypoints update -h

usage: haversine.py waypoints update [-h] [-e ELEVATION]
                                     id description latitude longitude

positional arguments:
  id                    The point ID, max 7 chars
  description           The point description, max 63 chars
  latitude              y=DDD.DDDDDDD
  longitude             x=DDD.DDDDDDD

optional arguments:
  -h, --help            show this help message and exit
  -e ELEVATION, --elevation ELEVATION
                        EEEE.EEEE in feet, type=float
```

## list

```
$ haversine.py waypoints list

[
	{
		"id": "0MTB",
		"description": "Mt Blanc",
		"latitude": 45.832119,
		"longitude": 6.865575,
		"elevation": 0.0
	},
	{
		"id": "0A51",
		"description": "Area 51",
		"latitude": 37.233333,
		"longitude": -115.808333,
		"elevation": 0.0
	},
	...
]
```

## get

```
$ haversine.py waypoints get -h

usage: haversine.py waypoints get [-h] id

positional arguments:
  id          The point ID, max 7 chars

optional arguments:
  -h, --help  show this help message and exit
```

## delete

```
$ haversine.py waypoints delete -h

usage: haversine.py waypoints delete [-h] id

positional arguments:
  id          The point ID, max 7 chars

optional arguments:
  -h, --help  show this help message and exit
```

___

# routes

```
$ haversine.py routes -h

usage: haversine.py routes [-h] [--hostname HOSTNAME] [-i]
                           [--password PASSWORD] [--username USERNAME] [-v]
                           {create,delete,get,list,sample,suggest,update} ...

positional arguments:
  {create,delete,get,list,sample,suggest,update}
                        operations
    create              create a new route, format as follows;
    delete              delete an existing route
    get                 get a single route by name, reads whole list and
                        filters
    list                get routes, bit broken at the moment
    sample              provide a sample route to be populated and used to
                        create/update a route
    suggest             find a route from the origin to the destination
    update              update an existing route, I'm doing it now Sybil

optional arguments:
  -h, --help            show this help message and exit
  --hostname HOSTNAME   default=https://haversine.com
  -i, --insecure        use insecure mode for old clients with old cert trees,
                        will remove later, developing on Pythonista
  --password PASSWORD   obtained from credstash, AWS dynamodb and crypto keys
  --username USERNAME   default=eddo888
  -v, --verbose         display verbose output
```

## sample

```
$ haversine routes sample

{
	"name": "STRING (63)\tA name for the route; it's unique key",
	"origin": "STRING (7)\tThe name of the first waypoint; typically the airport's ICAO",
	"departure_runway": "STRING (7)\tMay be NULL; otherwise the departire runway ID",
	"sid": "STRING (15)\tMay be NULL or SID (departure) identifier",
	"path": "STRING\t\tMay be NULL or empty, the sequence of points and airways along the route excluding procedures, runways and airports",
	"destination": "STRING (7)\tThe destination waypoint ID, typically the airport's ICAO",
	"star": "STRING (15)\tMay be NULL or STAR(arrival) identifier",
	"approach": "STRING (15)\tMay be NULL or IAP (approach) identifier",
	"arrival_runway": "STRING (7)\tMay be NULL; otherwise the arrival runway ID",
	"length": "DOUBLE\t\tThe calculated route length, may be incorrect and/or not precise, ROM",
	"flight_level": "INT\t\t\tIf specified (non NULL), the desired flight level in feet MSL, e.g. 35000 for FL350",
	"climb_descent_tas": "INT\t\t\tIf specified (non NULL), the climb and descent speed in knots of true air speed (TAS)",
	"vertical_speed_fpm": "INT\t\t\tIf specified (non NULL), the climb and descent vertical speed in feet per minute, e.g. 1800",
	"points ": [
		{
			"id": "STRING (7)\tPoint identifier",
			"type": [
				"one of the following;",
				"APT = Airport",
				"RW  = Runway",
				"ILS = ILS or localizer",
				"VOR = VOR navaid",
				"NDB = Enroute or Terminal NDB",
				"FIX = Enroute or Terminal Waypoint",
				"LOC = Locality",
				"CWP = Custom Waypoint",
				"POS = Position, a set of coordinates"
			],
			"latitude": "DOUBLE\t\tLatitude",
			"longitude": "DOUBLE\t\tLatitude",
			"elevation": "DOUBLE\t\tElevation in feet MSL at which to cross or NULL (if unspecified)"
		}
	]
}
```

## suggest

```
$ haversine.py routes suggest -h

usage: haversine.py routes suggest [-h] [-f] [-o OUTPUT] origin destination

find a route from the origin to the destination

positional arguments:
  origin                ICAO of origin
  destination           ICAO of destination

optional arguments:
  -h, --help            show this help message and exit
  -f, --first           take first suggestion and convert to importable route
  -o OUTPUT, --output OUTPUT
                        output to file name, null for stdout

```

## create

```
$ haversine.py routes create -h

usage: haversine.py routes create [-h] [-r ROUTE]

optional arguments:
  -h, --help            show this help message and exit
  -r ROUTE, --route ROUTE
                        file with json route, or None for stdin
                        
```

## update
work in progress

```
$ haversine.py routes update -h

usage: haversine.py routes update [-h] [--points POINTS]
                                  name origin destination

positional arguments:
  name
  origin
  destination

optional arguments:
  -h, --help       show this help message and exit
  --points POINTS
```

## list

```
$ haversine.py routes list 

[
	{
		"name": "EGLL-LFPG",
		"origin": "EGLL",
		"destination": "LFPG",
		"departure_runway": "09L",
		"sid": "MAY2K / 09L",
		"path": "MAY BIBAX",
		"star": null,
		"approach": "I08R / MOP6E",
		"arrival_runway": "08L",
		"length": 202.3582316939304,
		"flight_level": 10000,
		"climb_descent_tas": 300,
		"vertical_speed_fpm": 1800,
		"points": [
			{
				"id": "EGLL",
				"type": "APT",
				"latitude": 51.4775,
				"longitude": -0.4613888888888889,
				"elevation": 83.0
			},
			...
			{
				"id": "LFPG",
				"type": "APT",
				"latitude": 49.00972222222222,
				"longitude": 2.547777777777778,
				"elevation": 392.0
			}
		]
	}
]
```
```

## delete

```
$ haversine routes delete -h

usage: haversine.py routes delete [-h] name

positional arguments:
  name

optional arguments:
  -h, --help  show this help message and exit
  
```
