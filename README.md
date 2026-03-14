# Personal Finance Tracker (Django)

## Overview

Personal Finance Tracker is a web application developed using the Django framework that allows users to manage their personal finances. The system helps users record income and expenses, categorize financial transactions, and visualize spending patterns through charts.

The application provides an easy way to monitor financial activity and understand spending habits.

---

## Features

- User Registration and Authentication
- Secure Login and Logout
- Add Income Records
- Add Expense Records
- Categorize Transactions
- Dashboard with Financial Summary
- Data Visualization using Charts
- Responsive User Interface

---

## Technologies Used

- Python
- Django
- HTML
- Bootstrap
- Chart.js
- SQLite Database

---

## Project Structure

```
finance_tracker
│
├── finance_tracker
│   ├── settings.py
│   ├── urls.py
│
├── tracker
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── admin.py
│   ├── urls.py
│
├── templates
│   ├── base.html
│   ├── home.html
│   ├── signup.html
│   ├── login.html
│   ├── profile.html
│   ├── income.html
│   ├── expense.html
│   ├── charts.html
│
├── db.sqlite3
└── manage.py
```

---

## Installation

1. Clone the repository

```
git clone https://github.com/yourusername/personal-finance-tracker-django.git
```

2. Navigate to project folder

```
cd finance_tracker
```

3. Install dependencies

```
pip install django
```

4. Run migrations

```
python manage.py migrate
```

5. Start the server

```
python manage.py runserver
```

6. Open browser

```
http://127.0.0.1:8000
```

---

## Future Improvements

- Budget limit alerts
- Monthly financial reports
- Export reports to Excel or PDF
- Advanced analytics dashboard
- Mobile friendly UI

---

## Author

Developed as a Django learning project for personal finance management.
