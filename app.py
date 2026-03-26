import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from mysql.connector import Error
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "super_secret_key")

# Database Connection Function
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "egrievance_db")
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# --- PUBLIC ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

# --- USER AUTHENTICATION ---
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Hash the password for safety
        hashed_password = generate_password_hash(password)
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            try:
                # Check if email exists
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                if cursor.fetchone():
                    flash("Email already registered! Please login.", "danger")
                    return redirect(url_for('register'))
                
                # Insert new user
                cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                               (name, email, hashed_password))
                conn.commit()
                flash("Registration Successful! You can now login.", "success")
                return redirect(url_for('login'))
            except Error as e:
                flash(f"An error occurred: {e}", "danger")
            finally:
                cursor.close()
                conn.close()
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True) # returns data in dictionary format
            cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()
            cursor.close()
            conn.close()
            
            # Check if user exists and password is correct!
            if user and check_password_hash(user['password'], password):
                session['user_id'] = user['user_id']
                session['user_name'] = user['name']
                flash("Login successful!", "success")
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid email or password", "danger")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear() # Clear session perfectly
    flash("You have been logged out.", "info")
    return redirect(url_for('home'))

# --- USER PORTAL ---
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash("Please login to access the dashboard", "warning")
        return redirect(url_for('login'))
        
    conn = get_db_connection()
    complaints = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM complaints WHERE user_id = %s ORDER BY created_at DESC", (session['user_id'],))
        complaints = cursor.fetchall()
        cursor.close()
        conn.close()
        
    return render_template('dashboard.html', complaints=complaints)

@app.route('/submit_complaint', methods=['GET', 'POST'])
def submit_complaint():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        category = request.form['category']
        description = request.form['description']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO complaints (user_id, category, description) VALUES (%s, %s, %s)",
                           (session['user_id'], category, description))
            conn.commit()
            cursor.close()
            conn.close()
            flash("Complaint submitted successfully!", "success")
            return redirect(url_for('dashboard'))
            
    return render_template('submit_complaint.html')

# --- ADMIN PORTAL ---
@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = get_db_connection()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM admins WHERE email = %s", (email,))
            admin = cursor.fetchone()
            cursor.close()
            conn.close()
            
            # Secure Admin Authentication
            if admin and check_password_hash(admin['password'], password):
                session['admin_id'] = admin['admin_id']
                session['admin_name'] = admin['name']
                flash("Admin Login successful!", "success")
                return redirect(url_for('admin_dashboard'))
            else:
                flash("Invalid admin credentials", "danger")
                
    return render_template('admin_login.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
        
    conn = get_db_connection()
    complaints = []
    if conn:
        cursor = conn.cursor(dictionary=True)
        # Advanced MySQL JOIN queries to get student details alongside complaints!
        query = """
        SELECT c.*, u.name as student_name, u.email as student_email 
        FROM complaints c 
        JOIN users u ON c.user_id = u.user_id 
        ORDER BY c.created_at DESC
        """
        cursor.execute(query)
        complaints = cursor.fetchall()
        cursor.close()
        conn.close()
        
    return render_template('admin_dashboard.html', complaints=complaints)

@app.route('/update_status/<int:complaint_id>', methods=['POST'])
def update_status(complaint_id):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
        
    new_status = request.form['status']
    remarks = request.form['remarks']
    
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE complaints SET status = %s, remarks = %s WHERE complaint_id = %s", 
                       (new_status, remarks, complaint_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Complaint status updated successfully!", "success")
        
    return redirect(url_for('admin_dashboard'))

@app.route('/admin_logout')
def admin_logout():
    session.pop('admin_id', None)
    session.pop('admin_name', None)
    flash("Admin logged out.", "info")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
