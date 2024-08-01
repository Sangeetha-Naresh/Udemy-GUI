import pandas as pd

# Sample data
course_data = {
    "coursename": ["Python Basics", "Data Science", "Machine Learning", "Web Development"],
    "category": ["Programming", "Data Science", "AI", "Web Development"],
    "price": [29.99, 39.99, 49.99, 59.99]
}

# Create a DataFrame
df = pd.DataFrame(course_data)

# Save to Excel file
df.to_excel("courseinfo.xlsx", index=False)
