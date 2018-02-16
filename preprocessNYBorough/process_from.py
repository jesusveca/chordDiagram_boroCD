import json
from pprint import pprint
import csv
import sys


def point_in_poly(x,y,poly):
    n = len(poly)
    inside = False
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside

data = json.load(open('boroughs.json'))
size_boroughs = len(data["features"])

borough_list = []

num = lambda s: eval(s) if not set(s).difference('0123456789. *+-/e') else None


f = open("from_to.csv", 'wt')
writer = csv.writer(f)
writer.writerow( ('Origin', 'Orig Long' , 'Orig Lat', 'Destination','Dest Long', 'Dest Lat', 'Times') )

with open('from_.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        dropoff_long = row[3] # x
        dropoff_long = num(dropoff_long)
        dropoff_lat  = row[4] # y
        dropoff_lat = num(dropoff_lat)

        for x in range (size_boroughs):
            for y in range(len(data["features"][x]["geometry"]["coordinates"])): # number of polygons presents in each borough      # each_polygon_on_borough = data["features"][x]["geometry"]["coordinates"][y] # each polygon on a borough
                polygon_of_each_borough = data["features"][x]["geometry"]["coordinates"][y][0]
                point_x = dropoff_long
                point_y = dropoff_lat

                if point_in_poly(point_x,point_y,polygon_of_each_borough):
                    nombre_from= data["features"][x]["properties"]["BoroName"]
                    print row[0] +" "+ row[1] +" "+ row[2]+ "  to  "+ nombre_from+ " "+ row[3]+ " "+row[4] + "  0"
                    writer.writerow( (row[0], row[1], row[2], nombre_from, row[3], row[4] ,0))
