### DAY 2 CRUD OPERATIONS WITH THE HELP OF PYTHON AND psycopg2

# Import; package installed from pip
import psycopg2

# Made use of SQL Pooler (URI)
# postgresql://postgres.qstaywpgbmyxsuotdxvd:[YOUR-PASSWORD]@aws-0-ap-south-1.pooler.supabase.com:5432/postgres

### Database Credentials
DB_NAME = "postgres"
DB_USER = "postgres.qstaywpgbmyxsuotdxvd"
DB_PASSWORD = "SxRNLtNLDtFFlRqn"
DB_HOST = "aws-0-ap-south-1.pooler.supabase.com"
DB_PORT = "5432"

### connection made using try catch methods, 
def db_conn():
    try:
        conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        print("Database Connected Successfully")
        print(conn)
        return conn
    except Exception as e: # Take exceptions as e, which includes all the stuff that could make a credential fail
    # except: 
        # print("Error Connecting to Database")
        print(e) # Also possible to do this
        return None
    

### Make the Tables
def create_table_teachers():
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS teachers (
            teacher_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            age INT NOT NULL
        );
    """) # Use """ for multi line string
    conn.commit()
    cursor.close()
    conn.close()
    print("Table teachers Created Successfully")
    return None

def create_table_courses():
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            course_id SERIAL PRIMARY KEY,
            course_name VARCHAR(100) NOT NULL,
            department_id INT REFERENCES departments(department_id) ON DELETE CASCADE,
            credits INT NOT NULL,
            teacher_id INT REFERENCES teachers(teacher_id) ON DELETE CASCADE
        );
    """) # Use """ for multi line string
    conn.commit()
    cursor.close()
    conn.close()
    print("Table courses Created Successfully")
    return None

def create_table_students():
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE
        );
    """) # Use """ for multi line string
    conn.commit()
    cursor.close()
    conn.close()
    print("Table students Created Successfully")
    return None

def create_table_departments():
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            department_id SERIAL PRIMARY KEY,
            department_name VARCHAR(100) NOT NULL
        );
    """) # Use """ for multi line string
    conn.commit()
    cursor.close()
    conn.close()
    print("Table departments Created Successfully")
    return None

def create_table_enrollments():
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enrollments (
            enrollment_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES students(student_id) ON DELETE CASCADE,
            course_id INT REFERENCES courses(course_id) ON DELETE CASCADE,
            grade CHAR(2) NOT NULL
        );
    """) # Use """ for multi line string
    conn.commit()
    cursor.close()
    conn.close()
    print("Table enrollments Created Successfully")
    return None

### Insert the Data
def insert_data_teachers(f_name,l_name,age):
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("INSERT INTO teachers (first_name, last_name, age) VALUES (%s,%s,%s) ", (f_name, l_name, age))     # %s is called an interpolator
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted Successfully to teachers")
    return None

def insert_data_students(f_name,l_name,email):
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("INSERT INTO students (first_name, last_name, email) VALUES (%s,%s,%s) ", (f_name, l_name, email))     # %s is called an interpolator
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted Successfully to students")
    return None

def insert_data_departments(department_name):
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("INSERT INTO departments (department_name) VALUES (%s) ", (department_name,))     # %s is called an interpolator
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted Successfully to departments")
    return None

def insert_data_courses(course_name, department_id, credits, teacher_id):
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("INSERT INTO courses (course_name, department_id, credits, teacher_id) VALUES (%s,%s,%s,%s) ", (course_name, department_id, credits, teacher_id))     # %s is called an interpolator
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted Successfully to courses")
    return None

def insert_data_enrollments(student_id, course_id, grade):
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("INSERT INTO enrollments (student_id, course_id, grade) VALUES (%s,%s,%s) ", (student_id, course_id, grade))     # %s is called an interpolator
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Inserted Successfully to enrollments")
    return None

# Update the Data
def update_teachers_age(new_age):
    conn=db_conn()
    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
    cursor.execute("UPDATE teachers SET age = %s where id = 1", (new_age,)) # Convert it into a tuple with the help of a , to fix TypeError: 'int' object does not support indexing
    conn.commit()
    cursor.close()
    conn.close()
    print("Data Updated Successfully")
    return None

# Modify schema
# Original error in the table corrected, now already fixed in the original create table
# def update_teachers_id():
#    conn=db_conn()
#    cursor = conn.cursor() # Making a cursor that points in the database, needed for postgres for the navigation of data
#    cursor.execute("ALTER TABLE teachers RENAME id TO teacher_id") 
#    conn.commit()
#    cursor.close()
#    conn.close()
#    print("Column ID updated to t_id")
#    return None

# Initialisation of the Main Function
if __name__=="__main__":
    # db_conn()

    ### CREATE DATABASES
    create_table_teachers()
    create_table_departments()
    create_table_courses()
    create_table_students()
    create_table_enrollments()

    # update_teachers_age(22)
    # update_teachers_id()

    # insert_data_teachers("Ram", "Maharjan", 21)

    ### DATA FOR INSERTING INTO TABLES
    teachers = [
        {"first_name": "Alice", "last_name": "Brown", "age": 45},
        {"first_name": "Bob", "last_name": "Smith", "age": 50},
        {"first_name": "Charlie", "last_name": "Davis", "age": 38},
    ]

    students = [
        {"first_name": "John", "last_name": "Doe", "email": "john.doe@example.com"},
        {"first_name": "Jane", "last_name": "Smith", "email": "jane.smith@example.com"},
        {"first_name": "Alice", "last_name": "Johnson", "email": "alice.johnson@example.com"},
    ]

    departments = [
        {"department_name": "Computer Science"},
        {"department_name": "Mathematics"},
        {"department_name": "Physics"},
    ]

    courses = [
        {"course_name": "Intro to Programming", "department_id": 1, "credits": 3, "teacher_id": 1},
        {"course_name": "Calculus I", "department_id": 2, "credits": 4, "teacher_id": 2},
        {"course_name": "Physics 101", "department_id": 3, "credits": 4, "teacher_id": 3},
    ]

    enrollments = [
        {"student_id": 1, "course_id": 1, "grade": "FR"},
        {"student_id": 2, "course_id": 2, "grade": "SO"},
        {"student_id": 3, "course_id": 3, "grade": "JR"},
    ]

    ### INSERTING DATA INTO TABLES
    for teacher in teachers:
        insert_data_teachers(teacher["first_name"], teacher["last_name"], teacher["age"])

    for student in students:
        insert_data_students(student["first_name"], student["last_name"], student["email"])

    for department in departments:
        insert_data_departments(department["department_name"])

    for course in courses:
        insert_data_courses(course["course_name"], course["department_id"], course["credits"], course["teacher_id"])

    for enrollment in enrollments:
        insert_data_enrollments(enrollment["student_id"], enrollment["course_id"], enrollment["grade"])
