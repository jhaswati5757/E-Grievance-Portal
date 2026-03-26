import mysql.connector
from werkzeug.security import generate_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

def create_default_admin():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "egrievance_db")
        )
        if conn:
            cursor = conn.cursor()
            hashed_password = generate_password_hash("admin123")
            try:
                # Check first
                cursor.execute("SELECT * FROM admins WHERE email = 'admin@college.edu'")
                if cursor.fetchone():
                    print("Admin user already exists!")
                else:
                    cursor.execute("INSERT INTO admins (name, email, password) VALUES (%s, %s, %s)", 
                                   ('Super Admin', 'admin@college.edu', hashed_password))
                    conn.commit()
                    print("SUCCESS: Default admin created!")
                    print("Email: admin@college.edu")
                    print("Password: admin123")
            except mysql.connector.Error as err:
                print(f"Error executing query: {err}")
            finally:
                cursor.close()
                conn.close()
    except Exception as e:
        print(f"Database Connection Error: {e}")
        print("Please make sure MySQL is running and the database 'egrievance_db' exists.")

if __name__ == "__main__":
    create_default_admin()
