import pymysql
import json
import os
import fileinput
import sys

# This script assumes that the appropritate schema for mySQL has been set up/populated and is running

# The fileinput module allows filenames to be read from the command line, for now we will print
import fileinput
for line in fileinput.input(sys.argv[1:]):
    print(line)

# Connection to mySQL, default logins here
mydb = pymysql.connect(host='localhost', user='root',
                       password='', db='carDealership')
cursor = mydb.cursor()

# Contains our query execution, we have nested clauses to meet our conditions
cursor.execute("UPDATE employees SET salePoints = salePoints + 1 WHERE (SELECT model FROM sales INNER JOIN employees ON sales.salesRepresentative = employees.employeeID WHERE sales IN ( SELECT Max(sales) FROM cars ))")

# returns all the fields and rows from the result, so we can iterate over each result
result = cursor.fetchall()

for row in result:
    print(row[0])
