import pg8000

db_params = {
    'host': 'localhost',
    'port': 5432,
    'database': 'Students',
    'user': 'postgres',
    'password': 'Cfrb2003**'
}
def getAllStudents(cursor):
    cursor.execute('SELECT * from STUDENTS')
    results = cursor.fetchall()
    for x in results:
        print(x)
    

def addStudent(connection, cursor, first_name, last_name, email, enrollment_date):
    query = "INSERT INTO STUDENTS (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
    values = (first_name, last_name, email, enrollment_date)
    cursor.execute(query,values)
    connection.commit()

def updateStudentsEmail(connection, cursor, student_id, new_email):
    query = "UPDATE STUDENTS SET email = %s WHERE student_id = %s;"
    values = (new_email, student_id)
    cursor.execute(query, values)
    connection.commit()

def deleteStudent(connection, cursor, student_id):
    query = "DELETE FROM STUDENTS WHERE student_id = %s;"
    values = (student_id)
    cursor.execute(query, values)
    connection.commit()


try:
    connection = pg8000.connect(**db_params)
    cursor = connection.cursor()
    getAllStudents(cursor)


except Exception as error:
    print(error)


if connection:
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")