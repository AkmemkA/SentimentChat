import openai


class ChatBot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=user_input,
            max_tokens=3000,
            temperature=0.5
        ).choices[0].text
        return response


if __name__ == "__main__":
    chatbot = ChatBot()
    response = chatbot.get_response("Why do people lie?")
    print(response)