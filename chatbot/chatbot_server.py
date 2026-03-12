from flask import Flask, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

client = OpenAI(api_key=api_key)

@app.route("/chat", methods=["POST"])
def chat():

    try:

        message = request.json["message"]

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": "You are a travel assistant."},
                {"role": "user", "content": message}
            ]
        )

        reply = response.choices[0].message.content

        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"error": str(e)})

app.run(host="0.0.0.0", port=5001)