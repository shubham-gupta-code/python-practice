# Q53. Create a nested dictionary to represent student records.

students = {
    "student_01": {
        "name": "Alice Smith",
        "age": 18,
        "major": "Computer Science",
        "grades": {
            "math": 92,
            "physics": 88,
            "chemistry": 95
        }
    },
    "student_02": {
        "name": "Bob Johnson",
        "age": 19,
        "major": "Electrical Engineering",
        "grades": {
            "math": 85,
            "physics": 90,
            "electronics": 87
        }
    },
    "student_03": {
        "name": "Charlie Brown",
        "age": 17,
        "major": "Literature",
        "grades": {
            "english": 98,
            "history": 91,
            "art": 89
        }
    }
}

for stud_id, stud_info in students.items():
    print(f"{stud_id}:-")
    for key, info in stud_info.items():
        if key == "grades":
            print(f"{key}:- ")
            for subject, score in info.items():
                print(f"    {subject}: {score}")
        else:
            print(f"{key} --> {info}")
    print()

