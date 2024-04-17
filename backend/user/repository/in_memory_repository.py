from user.domain.models.models import User
from user.domain.models.exceptions import UserExist
from typing import List, Optional


class UserInMemoryRepository:

    def __init__(self) -> None:
        self.db: List[User] = [
            User(email="marcer735@gmail.com", user_id="AAA111", name="Marce", phone="31327638127",
                 address="alle falasd", password="1234"),
            User(email="sanchezbuitrago@gmail.com", user_id="AAA222", name="Edgar", phone="31327638127",
                 address="alle falasd", password="1234")
        ]

    def save(self, user: User) -> None:
        user = self.find_by_email(email=user.email)
        if user == None:
            self.db.append(user)
        elif user != None:
            raise UserExist("El usuario ya existe")

    def find_by_email(self, email: str) -> Optional[User]:
        for user in self.db:
            if user.email == email:
                return user
