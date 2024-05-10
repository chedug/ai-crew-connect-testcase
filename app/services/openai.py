import openai


def query_openai(messages):
    """Query the OpenAI API with the provided prompt."""
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150
        )
        return response.choices[0].message.content
    except Exception as e:
        return str(e)
