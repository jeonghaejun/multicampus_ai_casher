import mysql.connector
from . config.txt import conn


def lambda_handler(event, context) : 
    data         = json.loads(event["body"])
    student_name = body["username"]
    student_pw   = body["password"]




cursor = conn.cursor()
cursor.execute(f"""INSERT INTO users (name, password) VALUES ({student_name}, {student_pw})""")
conn.commit()