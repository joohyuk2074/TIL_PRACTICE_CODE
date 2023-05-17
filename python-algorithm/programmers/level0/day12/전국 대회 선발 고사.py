from dataclasses import dataclass


@dataclass
class Student:
    index: int
    rank: int
    attendance: bool


def solution(rank, attendance):
    arr = []
    for i in range(0, len(rank)):
        if attendance[i]:
            student = Student(index=i, rank=rank[i], attendance=attendance[i])
            arr.append(student)

    sorted_students = sorted(arr, key=lambda student: student.rank)

    result = []
    count = 0
    for student in sorted_students:
        if count < 3:
            result.append(student.index)
            count += 1

    return 10000 * result[0] + 100 * result[1] + result[0]
