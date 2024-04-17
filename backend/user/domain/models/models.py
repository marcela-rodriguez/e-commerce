class User:

    def __init__(self, user_id: str, name: str, email: str, address: str, phone: str, password: str) -> None:
        self.user_id = user_id
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.password = password
