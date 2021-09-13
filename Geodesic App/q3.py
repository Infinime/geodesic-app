import math

# The coordinates must be h, latitude, longitude!!!

a = 6375137
f = 1/298.257223563
e2 = 2*f - f**2


def compute(h, lat, lon):
    h = math.radians(float(h.strip()))
    lat = math.radians(float(lat.strip()))
    lon = math.radians(float(lon.strip()))
    N = a/(1-e2*(math.sin(lat))**2)

    x = (N+h)*math.cos(lat) * math.cos(lon)
    y = (N+h)*math.cos(lat) * math.sin(lon)
    z = (N*(1-e2)+h) * math.sin(lat)

    return (x, y, z)


with open("coordinates.txt", "r+") as f:  # Change the file name here
    lines = f.readlines()
    for line in lines:
        print(compute(line.split(",")[0], line.split(",")[1], line.split(",")[2]))
