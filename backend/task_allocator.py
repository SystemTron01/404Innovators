import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")
def allocate_task(task_desc, user_skills):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Allocate task to best user based on skills and priority."},
            {"role": "user", "content": f"Task: {task_desc}, Skills: {user_skills}"}
        ]
    )
    return response['choices'][0]['message']['content']
