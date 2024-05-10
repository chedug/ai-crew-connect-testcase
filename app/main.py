import os
from flask import Flask
from dotenv import load_dotenv
from app.api.endpoints import example, training, response

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

app.register_blueprint(example.bp)
app.register_blueprint(training.bp)
app.register_blueprint(response.bp)


@app.route('/')
def home():
    return "Welcome to the Ai Crew Connect microservice! Check documentation for more info."


if __name__ == "__main__":
    app.run(debug=True)
