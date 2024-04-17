import random
import string


def create_id(length: int = 10) -> str:
    id_created = ""
    for _ in range(length):
        id_created = id_created + random.choice(string.ascii_letters + string.digits)
    return id_created.upper()
