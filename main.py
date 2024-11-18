from flask import Flask, g, jsonify
from flask_jwt_extended import JWTManager

from answer_service.routes.answers import answers_router
from question_service.routes.questions import questions_router
from topic_service.routes.topics import topics_router # Import blueprint cho Topic Service
from user_service.routes.users import users_router
from utils.database import get_db

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret" # Thay bằng key bí mật của bạn
jwt = JWTManager(app)

# Đăng ký blueprints
app.register_blueprint(questions_router, url_prefix="/questions")
app.register_blueprint(topics_router, url_prefix="/topics")
app.register_blueprint(answers_router, url_prefix="/answers")
app.register_blueprint(users_router, url_prefix="/users")

# Khởi tạo database (chỉ chạy một lần, sau đó comment lại)
# create_tables()

@app.teardown_appcontext
def close_db(error):
    """Đóng kết nối database sau mỗi request."""
    if hasattr(g, 'db'):
        g.db.close()


#  Optional: Health check route
@app.route("/health")
def health_check():
    return jsonify({"status": "OK"}), 200


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001) #  host='0.0.0.0' để listen trên tất cả các interfaces