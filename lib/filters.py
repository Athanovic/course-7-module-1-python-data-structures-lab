def filter_students_by_major(student_list, major):
    """
    Return a list of students filtered by major.
    """

    filtered = []

    for student in student_list:
        if student[2] == major:
            filtered.append(student)

    return filtered
