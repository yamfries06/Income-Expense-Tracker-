# Trackify
Trackify is designed for users to manage, visualize, and improve their spending habits. It includes login, registration, and full CRUD functionality for expense tracking.

## Features
User Registration and Login: Users can sign up, log in, and manage their accounts.
Expense Management: Track expenses with categories, dates, and amounts. Update or delete them as needed.
Data Visualization: Provides insights into spending habits through visual tools.

## Deployment
Trackify is deployed on Render. You can check it out here: [Trackify on Render](https://trackify-ad7x.onrender.com).

## Current Status:
The application works flawlessly on my local machine, including all registration and expense management features. However, due to a migration issue on Render, the registration link is temporarily unavailable. This is a known issue, and I'm actively working on a fix.

## Locally:

All database migrations and functionalities, including user registration and CRUD operations, work as expected.

To run the app locally (where all features are functional):
'''bash
Clone the repository: git clone <repo-link>
Install dependencies: pip install -r requirements.txt
Apply migrations: python manage.py migrate
Run the server: python manage.py runserver
Technology Stack
Backend: Django
Database: PostgreSQL
Frontend: HTML, CSS, Bootstrap
Hosting: Render
