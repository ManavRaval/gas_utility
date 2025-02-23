Gas Utility Management System
Overview
This is a Django-based web application for managing customer service requests for a gas utility company. It allows users to sign up, log in, and submit service requests while providing customer support representatives with tools to manage and track requests.

Features
✅ User Authentication (Signup, Login, Logout)
✅ Customer Dashboard to view service requests
✅ Service Request Submission & Tracking
✅ Admin Panel for customer support representatives
✅ Django-based MVC structure for clean code organization

Installation
1. Clone the Repository

git clone https://github.com/your-github-username/gas-utility-management.git
cd gas-utility-management

2. Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate      # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Apply Migrations

python manage.py migrate

5. Create a Superuser (For Admin Panel)

python manage.py createsuperuser
Follow the prompts to set up an admin account.

6. Run the Development Server

python manage.py runserver
Now, visit http://127.0.0.1:8000/ in your browser to access the application.

Project Structure

gas_utility/
│── customers/          # Customer-related features
│   ├── templates/      # HTML templates (home, signup, login, etc.)
│   ├── views.py        # View functions for customer interactions
│   ├── urls.py         # URL routing for customers
│── support/            # Support representatives module
│── templates/          # Shared templates (base.html, etc.)
│── static/             # CSS, JS, and images
│── manage.py           # Django management script
│── requirements.txt    # Python dependencies
│── README.md           # Project documentation

Technologies Used
Python (Django Framework)
HTML, CSS, Bootstrap (Frontend UI)
SQLite (Default) / PostgreSQL (For production)

Future Enhancements
   Add Role-based Permissions (Admin, Customers, Support Reps)
   Email Notifications for service request updates
   Integrate AI chatbot for customer support

Contributing
Want to contribute? Fork the repo and submit a PR! 

License
This project is open-source under the MIT License.
