class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class User(LoggingMixin):
    def __init__(self, name):
        self.name = name

    def login(self):
        print(f"{self.name} увійшов у систему")
        self.log(f"Користувач {self.name} увійшов у систему")

user = User("Олександр")
user.login()