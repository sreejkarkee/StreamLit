import pandas as pd
import numpy as np

np.random.seed(42)
n = 150
subjects = ["Math", "Physics", "Programming", "Database", "Networks"]
df = pd.DataFrame({
    "student_id": range(1, n + 1),
    "semester": np.random.randint(1, 9, n),
    "subject": np.random.choice(subjects, n),
    "study_hours": np.round(np.random.uniform(0, 8, n), 1),
    "attendance": np.random.randint(50, 101, n).astype(float),
})
df["marks"] = (20 + df["study_hours"] * 5 + df["attendance"] * 0.3
               + np.random.normal(0, 8, n)).clip(0, 100).round(1)
df.loc[np.random.choice(n, 6, replace=False), "attendance"] = np.nan
df.to_csv("data/students.csv", index=False)
print("Created data/students.csv")
