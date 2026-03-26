# Software Testing Report: E-Grievance Portal
## Prepared by: [Your Name] | Course: BCA

### 1. Automated Unit Testing
Unit testing focuses on verifying the individual components of the software. We have developed an automated script `test_app.py` using Python's `unittest` framework to check route accessibility and HTTP response codes.

You can run the tests using: `python test_app.py`

### 2. Manual Test Cases (for Viva and Report)

| Test Case ID | Module | Test Description | Input Data | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|---|
| **TC-01** | **Authentication** | Student Registration | Valid Name, Email, Password | "Registration Successful" flash message and DB entry created | As Expected | PASS |
| **TC-02** | **Authentication** | Duplicate Email Check | Already registered Email | "Email already registered!" message without DB crash | As Expected | PASS |
| **TC-03** | **Authentication** | Correct Login | Valid Email and Password | Redirect to Student Dashboard | As Expected | PASS |
| **TC-04** | **Authentication** | Incorrect Login | Invalid Email or Password | "Invalid email or password" flash message | As Expected | PASS |
| **TC-05** | **Complaints** | Submit Complaint | Category, Description text | Complaint stored in DB with 'Pending' status | As Expected | PASS |
| **TC-06** | **Security** | Dashboard Access without Login | Attempt to access `/dashboard` directly | Redirected back to `/login` | As Expected | PASS |
| **TC-07** | **Admin** | Admin Login | Valid admin credentials | Redirect to Admin Dashboard showing all complaints | As Expected | PASS |
| **TC-08** | **Admin** | Update Status | Change status from 'Pending' to 'Resolved' | Status updated in DB and visible to user | As Expected | PASS |

### 3. Integration Testing
Integration testing verifies that the Frontend correctly communicates with the Database via the Backend.
- **Frontend ↔ Backend:** Form submissions correctly pass to Flask endpoints (Tested via `request.form`).
- **Backend ↔ Database:** Data from Flask perfectly matches the MySQL Queries and updates dynamically (`mysql-connector-python`).
