# ☁️ AWS Full Deployment Guide: E-Grievance Portal

Deploying a Flask + MySQL application on Amazon Web Services (AWS) is a great way to showcase production-level skills in your BCA project. We will use two main AWS services:
1. **AWS RDS (Relational Database Service):** To host the MySQL Database.
2. **AWS EC2 (Elastic Compute Cloud):** To host the Flask Python Backend.

---

## STEP 1: Setup MySQL Database on AWS RDS

Instead of local XAMPP, we will host our database on the cloud securely.

1. **Login to AWS Console** and search for **RDS**.
2. Click **Create database**.
3. **Choose a database creation method:** Select "Standard create".
4. **Engine options:** Select **MySQL**. Under templates, select **Free tier** to avoid billings.
5. **Settings:**
   - DB instance identifier: `egrievance-db`
   - Master username: `admin`
   - Master password: `your_strong_password123`
6. **Connectivity:**
   - Under *Public access*, choose **Yes** (So your EC2 and local MySQL Workbench can connect to it).
   - Create a new VPC security group. Let's call it `rds-sg`.
7. Click **Create database**. It will take 5-10 minutes to setup.
8. **Get the Endpoint:** Once the status is "Available", click on the database and copy the **Endpoint string** (e.g., `egrievance-xxxx.rds.amazonaws.com`). This is your new `DB_HOST`.

### Import your Local Data to RDS
1. Open **MySQL Workbench** or **HeidiSQL** on your computer.
2. Create a new connection using the **RDS Endpoint** as Hostname, `admin` as Username, and your password.
3. Once connected, open a new Query tab and copy-paste everything from your `database.sql` file.
4. Run the query. Your `egrievance_db` and all tables are now live on AWS!

---

## STEP 2: Launch an EC2 Server for Flask

Now we need a virtual computer (Server) to run your Python code 24/7.

1. Go to **EC2** in AWS Console and click **Launch Instances**.
2. **Name:** `EGrievance-Server`.
3. **OS Images (AMI):** Select **Ubuntu** (Free tier eligible).
4. **Instance type:** Select **t2.micro** (Free tier).
5. **Key pair:** Click "Create new key pair", name it `flask-key`, download the `.pem` file. You will need this to connect to the server.
6. **Network Settings (Security Group):**
   - Check **Allow SSH traffic**
   - Check **Allow HTTP traffic from the internet**
   - Click Edit -> Add Rule -> Custom TCP -> Port `5000` -> Source `Anywhere` (0.0.0.0/0). *This is important because Flask runs on port 5000!*
7. Click **Launch Instance**.

---

## STEP 3: Transfer Code & Setup the Server

1. **Connect to your EC2 instance:**
   - Go to EC2 instances, select your instance, and click **Connect**.
   - You can use the "EC2 Instance Connect" directly from the browser, or use SSH from your terminal:
     `ssh -i flask-key.pem ubuntu@<your-ec2-public-ip>`

2. **Update the server and install Python stuff:**
   Run these commands inside the EC2 terminal:
   ```bash
   sudo apt update
   sudo apt install python3-pip python3-venv git -y
   ```

3. **Clone your project:**
   Upload your project to GitHub first, then clone it on the server:
   ```bash
   git clone <your-github-repo-link>
   cd <your-repo-folder-name>
   ```

4. **Create the Environment File (`.env`):**
   ```bash
   nano .env
   ```
   Add your AWS RDS details:
   ```ini
   SECRET_KEY=my_super_secret_bca_project_key
   DB_HOST=egrievance-xxxx.rds.amazonaws.com
   DB_USER=admin
   DB_PASSWORD=your_strong_password123
   DB_NAME=egrievance_db
   ```
   Save (`Ctrl+O`, `Enter`) and exit (`Ctrl+X`).

5. **Setup Virtual Environment and Install Requirements:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

---

## STEP 4: Run the Application!

You could just run `python app.py`, but it will stop when you close your terminal. For production, we use **Gunicorn**.

1. **Install Gunicorn:**
   ```bash
   pip install gunicorn
   ```

2. **Run it continuously in the background:**
   ```bash
   nohup gunicorn -b 0.0.0.0:5000 app:app &
   ```
   *(Wait, if your main file is `app.py`, the command is `app:app`)*

### 🎉 FINAL RESULT:
Open your browser and visit your EC2 Public IPv4 address on port 5000:
`http://<your-ec2-public-ip>:5000`

Your E-Grievance Portal is now successfully deployed on AWS and accessible worldwide!

---

## Bonus: Nginx Reverse Proxy (Impress the Examiner)
Running on port 5000 looks okay, but standard websites run on Port 80 (without typing `:5000`). If you want to configure this:

1. `sudo apt install nginx -y`
2. `sudo nano /etc/nginx/sites-available/default`
3. Replace the `location /` block with:
   ```nginx
   location / {
       proxy_pass http://127.0.0.1:5000;
       proxy_set_header Host $host;
       proxy_set_header X-Real-IP $remote_addr;
   }
   ```
4. `sudo systemctl restart nginx`

Now your site will work directly on `http://<your-ec2-public-ip>`!
