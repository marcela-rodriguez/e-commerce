class RequestCreateUser:
    def __init__(self, name: str, email: str, address: str, phone: str, password: str) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone
        self.password = password


class LoginRequest:
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password


class LoginResponse:
    def __init__(self, refresh_token: str, access_token: str) -> None:
        self.refresh_token = refresh_token
        self.access_token = access_token
