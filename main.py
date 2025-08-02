from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import requests

# Load .env file
load_dotenv()

# Load API Key from environment
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
print("🔐 Loaded OpenRouter API Key:", OPENROUTER_API_KEY)  # Debug print

app = FastAPI()

# OpenRouter API setup
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}
MODEL = "mistralai/mistral-7b-instruct:free"  # You can also try other free models

# Home route
@app.get("/")
async def root():
    return {"message": "🤖 Code Review Bot using OpenRouter is Live!"}

# Webhook listener
@app.post("/webhook")
async def webhook_listener(request: Request):
    try:
        payload = await request.json()
    except Exception as e:
        print("❌ Invalid or empty JSON received:", e)
        return {"message": "Invalid JSON payload"}

    # Handle GitHub's ping test
    if "zen" in payload:
        print("🌀 GitHub ping event received.")
        return {"message": "Ping received from GitHub"}

    # Try extracting PR data
    try:
        pr_title = payload["pull_request"]["title"]
        pr_body = payload["pull_request"]["body"]
        print(f"📦 Pull Request Title: {pr_title}")
    except Exception as e:
        print("❌ Could not extract PR info:", e)
        return {"message": "Invalid payload structure"}

    # Construct the AI prompt
    prompt = f"Please review this pull request:\n\nTitle: {pr_title}\n\n{pr_body}"

    try:
        data = {
            "model": MODEL,
            "messages": [
                {"role": "system", "content": "You are a code reviewer."},
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(API_URL, headers=HEADERS, json=data)
        result = response.json()

        print("📩 Raw OpenRouter API Response:", result)

        if "choices" in result and result["choices"]:
            ai_reply = result["choices"][0]["message"]["content"]
        else:
            ai_reply = "⚠️ No valid response from OpenRouter."

        print("\n✅ AI Review Response:\n", ai_reply)
    except Exception as e:
        print("❌ Error while calling OpenRouter API:", e)

    return {"message": "AI Review Complete ✅"}
