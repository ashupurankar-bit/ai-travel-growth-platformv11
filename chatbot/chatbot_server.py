from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

client = OpenAI(api_key=api_key)

# Homepage (chat interface)
@app.route("/")
def home():
    return render_template("index.html")

# Chat API
@app.route("/chat", methods=["POST"])
def chat():

    try:

        message = request.json["message"]

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are an AI travel assistant helping with flights, hotels, itineraries and travel planning."},
                {"role": "user", "content": message}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)