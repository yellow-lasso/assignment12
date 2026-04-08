# Congressional Trade Disclosure Analysis Tool (Web Application – Assignment 12)

## Overview

This project extends the Congressional Trade Disclosure Analysis Tool by implementing user authentication and multi-user support.

In this version, users can register for an account, log in, and manage their own trade records securely. Each user’s data is isolated, ensuring that users can only view and modify the records they have created. Passwords are securely stored using hashing, and access to application routes is protected using session-based authentication.

This assignment represents a significant advancement toward a production-level web application.

---

## Features

### 1. User Registration

- New users can create an account via the `/register` route.
- User credentials include:
  - Username (must be unique)
  - Password (securely hashed)
- Passwords are not stored in plain text.

---

### 2. User Login

- Existing users can log in via the `/login` route.
- Credentials are validated using password hashing.
- Upon successful login, a session is created:

```python
session["user_id"] = user.id