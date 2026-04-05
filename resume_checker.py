import pandas as pd
import numpy as np

def check_resume(resume_text):

    resume = resume_text.lower()

    skills = [
        "python",
        "machine learning",
        "numpy",
        "pandas",
        "data analysis",
        "sql",
        "deep learning",
        "gen ai",
        "ai agent"
    ]

    found_skills = []

    for skill in skills:
        if skill in resume:
            found_skills.append(skill)

    score = (len(found_skills) / len(skills)) * 100

    if score > 70:
        result = "Strong Resume"
    elif score > 40:
        result = "Average Resume"
    else:
        result = "Improve Resume"

    return found_skills, score, result