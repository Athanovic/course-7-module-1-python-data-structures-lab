def format_student_data(student):
    """
    Format student data for display.
    Returns a formatted string.
    """

    student_id, name, major = student

    return f"ID: {student_id} | Name: {name} | Major: {major}"


def display_students(student_list):
    """
    Display all student records.
    """

    for student in student_list:
        print(format_student_data(student))
