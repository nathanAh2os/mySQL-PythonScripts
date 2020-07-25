import pymysql
import json
import os

# This script assumes that the appropritate schema for mySQL has been set up/populated and is running

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
