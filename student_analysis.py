# ========================================================
# PROJECT: STUDENT PERFORMANCE & ATTENDANCE ANALYSIS SYSTEM
# ========================================================

print("=" * 55)
print("       STUDENT PERFORMANCE & ATTENDANCE REPORT         ")
print("=" * 55)

# Student Dataset (Name, Marks out of 100, Attendance %)
students = [
    {"name": "Aarav", "marks": 82, "attendance": 85},
    {"name": "Sneha", "marks": 45, "attendance": 70},
    {"name": "Rahul", "marks": 68, "attendance": 90},
    {"name": "Priya", "marks": 33, "attendance": 60},
    {"name": "Amit", "marks": 75, "attendance": 88}
]

print(f"{'Name':<10} | {'Marks':<6} | {'Attendance':<10} | {'Status'}")
print("-" * 55)

total_marks = 0

for s in students:
    total_marks += s["marks"]
    
    # Logic for Pass/Fail & Attendance Criteria
    if s["marks"] >= 40 and s["attendance"] >= 75:
        status = "Pass & Eligible"
    elif s["marks"] < 40 and s["attendance"] >= 75:
        status = "Failed (Low Marks)"
    else:
        status = "Detained (Low Attendance)"
        
    print(f"{s['name']:<10} | {s['marks']:<6} | {s['attendance']}%{'':<6} | {status}")

# Calculating Class Average
average_marks = total_marks / len(students)

print("-" * 55)
print(f"Total Students Evaluated : {len(students)}")
print(f"Class Average Marks      : {average_marks:.2f}")
print("=" * 55)
