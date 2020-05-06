# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE

# recieve lat lon args


class LatLon:

    location_num = 0

    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

        LatLon.location_num += 1


newLL = LatLon(2,2)
print(LatLon.location_num)
print(newLL.__dict__)

newLL.lat = 500
print(newLL.__dict__)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# extends LatLon, adds name args
# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name


newWP = Waypoint(10, 10, "Nic")
print(newWP.__dict__)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty

newGeo = Geocache(50, 50, "GEO", "Hard")
print(newGeo.__dict__)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print(waypoint.__dict__)


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print('string:', waypoint.__str__())

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5)
# Print it--also make this print more nicely
print(geocache.__dict__)
print('Number of Locations:', LatLon.location_num)
