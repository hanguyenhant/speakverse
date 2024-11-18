from flask import Flask, g
from routes.questions import questions_router  # Import blueprint cho Question Service
from utils.database import get_db # Import các hàm từ database.py

app = Flask(__name__)

# Đăng ký blueprint. url_prefix="/questions" có nghĩa là tất cả các route
# trong questions_router sẽ có prefix là /questions.
app.register_blueprint(questions_router, url_prefix="/questions")

# Khởi tạo database (chỉ cần chạy một lần)
# create_tables()

@app.teardown_appcontext
def close_db(error): # Đảm bảo session database được đóng sau mỗi request
  """Closes the database again at the end of the request."""
  if hasattr(g, 'db'): # g là một global context trong Flask
        g.db.close()



# Bạn có thể thêm các route khác tại đây nếu cần, ví dụ:
# @app.route("/")
# def hello():
#     return "Hello from Question Service!"



if __name__ == "__main__":
    app.run(debug=True)  # debug=True để bật chế độ debug