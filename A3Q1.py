import psycopg

#Connect to the database
try:
    conn = psycopg.connect(
        dbname="University",
        user="postgres",
        password="nivetha",
        host="localhost",
        port="5432"
    )
except psycopg.OperationalError as e:
    print(f"Error: {e}")
    exit(1)

def get_all_students():
    """Function to get all the rows in the students table
    """
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM students") #select all the data from the table
        rows = cursor.fetchall() #method to retrieve the data
    #print the data
    for row in rows:
        print(row)
    
def add_student(first_name, last_name, email, enrollment_date):
    """Add a student to the database
    :param first_name: First name of the student
    :param last_name: Last name of the student
    :param email: Email of the student
    :param enrollment_date: The date of enrollment
    """
    with conn.cursor() as cursor:
        #insert the given data into the database but if the email exists then don't add it in
        cursor.execute(f"""
        INSERT INTO students (first_name, last_name, email, enrollment_date) 
        VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}')
        ON CONFLICT (email) DO NOTHING;""")
    conn.commit() #commit the data to the database

def update_student(student_id, new_email):
    """Update an existing record of a student
    :param student_id: ID of the student to update
    :param new_email: The new email of the student
    """
    with conn.cursor() as cursor:
        #update the row in the database
        cursor.execute(f"""UPDATE students
        SET email = '{new_email}'
        WHERE student_id={student_id}; 
        """)
    conn.commit()

def delete_student(student_id):
    """Delete a student from the database table
    :param student_id: The ID of the student to delete
    """
    with conn.cursor() as cursor:
        cursor.execute(f"""
        DELETE FROM students
        WHERE student_id={student_id};
        """)
    conn.commit()

def main():
    with conn.cursor() as cursor:
        #create table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
        student_id SERIAL PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        enrollment_date DATE
        );
        """)
        print("Table 'students' created successfully.")

        #Insert initial info
        add_student('John', 'Doe', 'john.doe@example.com', '2023-09-01')
        add_student('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01')
        add_student('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')
        
        print("Added info successfully")


    get_all_students()
    add_student("nivetha", "siva", "nivetha.siva5@example.com", "2023-04-02")
    update_student(2, "nivetha.siva6@example.com")
    delete_student(2)


if '__main__':
    main()


