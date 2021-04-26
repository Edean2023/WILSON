# Put your chatbot code when you made a text chatbot here
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# give the chatbot a name
chatbot = ChatBot('Mr.Chatbot')
# train the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer

# setup the trainers
trainer = ChatterBotCorpusTrainer(chatbot)
# train the standard personality
trainer.train('chatterbot.corpus.english')
# use for next assignment
# conv = open('chats.txt', 'r').readlines()

# chatbot.set_trainer(ListTrainer)

print("Welcome to the chat with Mr.Chatbot, ask it a question!")
is_exit = True
while not is_exit:
    request = input('You: ')
    response = chatbot.get_response(request)
    if request.lower().find("bye") != -1:
        is_exit = True
    else:
        print('Bot: ', response)

''' ******************* GUI Below Engine Above **************** '''
# Import for the GUI 
from chatbot_gui import ChatbotGUI

# create the chatbot app
app = ChatbotGUI("My Chat Bot (WINDOW NAME HERE)")
# time
import time


# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    # this is where you can add chat bot functionality!
    # text is the text the user has entered into the chat
    # you can use chat.send_ai_message("") to send a message as the AI
    # you can use chat.start_gif() and chat.stop_gif() to start and stop the gif
    # you can use chat.clear() to clear the user and AI chat boxes

    # print the text the user entered to console
    print("User Entered Message: " + text)
    # chat.start_gif()
    # send a response as the AI
    # chat.send_ai_message("Hello!")
    bot_response = chatbot.get_response(text)

    chat.send_ai_message(bot_response)

    # if the user send the "clear" message clear the chats
    if text == "clear":
        chat.clear()


# run the chat bot application
app.run()
