# 🏛️ E-Grievance Portal

<div align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />
  <img alt="Flask" src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white" />
  <img alt="MySQL" src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white" />
  <img alt="HTML5" src="https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white" />
  <img alt="CSS3" src="https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white" />
</div>

<br />

## 📖 Overview
The **E-Grievance Portal** is a comprehensive, open-source web application designed to digitize and streamline the process of submitting, tracking, and resolving complaints. Built with a robust Python/Flask backend and a clean HTML/CSS frontend, the platform provides a highly accessible system for users to voice their grievances and for administrators to manage them efficiently.

Perfectly suited for academic institutions, university projects, and organizational management to ensure transparent and accountable grievance redressal.

## ✨ Key Features
- **User Authentication**: Secure Login & Registration system with password protection.
- **Complaint Submission**: Intuitive forms for users to detail and submit a grievance quickly.
- **Real-Time Tracking**: Personalized user dashboard showing the live status of all submitted complaints (e.g., Pending, In Progress, Resolved).
- **Admin Management Panel**: Dedicated administrative interface to review all complaints, change their status, and provide resolutions.
- **Database Management**: Secure storage for users, admin details, and ticket history.

## 🛠️ Tech Stack
- **Backend**: Python 3, Flask, Jinja2
- **Database**: MySQL / SQLite
- **Frontend**: HTML5, CSS3, Vanilla JavaScript

---

## 🚀 Installation & Local Setup

Follow these commands to get the project running on your local machine:

**1. Clone the repository**
```bash
git clone https://github.com/jhaswati5757/E-Grievance-Portal.git
cd E-Grievance-Portal
```

**2. Install backend dependencies**
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

**3. Initialize Database**
Create the required database schema before running the app:
```bash
python init_db.py
```
*(Optional: Set up an administrator account by running `python create_admin.py`)*

**4. Run the Application**
```bash
python app.py
```
The application will be live at `http://127.0.0.1:5000`.

---

## 💡 Future Scope
- Implementation of email notifications for status updates.
- Ability to upload images/documents as evidence for complaints.
- Enhanced analytics dashboard for administrators to track resolution metrics.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome!

## 📝 License
This project is unrestricted and available for open use.