# haversine API python command line wrapper and client

This is a simple python wrapper around the excellent new haversine waypoint REST API
can be used from within python or from the unix command line (cygwin as well)


# help
```
$ ./haversine.py -h

usage: haversine.py [-h] [--hostname HOSTNAME] [--password PASSWORD]
                    [--username USERNAME]
                    {create,delete,get,list,args} ...

positional arguments:
  {create,delete,get,list,args}
                        operations
    create              create or update a single waypoint
    delete              delete a single waypoint by id
    get                 get a single waypoint by id, todo
    list                return the full list of waypoints in json format
    args                print the values for the args

optional arguments:
  -h, --help            show this help message and exit
  --hostname HOSTNAME   default=https://haversine.com
  --password PASSWORD   obtained from credstash, AWS dynamodb and crypto keys
  --username USERNAME   default=eddo888
```

## create
```
$ ./haversine create -h

usage: haversine.py create [-h] [--elevation ELEVATION] [-u]
                           id description latitude longitude

positional arguments:
  id                    The point ID, max 7 chars
  description           The point description, max 63 chars
  latitude              y=DDD.DDDDDDD
  longitude             x=DDD.DDDDDDD

optional arguments:
  -h, --help            show this help message and exit
  --elevation ELEVATION
                        EEEE.EEEE in feet, type=float
  -u, --update          update instead of create
```

## list
```
$ ./haversine.py list

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