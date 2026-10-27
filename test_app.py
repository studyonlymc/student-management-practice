def add_student(name):
    return {"name": name}


def test_add_student():
    assert add_student("Amit")["name"] == "Amit"
