# In[]: Import Pacakges

from .student import Student
from .teacher import Teacher

# In[]:


class School:
    """
    A class to represent a school.
    Attributes:
        name (str): The name of the school.
        people (list): A list of people (students and teachers) in the school.
    Methods:
        add_person(person): Adds a person to the school.
        show_all_people(): Prints introductions of all people in the school.
        mark_attendance(name): Marks attendance for a specific person by name.
        generate_report(): Generates a report of all people in the school, including their name, age, role, and attendance.
    """

    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        """Add a person to the school."""
        if person not in self.people:
            self.people.append(person)
            print(f"{person.name} has been added.")
        else:
            print("This person already exists")

    def show_all_people(self):
        """Print introductions of all people in the school."""
        for i in self.people:
            print(f"Hello, my name is {i.name}")

    def mark_attendance(self, name):
        """Mark attendance for a specific person by name."""
        people = {i.name:i for i in self.people} # Dict containing persons names as keys (getting it using 'name' attribute) and objects as values
        if name in people:
            print(people[name].mark_attendance() , f"Total: {people[name].get_attendance()}")
        else:
            print("Person doesn't exist.")

    def generate_report(self):
        """Generate a report of all people in the school."""
        print("Name","Age","Role","Attendance", sep="\t\t\t")
        print("------------------------------------------------------------")
        for i in self.people:
            if "student" in i.introduce():
                print("{:16s}{:12s}{:16s}{:16s}".format(i.name,str(i.age),"Student",i.get_attendance()))
            else:
                print("{:16s}{:12s}{:16s}{:16s}".format(i.name,str(i.age),"Teacher",i.get_attendance()))

