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

# for x in range(size_boroughs):
#     name_borough = data["features"][x]["properties"]["BoroName"]
#     borough_list.append(str(name_borough))
# print borough_list

# for x in range (size_boroughs):
#     for y in range(len(data["features"][x]["geometry"]["coordinates"])): # number of polygons presents in each borough      # each_polygon_on_borough = data["features"][x]["geometry"]["coordinates"][y] # each polygon on a borough
#         polygon_of_each_borough = data["features"][x]["geometry"]["coordinates"][y][0]
#         point_x = -73.985130
#         point_y = 40.758896
#         # print point_in_poly(point_x,point_y,polygon_of_each_borough)
#

contador_staten = 0 # 0
contador_queens = 0 # 1
contador_brooklyn = 0 # 2
contador_manhattan =0 #3
contador_bronx  = 0 # 4


from_staten_to_queens=0
from_staten_to_brooklyn=0
from_staten_to_manhattan=0
from_staten_to_bronx=0

from_queens_to_staten=0
from_queens_to_brooklyn=0
from_queens_to_manhattan=0
from_queens_to_bronx=0

from_brooklyn_to_queens=0
from_brooklyn_to_staten=0
from_brooklyn_to_manhattan=0
from_brooklyn_to_bronx=0

from_manhattan_to_staten=0
from_manhattan_to_brooklyn=0
from_manhattan_to_queens=0
from_manhattan_to_bronx=0

from_bronx_to_staten=0
from_bronx_to_brooklyn=0
from_bronx_to_manhattan=0
from_bronx_to_queens=0

list_to_chord=[]

num = lambda s: eval(s) if not set(s).difference('0123456789. *+-/e') else None

f = open("test.csv", 'wt')
writer = csv.writer(f)
writer.writerow( ('Origin', 'Orig Long' , 'Orig Lat','Dest Long', 'Dest Lat', 'Times') )

with open('sample_merged_1.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        pickup_long = row[2] # x
        pickup_long = num(pickup_long)
        pickup_lat  = row[3] # y
        pickup_lat = num(pickup_lat)

        dropoff_long = row[4] # x
        dropoff_long = num(dropoff_long)
        dropoff_lat  = row[5] # y
        dropoff_lat = num(dropoff_lat)

        for x in range (size_boroughs):
            for y in range(len(data["features"][x]["geometry"]["coordinates"])): # number of polygons presents in each borough      # each_polygon_on_borough = data["features"][x]["geometry"]["coordinates"][y] # each polygon on a borough
                polygon_of_each_borough = data["features"][x]["geometry"]["coordinates"][y][0]
                pprint (polygon_of_each_borough)
                point_x = pickup_long
                point_y = pickup_lat

                point_x2 = dropoff_long
                point_y2 = dropoff_lat

                if point_in_poly(point_x,point_y,polygon_of_each_borough):
                    nombre_from= data["features"][x]["properties"]["BoroName"]
                    print nombre_from+ " "+ str(point_x) + " " + str(point_y)+"     to   "+ str(point_x2)  + " " + str(point_y2)
                    # writer.writerow( (nombre_from,point_x,point_y, point_x2, point_y2,  0))
pprint (list_to_chord)
