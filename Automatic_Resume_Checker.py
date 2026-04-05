import pandas as pd
import numpy as np
resume = open("resume.txt").read().lower()

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

print("Matched Skills:", found_skills)

score = (len(found_skills) / len(skills)) * 100

print("Resume Score:", score)
if score > 70:
    print("Strong Resume")
elif score > 40:
    print("Average Resume")
else:
    print("Improve Resume")
    data = pd.DataFrame({
    "Required Skills": skills
})
data = pd.DataFrame({
    "Required Skills": skills
})

data["Matched"] = data["Required Skills"].apply(lambda x: x in resume)

print(data)

