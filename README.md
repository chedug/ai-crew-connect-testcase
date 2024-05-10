# Flask Firebase AI Microservice

This project is a Flask microservice that integrates with Firebase Firestore for data storage and OpenAI GPT for AI agent responses. The microservice includes functionality for training agents, generating responses, and storing them in Firestore.

## Features

- **Train AI Agents**: Train AI agents with specific role-based conversation examples via `/train` endpoint.
- **Generate Responses**: Simulate AI agent responses based on conversation datasets via `/respond` endpoint.
- **Store Responses**: Save generated responses to Firestore and retrieve them by role via `/responses` endpoint.
- **Unit Testing**: Includes unit tests for training, response generation, and OpenAI integration.


## Getting started

### Prerequisites
- Python 3.11+
- Firebase Project with Firestore enabled
- OpenAI API Key
- Poetry (Recommended)

## Set up

To set up a project it is recommended to install dependencies in a virtual environment

### Clone the Repository:
```bash
git clone <repo-url>
cd <repo-directory>
```

### Configure Firebase Credentials:
Download a service account key file (`serviceAccountKey.json`) from your Firebase Project.


Place the file in the root app directory.


Make sure the .env file contains the following:

```commandline
FIREBASE_SERVICE_ACCOUNT_KEY="path/to/serviceAccountKey.json"
OPENAI_API_KEY="your_openai_api_key"
```
### Install Dependencies: 
**Using Poetry:**

```bash
poetry install
```


### Running the Application
Start the Flask App:
```bash
flask --app main run
```

