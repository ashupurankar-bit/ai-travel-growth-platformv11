from openai import OpenAI
import json
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def handler(request):

    body = json.loads(request.body)
    message = body["message"]

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role":"system","content":"You are an AI travel assistant."},
            {"role":"user","content":message}
        ]
    )

    reply = response.choices[0].message.content

    return {
        "statusCode":200,
        "body":json.dumps({"reply":reply})
    }