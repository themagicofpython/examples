student_tuples = [
('John', 21),
('Jane', 22),
('Dave', 25),
]
print(sorted(student_tuples, key=lambda student: student[1]))
