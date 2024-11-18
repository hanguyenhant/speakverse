from flask import Flask, g, jsonify
from question_service.routes.questions import questions_router
from topic_service.routes.topics import topics_router # Import blueprint cho Topic Service
from utils.database import get_db

app = Flask(__name__)

# Đăng ký blueprints
app.register_blueprint(questions_router, url_prefix="/questions")
app.register_blueprint(topics_router, url_prefix="/topics")

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