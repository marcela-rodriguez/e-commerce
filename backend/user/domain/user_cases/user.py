from user.domain.models.dto import LoginRequest, LoginResponse, RequestCreateUser
from user.domain.models.exceptions import NotExist, UserExist
from user.domain.models.models import User
from user.repository.in_memory_repository import UserInMemoryRepository
from commons.utils import create_id


def create_user(user: RequestCreateUser, repository: UserInMemoryRepository) -> None:
    repository.save(user=User(address=user.address,
                              name=user.name,
                              phone=user.phone,
                              password=user.password,
                              email=user.email,
                              user_id=create_id()
                              ))


def log_in(user_data: LoginRequest, repository: UserInMemoryRepository) -> LoginResponse:
    user = repository.find_by_email(email=user_data.email)
    if user:
        print("correo correcto")
        return LoginResponse("ndhksdhjmk", "154sss")
    raise NotExist("El usuario no existe")
