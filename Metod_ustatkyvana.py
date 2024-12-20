class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self, current_year):
        return current_year - self.birth_year


class Driver(Person):
    def __init__(self, name, birth_year, license_number):
        super().__init__(name, birth_year)
        self.license_number = license_number

driver = Driver("Artem Shved", 2000, "SHI36678654")
print(f"Name: {driver.name}, Age: {driver.age(2024)}, License: {driver.license_number}")