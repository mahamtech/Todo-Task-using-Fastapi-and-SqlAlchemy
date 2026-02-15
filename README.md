# ✅ FastAPI Todo App with JWT Authentication & Role-Based Access

## 📌 Project Overview

A secure Todo Management REST API built using FastAPI with JWT-based authentication and role-based authorization.  
The application supports user registration, login, and protected CRUD operations for todos, with admin-level access control.

It uses SQLAlchemy ORM for database interaction and follows a modular architecture with separate routers, schemas, and security layers.

---

## 🚀 Features

- 🔐 User Registration & Login with JWT Authentication
- 👤 Role-Based Access Control (Admin / User)
- 🔑 Secure Password Hashing (pwdlib)
- 📝 Full CRUD Operations for Todo Items
- 🗄️ Database Integration with SQLAlchemy ORM
- 📖 Interactive API Documentation via Swagger UI
- 🧩 Modular Project Structure (routers, models, schemas, security)
- ⚡ Dependency Injection using FastAPI Depends

---

## 🛠️ Tech Stack

- **Backend:** FastAPI
- **Database:** PostgreSQL (configurable)
- **ORM:** SQLAlchemy
- **Authentication:** JWT (python-jose)
- **Password Hashing:** Pwdlib 
- **Server:** Uvicorn

---

## 📂 Project Structure
todo_project/
│── main.py
│── database.py
│── model.py
│── schemas.py
│── security.py
│── auth.py
│── todo.py
│── requirements.txt
│── .env

### Clone Repository

```bash
git clone https://github.com/mahamtech/Todo-Task-using-Fastapi-and-SqlAlchemy.git
cd your-repo-name

##Create Virtual Environment
python -m venv venv
venv\Scripts\activate     # Windows
##Run Application
uvicorn main:app --reload
##Swagger Documentation:
http://127.0.0.1:8000/docs

