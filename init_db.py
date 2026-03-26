import mysql.connector
import os

def init_db():
    try:
        # Connect without specifying database to create it
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        cursor = conn.cursor()
        
        # Read the database.sql file
        file_path = os.path.join(os.path.dirname(__file__), 'database.sql')
        with open(file_path, 'r') as f:
            sql_script = f.read()
            
        # Split script into commands by semicolon
        commands = sql_script.split(';')
        
        for command in commands:
            if command.strip():
                # Execute each command
                cursor.execute(command)
                
        conn.commit()
        print("Successfully created database and tables!")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Failed to setup database. Error: {e}")
        print("Is XAMPP/MySQL running?")

if __name__ == '__main__':
    init_db()
