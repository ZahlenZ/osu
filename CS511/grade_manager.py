
class Student:
    def __init__(self, id, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.assignments = []

    def get_full_name(self):
        full_name = self.first_name.title() + ' ' + self.last_name.title()
        return full_name

    def get_assignments(self):
        homework_list = self.assignments
        return homework_list

    def get_assignment(self, name):
        count = 0
        for j in range(len(self.assignments)):
            count += 1
            if self.assignments[j].name == name:
                most_recent = self.assignments[j]
                return most_recent
            elif count == len(self.assignments):
                return None

    def get_average(self):
        if len(self.assignments) > 0:
            add = 0
            count = 0
            for j in range(len(self.assignments)):
                if self.assignments[j].grade is None:
                    pass
                else:
                    add += self.assignments[j].grade / self.assignments[j].max_score
                    count += 1
            average = (add / count) * 100
            something = round(average, 1)
            return something
        else:
            pass

    def submit_assignment(self, assignment_list):
        try:
            for homework in assignment_list:
                self.assignments.insert(0, homework)
        except TypeError:
            self.assignments.insert(0, assignment_list)

    def remove_assignment(self, assignment):
        for j in range(len(self.assignments)):
            if self.assignments[j].name == assignment:
                remove = self.assignments.index(self.assignments[j])
                self.assignments.pop(remove)
                break


class Assignment:
    def __init__(self, name, max_score) -> None:
        self.name = name
        self.max_score = max_score
        self.grade = None

    def assign_grade(self, grade):
        if grade > self.max_score:
            pass
        else:
            self.grade = grade

