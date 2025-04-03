from flask import Flask, request, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Task
from matching import TaskMatcher


app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///tasks.db')
Session = sessionmaker(bind=engine)
session = Session()

matcher = TaskMatcher()

@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = session.query(Task).filter_by(status="open").all()
    return jsonify([task.to_dict() for task in tasks])

@app.route("/users", methods=["GET"])
def get_users():
    users = session.query(User).all()
    return jsonify([user.to_dict() for user in users])

@app.route("/assign_task/<int:task_id>", methods=["POST"])
def assign_task(task_id):
    try:
        task = session.query(Task).get(task_id)
        users = session.query(User).all()
        
        available_users = [
            u for u in users 
            if len(u.current_tasks) < u.capacity and task.status == "open"
        ]
        
        matches = [(u, matcher.calculate_similarity(task.required_skills, u.skills)) for u in available_users]
        matches.sort(key=lambda x: x[1], reverse=True)
        selected = matches[:task.required_people]
        
        if len(selected) >= task.required_people:
            task.assigned_to = [u[0].id for u in selected]
            task.status = "in-progress"
            for user in selected:
                user.current_tasks.append(task.id)
            session.commit()
            return jsonify({"success": True, "message": "Task assigned."})
        else:
            return jsonify({"success": False, "message": "Not enough qualified users."})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
