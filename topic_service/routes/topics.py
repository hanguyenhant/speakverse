from flask import Blueprint, jsonify, request
from topic_service.services.topic_logic import (
    get_all_topics, get_topic_by_id, create_topic, update_topic, delete_topic
)
from utils.database import get_db

topics_router = Blueprint("topics", __name__)


@topics_router.route("/topics", methods=["GET"])
def get_topics():
    with next(get_db()) as db:
        topics = get_all_topics(db)
        return jsonify([topic.as_dict() for topic in topics])  # Giả sử bạn có as_dict() trong model


@topics_router.route("/topics/<int:topic_id>", methods=["GET"])
def get_topic(topic_id):
    with next(get_db()) as db:
        topic = get_topic_by_id(db, topic_id)
        if topic:
            return jsonify(topic.as_dict())
        return jsonify({"message": "Topic not found"}), 404


@topics_router.route("/topics", methods=["POST"])
def create_new_topic():
    with next(get_db()) as db:
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")
        # Validate dữ liệu
        topic = create_topic(db, name, description)
        return jsonify(topic.as_dict()), 201


@topics_router.route("/topics/<int:topic_id>", methods=["PUT"])
def update_existing_topic(topic_id):
    with next(get_db()) as db:
        data = request.get_json()
        name = data.get("name")
        description = data.get("description")

        topic = update_topic(db, topic_id, name, description)

        if topic:
            return jsonify(topic.as_dict())

        return jsonify({"message": "Topic not found"}), 404


@topics_router.route("/topics/<int:topic_id>", methods=["DELETE"])
def delete_existing_topic(topic_id):
    with next(get_db()) as db:
        success = delete_topic(db, topic_id)

        if success:
            return jsonify({"message": "Topic deleted"})

        return jsonify({"message": "Topic not found"}), 404