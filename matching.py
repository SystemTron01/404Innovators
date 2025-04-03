import numpy as np
from sentence_transformers import SentenceTransformer

class TaskMatcher:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
    
    def calculate_similarity(self, task_requirements: str, user_skills: str) -> float:
        # Ensure input is a single string (not a list)
        if isinstance(task_requirements, list):
            task_requirements = " ".join(task_requirements)
        if isinstance(user_skills, list):
            user_skills = " ".join(user_skills)
        
        # Encode text inputs properly
        req_embedding = self.model.encode(task_requirements, convert_to_numpy=True)
        user_embedding = self.model.encode(user_skills, convert_to_numpy=True)
        
        # Compute cosine similarity
        similarity = np.dot(req_embedding, user_embedding) / (
            np.linalg.norm(req_embedding) * np.linalg.norm(user_embedding)
        )
        return float(similarity)


