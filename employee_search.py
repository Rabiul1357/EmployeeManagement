employees = [
    {"id": 1, "name": "Rahul"},
    {"id": 2, "name": "Ayan"},
    {"id": 3, "name": "Chitra"}
]

def search_employee(name):
    for employee in employees:
        if employee["name"].lower() == name.lower():
            return employee

    return "Employee not found"


print(search_employee("Rahul"))