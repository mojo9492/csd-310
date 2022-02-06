"""
Jonathan Moore 06FEB2022 m6.3 assignment
this module queries the database using find, find one, insert one, and delete one
"""
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.qyihp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

students = db.students


try:
    # find all students
    print("\n- - DISPLAYING STUDENT DOCUMENTS FROM THE find() QUERY - -")
    results = students.find({})
    for result in results:
        print(f"Student ID: {result['student_id']}")
        print(f"First Name: {result['first_name']}")
        print(f"Last Name: {result['last_name']}")
    # insert new record
    print("\n- - INSERT STATEMENTS - -")
    result = students.insert_one(
        {"student_id": 1010, "first_name": "Jack", "last_name": "Barker"})
    print(
        f"Inserted student record Jack Barker into the students collection with document id: {result}")
    # find added student
    print("\n- - DISPLAYING STUDENT DOCUMENT FROM THE find_one() QUERY - -")
    result = students.find_one({"student_id": 1010})
    print(f"Student ID: {result['student_id']}")
    print(f"First Name: {result['first_name']}")
    print(f"Last Name: {result['last_name']}")
    # delete added student
    students.delete_one({"student_id": 1010})
    # find all students
    print("\n- - DISPLAYING STUDENT DOCUMENTS FROM THE find() QUERY - -")
    results = students.find({})
    for result in results:
        print(f"Student ID: {result['student_id']}")
        print(f"First Name: {result['first_name']}")
        print(f"Last Name: {result['last_name']}")
except Exception as e:
    print(e)
