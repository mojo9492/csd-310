"""
Jonathan Moore 06FEB2022 m6.2 assignment
this module queries the database using find and update one
"""
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.qyihp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students


try:
    print("\n- - DISPLAYING STUDENT DOCUMENTS FROM THE find() QUERY - -")
    results = students.find({})
    for result in results:
        print(f"Student ID: {result['student_id']}")
        print(f"First Name: {result['first_name']}")
        print(f"Last Name: {result['last_name']}")

    result = students.update_one({"student_id": 1007}, {"$set": {"last_name": "Bestboisen"}})
    print("\n- - DISPLAYING STUDENT DOCUMENT 1007 - -")
    result = students.find_one({"student_id": 1007})
    print(f"Student ID: {result['student_id']}")
    print(f"First Name: {result['first_name']}")
    print(f"Last Name: {result['last_name']}")
except Exception as e:
    print(e)
