# 🚀 AI Task Allocation System

This project is an AI-powered **task allocation system** that assigns tasks to users based on their skills and task priorities. The backend is built with **FastAPI**, the frontend with **React**, and AI-based task allocation uses **OpenAI/Gemini API**.

---

## 📌 Features

- ✅ Load tasks and users from CSV files  
- ✅ AI-powered task assignment using OpenAI/Gemini  
- ✅ FastAPI backend with REST API endpoints  
- ✅ React frontend with task display and allocation  
- ✅ Simple CSV-based database (Excel-compatible)

---

## 🦜 Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React, Chakra UI
- **AI Integration:** OpenAI API / Gemini API
- **Storage:** CSV (Excel-compatible)

---

## ⚡ Quick Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-task-allocation.git
cd ai-task-allocation
```

### 2️⃣ Set Up Backend (FastAPI)
```sh
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```
📍 The backend runs at [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3️⃣ Set Up Frontend (React)
```sh
cd frontend
npm install
npm start
```
📍 The frontend runs at [http://localhost:3000](http://localhost:3000)

---

## 📂 Project Structure
```bash
ai-task-allocation/
├── backend/              # FastAPI Backend
│   ├── main.py           # API Entry Point
│   ├── data_loader.py    # Loads Tasks & Users from CSV
│   ├── task_allocator.py # AI-based Task Assignment
│   ├── requirements.txt  # Dependencies
│   ├── .env              # API Keys (Ignored in Git)
├── frontend/             # React Frontend
│   ├── src/
│   │   ├── components/   # React UI Components
│   │   ├── pages/        # Main Pages
│   │   ├── App.js        # Main React File
│   ├── package.json      # Frontend Dependencies
├── sample_data/          # Sample CSV Files
│   ├── tasks.csv
│   ├── users.csv
├── README.md             # Project Documentation
```

---

## 💽 API Endpoints

### 🔹 Get All Tasks
**Endpoint:** `GET /tasks`

**Response Example:**
```json
[
    {"task_id": 1, "description": "Fix UI bug", "priority": "High"},
    {"task_id": 2, "description": "Optimize database", "priority": "Medium"}
]
```

### 🔹 Get All Users
**Endpoint:** `GET /users`

**Response Example:**
```json
[
    {"user_id": 101, "name": "John Doe", "skills": ["UI", "JavaScript"]},
    {"user_id": 102, "name": "Jane Doe", "skills": ["Python", "FastAPI"]}
]
```

### 🔹 Assign Tasks Using AI
**Endpoint:** `POST /assign`

**Request Example:**
```json
{
    "task_id": 1
}
```

**Response Example:**
```json
{
    "task_id": 1, "assigned_to": "John Doe"
}
```

---

## 🛠️ How to Use the API

### 1️⃣ Start the FastAPI Server
```sh
uvicorn main:app --reload
```

### 2️⃣ Available API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Check if API is running |
| `/tasks` | GET | Fetch all tasks from the CSV |
| `/users` | GET | Fetch all users from the CSV |
| `/assign` | POST | Assign a task to the best user using AI |

### 3️⃣ Testing API with Postman or Curl
```sh
# Get All Tasks
curl -X GET "http://127.0.0.1:8000/tasks"

# Get All Users
curl -X GET "http://127.0.0.1:8000/users"

# Assign Task Using AI
curl -X POST "http://127.0.0.1:8000/assign" \
     -H "Content-Type: application/json" \
     -d '{"task_description": "Fix UI bug"}'
```

---

# 🎤 AI Task Allocation - Demo Script

## 1️⃣ Introduction
**"Hello everyone, welcome to our demo of the AI Task Allocation system! This project automates task assignments using AI, optimizing efficiency."**

## 2️⃣ Features Overview
- **FastAPI Backend** for handling tasks and users.
- **AI-based Task Assignment** using OpenAI/Gemini.
- **React Frontend** to display tasks and users.

## 3️⃣ Live Demo

### 📌 Step 1: Start the Server
- Run: `uvicorn main:app --reload`
- Open `http://127.0.0.1:8000` to check if it's running.

### 📌 Step 2: Fetch Tasks & Users
- Call `/tasks` to list all tasks.
- Call `/users` to list available users.

### 📌 Step 3: Assign a Task using AI
- Send a **POST request** to `/assign`.
- The AI suggests the best user for the task.

### 📌 Step 4: Frontend Demo
- Show task assignment in the React UI.

## 4️⃣ Conclusion
**"This AI-powered system streamlines task management, making it more efficient. Thank you for watching!"**


