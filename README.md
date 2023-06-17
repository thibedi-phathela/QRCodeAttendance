# Student attendance using QR Codes
An attendance system which uses QR codes to take attendance. This system can be used in institutions of learning, workplaces or conferences. 

This system is developed using Python3 and MySQL backend.

# Prerequisites
Make sure you have the following installed:

- Python3
- XAMPP with MySQL server

# Set-Up
 Before running the project, please ensure that all the required libraries and dependancies are installed: 

- pip install -r requirements.txt

# Files
- qr_code_generation.py: Generates QR codes for each student or attendee.
- scan.py: Scans QR codes, captures attendance, and records it in the database.

# Database Configuration
- Make sure you have XAMPP installed and the MySQL server is running.
- The database configuration can be found in the code file (scan.py).
- Modify the database connection details (host, username, password, and database name) in the code files accordingly.

# How to use
1. Start the MySQL server using XAMPP control panel.
2. Generate QR codes by running qr_code_generation.py.
3. Place the QR code in front of the camera to capture it and mark attendance using scan.py.
