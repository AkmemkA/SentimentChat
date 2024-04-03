from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow, \
    QTextEdit
import sys
from backend import ChatBot
import threading
from textblob import TextBlob


class ChatBotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.chatbot = ChatBot()

        self.setMinimumSize(700, 500)

        self.setWindowTitle("AI Chat")

        # Adds chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 680, 410)
        self.chat_area.setReadOnly(True)

        # Adds the input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 430, 580, 30)
        self.input_field.returnPressed.connect(self.send_message)

        # Adds the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(600, 430, 90, 30)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#34E831'>Me: {user_input}")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response,
                                  args=(user_input,))
        thread.start()

    def get_bot_response(self, user_input):
        blob = TextBlob(user_input)
        sentiment = blob.sentiment
        if sentiment.polarity > 0:
            user_input = f'Answer the following request as if you were Batman: {user_input}'
            response = self.chatbot.get_response(user_input)
            self.chat_area.append(f"<p style='color:#000000; "
                                  f"background-color:#FFFFFF'>ChatBot: {response}")
        else:
            user_input = f'Answer the following request as if you were Joker: {user_input}'
            response = self.chatbot.get_response(user_input)
            self.chat_area.append(f"<p style='color:#000000; "
                                  f"background-color:#FFFFFF'>ChatBot: {response}")


app = QApplication(sys.argv)
main_window = ChatBotWindow()
sys.exit(app.exec())
