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

1. Clone the repository:
   ```bash
   git clone <repo-link>
2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

3. Apply migrations:
  ```bash
  python manage.py migrate
  ```
4. Run server:
```bash
  python manage.py runserver

