   def add_student(name):
       if not name.strip():
           raise ValueError("Name cannot be empty")
       return {"name": name}


def test_add_student():
    assert add_student("Amit")["name"] == "Amit"
