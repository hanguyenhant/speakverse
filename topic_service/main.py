from routes.topics import topics_router

app = Flask(__name__)
app.register_blueprint(topics_router, url_prefix="/topics") # url_prefix="/topics"