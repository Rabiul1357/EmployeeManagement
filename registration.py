def register_employee(name, email):
    employee = {
        "name": name,
        "email": email
    }

    return employee


print(register_employee("Rahul", "rahul@gmail.com"))