# 🚀 AI Task Allocation System

This project is an AI-powered **task allocation system** that assigns tasks to users based on their skills and task priorities. The backend is built with **FastAPI**, the frontend with **React**, and AI-based task allocation uses **OpenAI/Gemini API**.  

---

## 📌 Features
✅ Load tasks and users from CSV files  
✅ AI-powered task assignment using OpenAI/Gemini  
✅ FastAPI backend with REST API endpoints  
✅ React frontend with task display and allocation  
✅ Simple CSV-based database (Excel-compatible)  

---

## 🛠️ Tech Stack
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
2️⃣ Set Up Backend (FastAPI)
sh
Copy
Edit
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
The backend runs at http://127.0.0.1:8000

3️⃣ Set Up Frontend (React)
sh
Copy
Edit
cd frontend
npm install
npm start
The frontend runs at http://localhost:3000

📂 Project Structure
bash
Copy
Edit
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
📡 API Endpoints (FastAPI)
🔹 GET /tasks
Response:

json
Copy
Edit
[
  {"task_id": 1, "description": "Fix UI bug", "priority": "High"},
  {"task_id": 2, "description": "Optimize database", "priority": "Medium"}
]
🔹 GET /users
Response:

json
Copy
Edit
[
  {"user_id": 101, "name": "John Doe", "skills": ["UI", "JavaScript"]},
  {"user_id": 102, "name": "Jane Doe", "skills": ["Python", "FastAPI"]}
]
🔹 POST /assign
Request:

json
Copy
Edit
{"task_id": 1}
Response:

json
Copy
Edit
{"task_id": 1, "assigned_to": "John Doe"}
📜 Sample CSV Data
📄 tasks.csv

scss
Copy
Edit
task_id,description,priority
1,Fix UI bug,High
2,Optimize database queries,Medium
📄 users.csv

pgsql
Copy
Edit
user_id,name,skills
101,John Doe,UI, JavaScript
102,Jane Doe,Python, FastAPI
🏗️ Contributors
👨‍💻 Ameer - Backend Development (FastAPI, CSV Handling)
🎨 Tharun - Frontend Development (React, Chakra UI)
🔗 Tushar - API Integration (AI Model, FastAPI)
📝 Sanjay - Documentation & Testing

📌 Next Steps
 Improve AI task matching logic

 Enhance UI with task filtering

 Deploy the project (Optional)
