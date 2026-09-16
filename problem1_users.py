class Users:
    def __init__(self, name, surname, birth_year, email):
        self.name = name
        self.surname = surname
        self.birth_year = birth_year
        self.email = email

    def getAge(self):
        return 2023 - self.birth_year


user = Users("Ivan", "Petrov", 2000, "ivan@gmail.com")
print(user.getAge())
