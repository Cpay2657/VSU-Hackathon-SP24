from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)
config = {
    "max_output_tokens": 2048,
    "temperature": 0.9,
    "top_p": 1,
    "max_output_tokens": 200
}

# This unlocks the genai model
GOOGLE_API_KEY = "AIzaSyCvYlNHfis8KTM_PGZE2BKGuToNGAEJDIQ"
genai.configure(api_key=GOOGLE_API_KEY)
# Set up the model
generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 0,
        "max_output_tokens": 200,
        #"response_mime_type": "application/json",
    }

system_instruction = "You're Mable, a friendly mental health assistant that works to help people when they are in need. You are empathetic, compassionate, and soothing.\n"

# Initialize the Model
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                            generation_config=generation_config,
                            system_instruction=system_instruction)

# Initializing a chat with the model. The history of the chat is empty.
chat = model.start_chat(history=[])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    response = chat.send_message(userText, generation_config=config)
    print(response.text)
    return response.text

if __name__ == "__main__":
    app.run()