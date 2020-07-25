import pymysql
import json
import os

# We are going to read in the JSON file, finding its path, returning a data stream, and loading
readData = os.path.abspath('../../..') + "/inputVehicle.json"
json_data = open(readData).read()
json_obj = json.loads(json_data)

# Here is where data validation will initially occur from our data stream


def validate_string(data):
    if data != None:
        if type(data) is int:
            return str(data).encode('utf-8')
        else:
            return data


# Connection to mySQL, default logins here
con = pymysql.connect(host='localhost', user='root',
                      passwd='', db='carDealership')
cursor = con.cursor()

# Parsing the JSON data, validating it as we go for each column
for i, item in enumerate(json_obj):
    carID = validate_string(item.get("carID", None))
    make = validate_string(item.get("make", None))
    model = validate_string(item.get("model", None))

    # Once we have our extracted data, we can execute this data in a SQL query
    # We can have wildcard character
    cursor.execute(
        "INSERT INTO cars (carID, make, model) VALUES (%s, %s, %s)", (carID, make, model))

# Once we are done we can close our connection
con.commit()
con.close()
