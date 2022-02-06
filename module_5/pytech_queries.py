"""
Jonathan Moore 30JAN2022 m5.3 assignment
this module queries the database using find and find_one
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

    print("\n- - DISPLAYING STUDENT DOCUMENT FROM THE find_one() QUERY - -")
    result = students.find_one({"student_id": 1007})
    print(f"Student ID: {result['student_id']}")
    print(f"First Name: {result['first_name']}")
    print(f"Last Name: {result['last_name']}")
except Exception as e:
    print(e)
