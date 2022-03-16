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
    Haversine           wrapper around the most excellent REST API for waypoints by joao @ haversine
    waypoints
    routes
    args                print the values for the args

optional arguments:
-h, --help            show this help message and exit

```

___

# waypoints

```
usage: haversine.py waypoints [-h] [--hostname HOSTNAME] [--password PASSWORD] [--username USERNAME]
                              {create,delete,get,list} ...

positional arguments:
  {create,delete,get,list}
                        operations
    create              create or update a single waypoint
    delete              delete a single waypoint by id
    get                 get a single waypoint by id, todo
    list                return the full list of waypoints in json format

optional arguments:
  -h, --help            show this help message and exit
  --hostname HOSTNAME   default=https://haversine.com
  --password PASSWORD   obtained from credstash, AWS dynamodb and crypto keys
  --username USERNAME   default=eddo888

```

## create

```
$ haversine.py waypoints create -h
usage: haversine.py waypoints create [-h] [-e ELEVATION] [-u] id description latitude longitude

create or update a single waypoint

positional arguments:
  id                    The point ID, max 7 chars
  description           The point description, max 63 chars
  latitude              y=DDD.DDDDDDD
  longitude             x=DDD.DDDDDDD

optional arguments:
  -h, --help            show this help message and exit
  -e ELEVATION, --elevation ELEVATION
                        EEEE.EEEE in feet, type=float
  -u, --update          update instead of create

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

get a single waypoint by id, todo

positional arguments:
  id          The point ID, max 7 chars

optional arguments:
  -h, --help  show this help message and exit

```

## delete

```
$ haversine.py waypoints delete -h
usage: haversine.py waypoints delete [-h] id

delete a single waypoint by id

positional arguments:
  id          The point ID, max 7 chars

optional arguments:
  -h, --help  show this help message and exit

```

___

# routes

```
$ haversine.py routes -h
usage: haversine.py routes [-h] [--hostname HOSTNAME] [--password PASSWORD] [--username USERNAME] {list} ...

positional arguments:
  {list}               operations
    list               get routes, bit broken at the moment

optional arguments:
  -h, --help           show this help message and exit
  --hostname HOSTNAME  default=https://haversine.com
  --password PASSWORD  obtained from credstash, AWS dynamodb and crypto keys
  --username USERNAME  default=eddo888

```

## list

this looks to be work in progress

```
$ haversine.py routes list 
...
```

## create

todo

## delete

todo
