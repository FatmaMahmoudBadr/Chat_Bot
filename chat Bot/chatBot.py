import re
import json
import random


def load_file(file):
    with open(file) as responses:
        return json.load(responses)

responses_data = load_file("bot.json")
def get_bot_response(user_message):
    user_message = re.split(r'\s+|[,;?!.-]\s*',user_message.lower())
    score_list=[]
    for response in responses_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        if required_words:
            for word in user_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):
            for word in user_message:
                if word in response["user_input"]:
                    response_score += 1

        score_list.append(response_score)

    max_score = max(score_list)
    response_index = score_list.index(max_score)

    if user_message == "":
        return "please write something."
    if max_score == 0:
        return random_response()
    else:
        return responses_data[response_index]["response"]

def random_response():
    responses_list =["I don't understand, ask another question.",
                     "please try something else.",
                     "I am sorry, i didn't catch that.",
                     "Please try to write something more clear."]
    return responses_list[random.randrange(len(responses_list))]


while True:
    user_message = input("you: ")
    print(f"Bot: {get_bot_response(user_message)}")