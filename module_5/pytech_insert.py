"""
Jonathan Moore 30JAN2022 m5.3 assignment
this module inserts students into the database
"""
from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.qyihp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

studentsCollection = db.students
# delete all students
studentsCollection.delete_many({})
# insert new students function

def insert_student(student_id, first_name, last_name):
    try:
        document_id = studentsCollection.insert_one({"student_id": student_id, "first_name": first_name, "last_name": last_name}).inserted_id
        print(f"Inserted student record {first_name} {last_name} into the students collection with document id: {document_id}")
    except Exception as e:
        print(e)

student_id = 1007
print("- - INSERT STATEMENTS - -")
insert_student(student_id, "Jobi", "Bober")
student_id += 1
insert_student(student_id, "Xena", "Beans")
student_id += 1
insert_student(student_id, "Geeter", "Oglethorpe")
