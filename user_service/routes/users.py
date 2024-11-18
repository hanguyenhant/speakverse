from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

from user_service.models.user import User
from user_service.services.user_logic import create_user, get_user_by_username
from utils.database import get_db


users_router = Blueprint("users", __name__)


@users_router.route("/register", methods=["POST"])
def register():
    with next(get_db()) as db:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        email = data.get("email")

        # Validate dữ liệu (kiểm tra username, password, email)

        if get_user_by_username(db, username):
            return jsonify({"message": "Username already exists"}), 400

        user = create_user(db, username, password, email)
        access_token = create_access_token(identity=user.id) # Tạo access token
        return jsonify({"access_token": access_token}), 201


@users_router.route("/login", methods=["POST"])
def login():
    with next(get_db()) as db:
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        user = get_user_by_username(db, username)

        if not user or not user.check_password(password): # Kiểm tra password
            return jsonify({"message": "Invalid username or password"}), 401

        access_token = create_access_token(identity=user.id)
        return jsonify({"access_token": access_token}), 200

@users_router.route("/me", methods=["GET"])  # protected route
@jwt_required()
def protected():
    with next(get_db()) as db:
        current_user_id = get_jwt_identity() # lấy id từ token
        user = db.query(User).filter(User.id == current_user_id).first()
        return jsonify(user.as_dict()), 200