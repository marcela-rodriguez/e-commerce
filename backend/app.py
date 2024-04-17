from user.domain.models.dto import LoginRequest, RequestCreateUser
from user.domain.user_cases import user as user_cases
from user.domain.models.exceptions import NotExist, UserExist
from user.repository.in_memory_repository import UserInMemoryRepository
from flask import Flask, Response, request
import json

app = Flask(__name__)

_REPOSITORY = UserInMemoryRepository()


@app.route("/user", methods=["POST"])
def create_user():
    body_request = request.get_json()
    user_information = RequestCreateUser(
        name=body_request["name"],
        email=body_request["email"],
        address=body_request["address"],
        phone=body_request["phone"],
        password=body_request["password"]
    )
    try:
        user_cases.create_user(user=user_information, repository=_REPOSITORY)
        return Response(
            response=json.dumps({"Mensaje": "usuario creado"}),
            status=201
        )
    except UserExist:
        return Response(
            response=json.dumps({"Error": "usuario ya existe"}),
            status=200
        )


@app.route("/user/login", methods=["POST"])
def login():
    body_request = request.get_json()
    user_info = LoginRequest(
        email=body_request["email"],
        password=body_request["password"]
    )
    try:
        response = user_cases.log_in(user_data=user_info, repository=_REPOSITORY)
        return Response(
            response=json.dumps({"refresh_token": response.refresh_token, "access_token": response.access_token}),
            status=200
        )
    except NotExist:
        return Response(
            response=json.dumps({"error": "usuario no encontrado"}),
            status=404
        )


@app.route("/products", methods=["POST"])
def create_product():
    body_request = request.get_json()

    return Response(
        response=json.dumps({}),
        status=200
    )
