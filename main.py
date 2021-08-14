from models.Station import Station
from models.Station2 import Station2

stations = Station.all()

print(stations.serialize())
# []

# Creating a station directly calling the properties

station_model = Station()
station_model.name = "Station1"
station_model.ip = "127.0.0.1"
saved_station = station_model.save().fresh()
print(saved_station.serialize())
# {'id': 1, 'name': 'Station1', 'ip': 2130706433, 'created_at': '2021-08-14T22:10:35+00:00', 'updated_at': '2021-08-14T22:10:35+00:00'}

print(Station2.first().serialize())
# {'id': 1, 'name': 'Station1', 'ip': 2130706433, 'created_at': '2021-08-14T22:20:30+00:00', 'updated_at': '2021-08-14T22:20:30+00:00', 'ip_address': IPv4Address('127.0.0.1')}

# Creating a station with the method (create)

new_station = Station.create(
   name="Station2",
   ip="192.168.100.1"
).fresh()
# masoniteorm.exceptions.QueryException: (1265, "Data truncated for column 'ip' at row 1")

print(Station.first().ip)
# RecursionError: maximum recursion depth exceeded while calling a Python object

print(Station2.first().ip_address)
# "127.0.0.1"
