# Deployment Guide: E-Grievance Portal

## 1. Local Deployment (For College Viva & Presentation)

To present this project on your local machine effectively in front of the external or internal examiner, follow these exact steps:

### Prerequisites Checklist:
- [ ] Python (3.x) installed and added to PATH.
- [ ] XAMPP / WAMP installed for MySQL Database.
- [ ] Modern browser like Chrome or Edge.

### Steps to Run:
**Step A: Start Database**
1. Open **XAMPP Control Panel**.
2. Click **Start** next to MySQL (Ensure port 3306 is running smoothly).
3. Ensure your database `egrievance_db` exists and the tables are created.

**Step B: Start Server securely**
1. Open Terminal or Command Prompt inside your project folder.
2. Run the command to install packages (Only required first time): 
   `pip install -r requirements.txt`
3. Run the backend server using:
   `python app.py`

**Step C: Present App**
1. Open up your web browser.
2. Enter the local development URL: 

3. Present your beautiful portal! Have 2 user tabs open (1 for Student, 1 for Admin) to show Real-time status update functionality.

---

## 2. Cloud Deployment Strategy (AWS / Render)

**Important Examiner Question:** "How would you put this on the internet so all college students can actually access it?"

**BCA VIVA Answer:** "Sir, we have designed our entire codebase keeping Modern Cloud Deployment principles in mind. We used `python-dotenv` so that our DB passwords are not hardcoded, and we setup a `requirements.txt` for smooth cross-server dependency management."

### Expected Process for Cloud:
We can use a free Platform-as-a-Service like **Render**.
1. Create a free account on [Render.com](https://render.com/).
2. Push our code to a **GitHub repository** (Make sure to exclude `.env` using `.gitignore`).
3. Build the backend using: `pip install -r requirements.txt`.
4. Run the production server using WSGI server: `gunicorn app:app`.
5. For the database, instead of local XAMPP, we will spin up a free cloud MySQL DB on **Aiven** or **AWS RDS**, and place their Host credentials in the Render "Environment Variables" section.
6. Render will grant us a permanent cloud URL (e.g., `https://college-egrievance.onrender.com`).
