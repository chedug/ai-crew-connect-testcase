import os
from flask import Flask
from dotenv import load_dotenv
from app.api.endpoints.example import example_blueprint

load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

app.register_blueprint(example_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
