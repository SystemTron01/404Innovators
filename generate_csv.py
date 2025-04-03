import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Configuration
NUM_TASKS = 100  # Adjust as needed
OUTPUT_FILE = "supreme_task_allocations_v2.1.csv"

# Data Generation
def generate_ai_enhanced_tasks(num_tasks):
    tasks = []
    skills_pool = ["Python", "CAD", "Electrical", "UI/UX", "SQL", "AWS", 
                  "Data Analysis", "Embedded Systems", "React", "C++"]
    employees = ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank", "Grace", "Henry"]
    
    for i in range(num_tasks):
        # Core Fields
        task_id = f"TASK-{1000+i}"
        skills = list(np.random.choice(skills_pool, size=np.random.randint(1,4), replace=False))
        deadline = (datetime.now() + timedelta(days=np.random.randint(1,60))).strftime("%Y-%m-%d")
        priority = np.random.choice(["Low", "Medium", "High"], p=[0.15, 0.35, 0.5])
        hours = round(np.random.uniform(2, 40), 1)
        deps = np.random.choice(["None", f"TASK-{999+i}", f"TASK-{998+i}"], p=[0.7, 0.15, 0.15])
        
        # AI-Enhanced Fields
        urgency = round(0.5 + 0.5*np.random.beta(2,5), 2)  # Skewed toward high urgency
        confidence = f"{min(100, int(70 + 30*np.random.beta(2,2)))}%"
        best_emp = np.random.choice(employees)
        backup_emp = np.random.choice([e for e in employees if e != best_emp])
        gaps = np.random.choice(skills_pool) if np.random.random() > 0.3 else ""
        
        tasks.append({
            "Task_ID": task_id,
            "Description": f"Industrial task #{i}",
            "Required_Skills": "|".join(skills),  # Pipe-delimited for easy parsing
            "Deadline": deadline,
            "Priority": priority,
            "Estimated_Hours": hours,
            "Dependencies": deps,
            "Urgency_Score": urgency,
            "AI_Confidence": confidence,
            "Best_Employee": best_emp,
            "Backup_Employee": backup_emp,
            "Skill_Gaps": gaps
        })
    
    return pd.DataFrame(tasks)

# Generate and save
df = generate_ai_enhanced_tasks(NUM_TASKS)
df.to_csv(OUTPUT_FILE, index=False)
print(f"✅ File saved as {OUTPUT_FILE}")