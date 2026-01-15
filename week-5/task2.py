import json

with open("students.json", "r", encoding="utf-8") as fail:
    students = json.load(fail)

for okushy in students:
    bagasy = okushy["grades"]
    okushy["average_grade"] = sum(bagasy) / len(bagasy)

with open("students_updated.json", "w", encoding="utf-8") as rezultat:
    json.dump(students, rezultat, indent=2)
