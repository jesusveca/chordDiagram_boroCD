import json
from pprint import pprint
import csv
import sys

data = json.load(open('community_districts.json'))
number_of_community_districts = len(data["features"])
#
f = open("times_boroughCD_to_other.csv", 'wt')
writer = csv.writer(f)
writer.writerow( ('id','number_boroughCD', 'Times') )
#
#
# #
for x in range(number_of_community_districts):
    number_of_boroughCD = data["features"][x]["properties"]["BoroCD"]
    id_number_of_boro = data["features"][x]["id"]
    data_coordinates = data["features"][x]["geometry"]["coordinates"]
    print "number: "
    print number_of_boroughCD
    pprint (data_coordinates[0][0])
    # for element in data_coordinates[0]:
    #     print element
    # print "\n \n"
    # writer.writerow( (id_number_of_boro,number_of_boroughCD,  0))
#


#
# with open('community_board_by_borough.csv') as File:
#     reader = csv.reader(File)
#     for row in reader:
#         data_boroCD = row[0]
#         data_boroName = row[1]
#         data_names = row[2]
#         print data_boroCD + "   "+ data_boroName+ "     "+ data_names
