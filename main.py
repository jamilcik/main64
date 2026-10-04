class WorkPlace:
    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary

    def info(self):
        print("Ish joyi:", self.name)
        print("Kasbi:", self.job)
        print("Oyligi:", self.salary)
        print()


ish1 = WorkPlace("IT kompaniya", "Backend Developer", 8000000)
ish2 = WorkPlace("Bank", "Operator", 5000000)
ish3 = WorkPlace("Maktab", "O'qituvchi", 4000000)

ish1.info()
ish2.info()
ish3.info()
