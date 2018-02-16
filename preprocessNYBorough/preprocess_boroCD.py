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


num = lambda s: eval(s) if not set(s).difference('0123456789. *+-/e') else None

data = json.load(open('community_districts.json'))
number_of_community_districts = len(data["features"])


# f = open("13_febrero_communi_distric_NY.csv", 'wt')
# writer = csv.writer(f)
# writer.writerow( ('id_origin', 'orig_long' , 'orig_lat','dest_long', 'dest_lat') )

#
# with open('sample_merged_1.csv') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         pickup_long = row[2] # x
#         pickup_long = num(pickup_long)
#         pickup_lat  = row[3] # y
#         pickup_lat = num(pickup_lat)
#
#         dropoff_long = row[4] # x
#         dropoff_long = num(dropoff_long)
#         dropoff_lat  = row[5] # y
#         dropoff_lat = num(dropoff_lat)
#
#         contador = 0
#         for x in range (number_of_community_districts):
#             for y in range(len(data["features"][x]["geometry"]["coordinates"])): # number of polygons presents in each borough      # each_polygon_on_borough = data["features"][x]["geometry"]["coordinates"][y] # each polygon on a borough
#                 size_of_each_polygon = len(data["features"][x]["geometry"]["coordinates"])
#                 polygon_of_each_borough = data["features"][x]["geometry"]["coordinates"][y]
#
#                 point_x = pickup_long
#                 point_y = pickup_lat
#                 if size_of_each_polygon==1:
#                     if point_in_poly(point_x,point_y,polygon_of_each_borough):
#                         id_origin = data["features"][x]["properties"]["BoroCD"]
#                         writer.writerow( (id_origin,point_x,point_y, dropoff_long, dropoff_lat))
#                 else:
#                     for m in polygon_of_each_borough:
#                         if point_in_poly(point_x,point_y,m):
#                             id_origin = data["features"][x]["properties"]["BoroCD"]
#                             writer.writerow( (id_origin,point_x,point_y, dropoff_long, dropoff_lat))



# f = open("13_febrero_destino_communi_distric_NY.csv", 'wt')
# writer = csv.writer(f)
# writer.writerow( ('id_origin', 'orig_long' , 'orig_lat','espacio','id_destino','dest_long', 'dest_lat') )
#
#
# with open('13_febrero_communi_distric_NY.csv') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         id_origin = row[0]
#         pickup_long = row[1] # x
#         pickup_long = num(pickup_long)
#         pickup_lat  = row[2] # y
#         pickup_lat = num(pickup_lat)
#
#         dropoff_long = row[3] # x
#         dropoff_long = num(dropoff_long)
#         dropoff_lat  = row[4] # y
#         dropoff_lat = num(dropoff_lat)
#
#
#         for x in range (number_of_community_districts):
#             for y in range(len(data["features"][x]["geometry"]["coordinates"])): # number of polygons presents in each borough      # each_polygon_on_borough = data["features"][x]["geometry"]["coordinates"][y] # each polygon on a borough
#                 size_of_each_polygon = len(data["features"][x]["geometry"]["coordinates"])
#                 polygon_of_each_borough = data["features"][x]["geometry"]["coordinates"][y]
#
#                 point_x = dropoff_long
#                 point_y = dropoff_lat
#                 if size_of_each_polygon==1:
#                     if point_in_poly(point_x,point_y,polygon_of_each_borough):
#                         id_destino = data["features"][x]["properties"]["BoroCD"]
#                         # print "size 1"
#                         # print id_destino
#                         writer.writerow( (id_origin,point_x,point_y,"       ", id_destino, dropoff_long, dropoff_lat))
#                 else:
#                     for m in polygon_of_each_borough:
#                         if point_in_poly(point_x,point_y,m):
#                             id_destino = data["features"][x]["properties"]["BoroCD"]
#                             # print "size <1"
#                             # print id_destino
#                             writer.writerow( (id_origin,point_x,point_y,"       ", id_destino, dropoff_long, dropoff_lat))


# # sort all the origins values in a new csv
# with open('13_febrero_destino_communi_distric_NY.csv') as sample, open('randomized.csv', "w") as out:
#     csv1=csv.reader(sample)
#     header = next(csv1, None)
#     csv_writer = csv.writer(out)
#     if header:
#         csv_writer.writerow(header)
#     csv_writer.writerows(sorted(csv1, key=lambda x:int(x[0])))
#
#

# f = open("13_febrero_test.csv", 'wt')
# writer = csv.writer(f)
# writer.writerow( ('id_origin', 'id_destino') )

# def count(sequence, item):
#     cont=0
#     for i in sequence:
#         if item==i:
#             cont+=1
#     return cont




##count all the boroCD origin to boroCD destination
# str_general = ""
# list_str_boroCD = []
#
# with open('13_febrero_test.csv') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         str_to = (row)
#         list_str_boroCD.append(str_to)
#         str_general+=str(row)+'\n'
#
#
#
# f = open("14_febrero_count_boroCD_to_boroCD.csv", 'wt')
# writer = csv.writer(f)
# writer.writerow( ('id_origin', 'id_destino', 'times') )
#
# for element in list_str_boroCD:
#     str_origin = element[0]
#     str_destination = element[1]
#     counter = str_general.count(str(element))
#     writer.writerow( (str_origin, str_destination, counter) )



list_to_delete_and_copy_to_final_csv = []

with open('14_febrero_count_boroCD_to_boroCD.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        list_to_delete_and_copy_to_final_csv.append(row)


# b_set = set(map(tuple,list_to_delete_and_copy_to_final_csv))  #need to convert the inner lists to tuples so they are hashable
# b = map(list,b_set)
#
# b.sort(key = lambda x: list_to_delete_and_copy_to_final_csv.index(x) )
# pprint (b)





# b = list()
# for sublist in list_to_delete_and_copy_to_final_csv:
#     if sublist not in b:
#         b.append(sublist)







#
# f = open("14_febrero_Nombres_FINAL_boroCD.csv", 'wt')
# writer = csv.writer(f)
# writer.writerow( ('id_origin', 'id_destino', 'times') )
#
#
#
#
# with open('14_febrero_FINAL_boroCD.csv') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         nombre_origin = row[0]
#         nombre_destinatio = row[1]
#
#         with open('community_board_by_borough.csv') as F:
#             other_reader = csv.reader(F)
#             for row_1 in other_reader:
#                 str_final_1 = ""
#                 str_final_2 = ""
#                 if nombre_origin == row_1[0] :
#                     str_final_1 = row_1[0] + " /" + row_1[1] + "/" + row_1[2]
#                     writer.writerow( (str_final_1, nombre_destinatio, row[2]) )


#
f = open("14_febrero_Nombres_F_FINAL_FINAL_boroCD.csv", 'wt')
writer = csv.writer(f)
writer.writerow( ('id_origin', 'id_destino', 'times') )

with open('14_febrero_Nombres_FINAL_boroCD.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        nombre_origin = row[0]
        nombre_destinatio = row[1]
        print row
        with open('community_board_by_borough.csv') as F:
            other_reader = csv.reader(F)
            for row_1 in other_reader:
                str_final_1 = ""
                str_final_2 = ""
                if nombre_destinatio == row_1[0] :
                    str_final_1 = row_1[0] + " /" + row_1[1] + "/" + row_1[2]
                    writer.writerow( (row[0], str_final_1, row[2]) )
