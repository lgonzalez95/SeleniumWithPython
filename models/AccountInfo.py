class AccountInfo:

    def __init__(self, title, name, email, password, dob):
        self.title = title
        self.name = name
        self.email = email
        self.password = password
        self.dob = dob

    def __str__(self):
        return f"Title: {self.title}, Name: {self.name}, Email: {self.email}, Password: {self.password}, DOB: {self.dob}"
