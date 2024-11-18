from flask import Blueprint, request, jsonify
from question_service.services.question_logic import get_questions, get_random_question, create_question
from utils.database import get_db # Hàm get_db từ file database.py của bạn.
from sqlalchemy.orm import Session

questions_router = Blueprint("questions", __name__)


@questions_router.route("/questions", methods=["GET"])
def get_all_questions():
    # db: Session = get_db()
    with next(get_db()) as db:
        part = request.args.get("part", type=int)
        topic_id = request.args.get("topic_id", type=int)
        skip = request.args.get("skip", 0, type=int)
        limit = request.args.get("limit", 100, type=int)
        questions = get_questions(db, part, topic_id, skip, limit)
        return jsonify([question.as_dict() for question in questions]) # Chuyển đổi object thành dict


@questions_router.route("/questions/random", methods=["GET"])
def get_random():
    # db: Session = get_db()
    with next(get_db()) as db:
        part = request.args.get("part", type=int)
        topic_id = request.args.get("topic_id", type=int)
        question = get_random_question(db, part, topic_id)

        if question:
            return jsonify(question.as_dict())
        else:
            return jsonify({"message": "Không tìm thấy câu hỏi"}), 404


@questions_router.route("/questions", methods=["POST"])
def create_new_question():
    # db: Session = get_db()
    with next(get_db()) as db:
        data = request.get_json()
        text = data.get("text")
        part = data.get("part")
        topic_id = data.get("topic_id")
        youtube_video_id = data.get("youtube_video_id")

        # Validate dữ liệu ở đây

        question = create_question(db, text, part, topic_id, youtube_video_id)
        return jsonify(question.as_dict()), 201

