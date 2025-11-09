import psycopg2
import datetime

# Information needed to connect to the database
login = {
    "dbname": "assignment3",
    "user": "postgres",
    "password": "password"
}

# Connect to the Database
def connect():
    conn = psycopg2.connect(**login)
    if conn.closed == 0:
        return conn
    else:
        print("CONNECTION ERROR")
        exit(1)

# Prints all rows of the database
def getAllStudents():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students;")
    rows = cur.fetchall()
    print("Students:")
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# Add a Row to the database
def addStudent(first_name, last_name, email, enrollment_date):
    conn = connect()    
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",(first_name, last_name, email, enrollment_date))
    conn.commit()
    print("Student Added")
    cur.close()
    conn.close()

# Alters designated rows email attribute
def updateStudentEmail(student_id, new_email):
    conn = connect()    
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;  ", (new_email, student_id))
    conn.commit()
    print("Email Changed")
    cur.close()
    conn.close()

# Removes designated row from table 
def deleteStudent(student_id):
    conn = connect()    
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    print("Student Removed")
    cur.close()
    conn.close()
