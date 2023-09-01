class AddressInfo:
    def __init__(self, address_line_1, address_line_2, country, state, city, zip_code):
        self.address_line_1 = address_line_1
        self.address_line_2 = address_line_2
        self.country = country
        self.state = state
        self.city = city
        self.zip_code = zip_code

    def __str__(self):
        return (f"Address Line 1: {self.address_line_1}, Address Line 2: {self.address_line_2}, "
                f"Country: {self.country}, State: {self.state}, City: {self.city}, Zip Code: {self.zip_code}")
