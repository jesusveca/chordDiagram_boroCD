import json
from pprint import pprint
import csv


from_staten_to_staten=0
from_staten_to_queens=0
from_staten_to_brooklyn=0
from_staten_to_manhattan=0
from_staten_to_bronx=0

from_queens_to_queens=0
from_queens_to_staten=0
from_queens_to_brooklyn=0
from_queens_to_manhattan=0
from_queens_to_bronx=0

from_brooklyn_to_brooklyn=0
from_brooklyn_to_queens=0
from_brooklyn_to_staten=0
from_brooklyn_to_manhattan=0
from_brooklyn_to_bronx=0

from_manhattan_to_manhattan=0
from_manhattan_to_staten=0
from_manhattan_to_brooklyn=0
from_manhattan_to_queens=0
from_manhattan_to_bronx=0

from_bronx_to_bronx=0
from_bronx_to_staten=0
from_bronx_to_brooklyn=0
from_bronx_to_manhattan=0
from_bronx_to_queens=0

num = lambda s: eval(s) if not set(s).difference('0123456789. *+-/e') else None



with open('from_to_work.csv') as File:
    reader = csv.reader(File)
    for row in reader:
        origin = row[0]
        destination = row[3]

        if origin == "Staten Island":
            if destination == "Queens":
                from_staten_to_queens +=1
            if destination == "Brooklyn":
                from_staten_to_brooklyn +=1
            if destination == "Manhattan":
                from_staten_to_manhattan +=1
            if destination == "Bronx":
                from_staten_to_bronx +=1
            if destination == "Staten Island":
                from_staten_to_staten +=1
        if origin == "Queens":
            if destination == "Staten Island":
                from_queens_to_staten +=1
            if destination == "Brooklyn":
                from_queens_to_brooklyn +=1
            if destination == "Manhattan":
                from_queens_to_manhattan +=1
            if destination == "Bronx":
                from_queens_to_bronx +=1
            if destination == "Queens":
                from_queens_to_queens +=1

        if origin == "Brooklyn":
            if destination == "Queens":
                from_brooklyn_to_queens +=1
            if destination == "Staten Island":
                from_brooklyn_to_staten +=1
            if destination == "Manhattan":
                from_brooklyn_to_manhattan +=1
            if destination == "Bronx":
                from_brooklyn_to_bronx +=1
            if destination == "Brooklyn":
                from_brooklyn_to_brooklyn+=1

        if origin == "Manhattan":
            if destination == "Queens":
                from_manhattan_to_queens +=1
            if destination == "Brooklyn":
                from_manhattan_to_brooklyn +=1
            if destination == "Staten Island":
                from_manhattan_to_staten +=1
            if destination == "Bronx":
                from_manhattan_to_bronx +=1
            if destination == "Manhattan":
                from_manhattan_to_manhattan +=1

        if origin == "Bronx":
            if destination == "Queens":
                from_bronx_to_queens +=1
            if destination == "Brooklyn":
                from_bronx_to_brooklyn +=1
            if destination == "Manhattan":
                from_bronx_to_manhattan +=1
            if destination == "Staten Island":
                from_bronx_to_staten +=1
            if destination == "Bronx":
                from_bronx_to_bronx +=1

print from_staten_to_staten
print from_staten_to_queens
print from_staten_to_brooklyn
print from_staten_to_manhattan
print from_staten_to_bronx
print "\n"

print from_queens_to_queens
print from_queens_to_staten
print from_queens_to_brooklyn
print from_queens_to_manhattan
print from_queens_to_bronx
print "\n"

print from_brooklyn_to_brooklyn
print from_brooklyn_to_queens
print from_brooklyn_to_staten
print from_brooklyn_to_manhattan
print from_brooklyn_to_bronx
print "\n"

print from_manhattan_to_manhattan
print from_manhattan_to_staten
print from_manhattan_to_brooklyn
print from_manhattan_to_queens
print from_manhattan_to_bronx
print "\n"

print from_bronx_to_bronx
print from_bronx_to_staten
print from_bronx_to_brooklyn
print from_bronx_to_manhattan
print from_bronx_to_queens
print "\n"

f = open("borough_trips_count.csv", 'wt')
writer = csv.writer(f)
writer.writerow( ('Origin', 'Destination','Times') )

writer.writerow( ('Staten Island', 'Staten Island',from_staten_to_staten) )
writer.writerow( ('Staten Island', 'Queens',from_staten_to_queens) )
writer.writerow( ('Staten Island', 'Brooklyn',from_staten_to_brooklyn) )
writer.writerow( ('Staten Island', 'Manhattan',from_staten_to_manhattan) )
writer.writerow( ('Staten Island', 'Bronx',from_staten_to_bronx) )

writer.writerow( ('Queens', 'Queens',from_queens_to_queens) )
writer.writerow( ('Queens', 'Staten Island',from_queens_to_staten) )
writer.writerow( ('Queens', 'Brooklyn',from_queens_to_brooklyn) )
writer.writerow( ('Queens', 'Manhattan',from_queens_to_manhattan) )
writer.writerow( ('Queens', 'Bronx',from_queens_to_bronx) )

writer.writerow( ('Brooklyn', 'Brooklyn',from_brooklyn_to_brooklyn) )
writer.writerow( ('Brooklyn', 'Staten Island',from_brooklyn_to_staten) )
writer.writerow( ('Brooklyn', 'Queens',from_brooklyn_to_queens) )
writer.writerow( ('Brooklyn', 'Manhattan',from_brooklyn_to_manhattan) )
writer.writerow( ('Brooklyn', 'Bronx',from_brooklyn_to_bronx) )

writer.writerow( ('Manhattan', 'Manhattan',from_manhattan_to_manhattan) )
writer.writerow( ('Manhattan', 'Staten Island',from_manhattan_to_staten) )
writer.writerow( ('Manhattan', 'Queens',from_manhattan_to_queens) )
writer.writerow( ('Manhattan', 'Brooklyn',from_manhattan_to_brooklyn) )
writer.writerow( ('Manhattan', 'Bronx',from_manhattan_to_bronx) )

writer.writerow( ('Bronx', 'Bronx',from_bronx_to_bronx) )
writer.writerow( ('Bronx', 'Staten Island',from_bronx_to_staten) )
writer.writerow( ('Bronx', 'Queens',from_bronx_to_queens) )
writer.writerow( ('Bronx', 'Brooklyn',from_bronx_to_brooklyn) )
writer.writerow( ('Bronx', 'Manhattan',from_bronx_to_manhattan) )
