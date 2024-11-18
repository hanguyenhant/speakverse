from flask import Blueprint, request, jsonify
from answer_service.services.answer_logic import (
    create_answer, get_latest_answer, get_all_answers_by_question, hide_previous_answers
)
from utils.database import get_db


answers_router = Blueprint("answers", __name__)

@answers_router.route("/answers", methods=["POST"])
def create_new_answer():
    with next(get_db()) as db:
        data = request.get_json()
        question_id = data.get("question_id")
        user_id = data.get("user_id")
        audio_url = data.get("audio_url")
        text = data.get("text")

        # Validate dữ liệu

        new_answer = create_answer(db, question_id, user_id, audio_url, text)
        hide_previous_answers(db, question_id, new_answer.id) # ẩn các câu trả lời cũ


        return jsonify(new_answer.as_dict()), 201

@answers_router.route("/answers/<int:question_id>", methods=["GET"])
def get_answers(question_id):
    with next(get_db()) as db:
        answers = get_all_answers_by_question(db, question_id)
        return jsonify([answer.as_dict() for answer in answers])

@answers_router.route("/answers/latest/<int:question_id>", methods=["GET"])
def get_latest(question_id):
    with next(get_db()) as db:
        latest_answer = get_latest_answer(db, question_id)
        if latest_answer:
            return jsonify(latest_answer.as_dict())
        return jsonify({"message": "No answers found"}), 404