# CS61A Discussion 05 Object Oriented Programming


# OOP
# Q1
class Instructor:
    degree = "PhD (Magic)" # this is a class attribute

    def __init__(self, name):
        self.name = name # this is an instance attribute

    def lecture(self, topic):
        print("Today we're learning about " + topic)

dumbledore = Instructor("Dumbledore")

class Student:
    instructor = dumbledore

    def __init__(self, name, ta):
        self.name = name
        self.understanding = 0
        ta.add_student(self)

    def attend_lecture(self, topic):
        Student.instructor.lecture(topic)
        if Student.instructor == dumbledore:
            print(Student.instructor.name + " is awesome!")
        else:
            print("I miss Dumbledore.")
        self.understanding += 1

    def visit_office_hours(self, staff):
        staff.assist(self)
        print("Thanks, " + staff.name)

class TeachingAssistant:
    def __init__(self, name):
        self.name = name
        self.students = {}

    def add_student(self, student):
        self.students[student.name] = student
    def assist(self, student):
        student.understanding += 1

if __name__ == '__main__':
    snape = TeachingAssistant("Snape")
    harry = Student("Harry", snape)
    harry.attend_lecture("potions")
    # >>>
    # Today we're learning about potions
    # Dumbledore is awesome!

    hermione = Student("Hermione", snape)
    hermione.attend_lecture("herbology")
    # >>>
    # Today we're learning about herbology
    # Dumbledore is awesome

    hermione.visit_office_hours(TeachingAssistant("Hagrid"))
    # >>>
    # Thanks, Hagrid

    print(harry.understanding)
    # >>> 1

    print(snape.students["Hermione"].understanding)
    # >>> 2  # even though not get this from snape (for visit office hour)

    Student.instructor = Instructor("Umbridge")
    Student.attend_lecture(harry, "transfiguration")
    # >>>
    # Today we're learning about transfiguration
    # I miss Dumbledore

    # Equivalent to harry.attend_lecture("transfiguration")


# Q2 Email
# We now want to write three different classes, Mailman, Client, and Email to simulate email.
# Fill in the definitions below to finish the implementation!

class Email:
    """Every email object has 3 instance attributes: the message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Mailman:
    """Each Mailman has an instance attribute clients, which is a dictionary that associates client names with client objects.
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client it is addressed to."""
        self.clients[email.recipient_name].receive(email)


    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it to the clients instance attribute."""
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is used for addressing emails to the client), mailman (which is used to send emails out to other clients), and inbox (a list of all emails the client has received).
    """

    def __init__(self, mailman, name):
        self.name = name
        self.mailman = mailman
        self.mailman.register_client(self, self.name)  # also register the Client in the mailman
        self.inbox = []

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        mail = Email(msg, self.name, recipient_name)
        self.mailman.send(mail)


    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        self.inbox.append(email)

