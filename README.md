# 🚀 FastAPI Blog API

A backend Blog API built using **FastAPI**, following a modular project structure with routers, repositories, schemas, and database integration.

This project was created to learn backend development, REST APIs, authentication flow, and API structuring using FastAPI.

---

## ✨ Features

✅ Blog CRUD operations  
✅ User management  
✅ Modular FastAPI architecture  
✅ Database integration with SQLite  
✅ Password hashing  
✅ Organized routers & repositories structure  
✅ RESTful API endpoints

---

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **SQLite**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**

---

## 📂 Project Structure

```txt
FASTAPI/
│── blog/
│   ├── repository/
│   ├── routers/
│   ├── database.py
│   ├── hashing.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
│── requirements.txt
│── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
```

### 2. Move into the project folder

```bash
cd FASTAPI
```

### 3. Create virtual environment

```bash
python -m venv venv
```

### 4. Activate virtual environment

**Mac/Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the server

```bash
uvicorn blog.main:app --reload
```

---

## 📌 API Documentation

FastAPI automatically generates API docs.

### Swagger UI

```txt
http://127.0.0.1:8000/docs
```

### ReDoc

```txt
http://127.0.0.1:8000/redoc
```

---

## 🎯 Learning Goals

This project helped me learn:

- REST API development
- Backend architecture
- FastAPI fundamentals
- Database handling
- API routing
- Git & GitHub workflow

---

## 📈 Future Improvements

- [ ] JWT Authentication
- [ ] User Login System
- [ ] Better error handling
- [ ] PostgreSQL integration
- [ ] Deployment

---

## 👩‍💻 Author

**Poojitha**  
Learning backend development with FastAPI 🚀