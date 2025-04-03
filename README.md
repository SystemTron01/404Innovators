# 🚀 AI Task Allocation System

This project is an AI-powered **task allocation system** that assigns tasks to users based on their skills and task priorities. The backend is built with **FastAPI**, the frontend with **React**, and AI-based task allocation uses **OpenAI/Gemini API**.

---

## 📌 Features

- ✅ **AI-Powered Task Assignment:** Utilizes OpenAI/Gemini to match tasks to the most suitable users based on skills and priorities.
- ✅ **FastAPI Backend:** Handles task and user data efficiently through REST API endpoints.
- ✅ **React Frontend:** Provides an intuitive interface to display tasks and user allocations.
- ✅ **CSV-Based Storage:** Uses simple CSV files to store task and user information, making it lightweight and Excel-compatible.
- ✅ **Scalability:** Designed to be easily extendable for databases and additional AI models.

---

## 🦜 Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** React, Chakra UI
- **AI Integration:** OpenAI API / Gemini API
- **Storage:** CSV (Excel-compatible)

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

# 🎤 AI Task Allocation - Explanation

## 1️⃣ Introduction
**"Our AI Task Allocation system automates task assignments by intelligently matching tasks with the most suitable users based on their skills and priorities."**

## 2️⃣ Key Features Explained
- **Task Management:** The system stores tasks in CSV format and categorizes them by priority.
- **User Management:** User details, including their skills, are also stored in CSV files.
- **AI-Powered Task Assignment:** The AI model processes task descriptions and assigns them to the most relevant user.
- **Scalability & Flexibility:** The system is designed to integrate with databases or advanced AI models if needed.

## 3️⃣ AI Task Assignment Process
- **Step 1:** The system reads available tasks and users from CSV files.
- **Step 2:** When a task needs assignment, the AI model evaluates the task description.
- **Step 3:** The AI suggests the best user for the task based on skill matching.
- **Step 4:** The task is assigned, and the result is stored/displayed.

## 4️⃣ Conclusion
**"This AI-powered system streamlines task management, ensuring efficient and optimized task allocation. It is lightweight, scalable, and can be adapted for more advanced use cases."**

