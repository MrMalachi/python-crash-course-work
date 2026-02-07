people = []

person_1 = {
    "first_name": "david",
    "last_name": "simmons",
    "age": 27,
    "eye_color": "brown",
    }
people.append(person_1)

person_2 = {
    "first_name": "david",
    "last_name": "korang",
    "age": 31,
    "eye_color": "brown",
    }
people.append(person_2)

person_3 = {
    "first_name": "sean",
    "last_name": "callahan",
    "age": 26,
    "eye_color": "blue"
    }
people.append(person_3)

for person in people:
    name = f"{person["first_name"].title()} {person["last_name"].title()}"
    age = person["age"]
    eye_color = person["eye_color"].title()

    print(f"\n{name}\n\tEye Color: {eye_color}\n\tAge: {age}")