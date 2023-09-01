class PersonalInfo:

    def __init__(self, first_name, last_name, company, mobile_number):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.mobile_number = mobile_number

    def __str__(self):
        return (f"First Name: {self.first_name}, Last Name: {self.last_name}, Company: {self.company}, "
                f"Mobile Number: {self.mobile_number}")
