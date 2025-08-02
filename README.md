# 🤖 AI Code Review Bot (FastAPI + OpenRouter)

The **AI Code Review Bot** is a smart assistant that automatically reviews pull requests on your GitHub repositories.
It uses large language models (LLMs) via OpenRouter's API to analyze PR titles and descriptions, providing helpful feedback instantly — like a virtual code reviewer on your team!

---

## 📦 Features

- 🚀 Automatically listens to GitHub webhook events for new PRs
- 🧠 Uses OpenRouter LLMs (e.g., Mistral, Hermes) to analyze PR content
- 📝 Returns natural language suggestions or summaries for code reviews
- 🔗 Can be deployed with `ngrok` for quick webhook access

---

## 🛠 Requirements

Make sure you have the following installed:

- Python 3.10+
- FastAPI
- Uvicorn
- requests
- python-dotenv
- [OpenRouter API key](https://openrouter.ai/)
- [ngrok](https://ngrok.com/) (for local testing with GitHub webhooks)

Install dependencies:

```bash
pip install fastapi uvicorn requests python-dotenv

```
## ⚙️ How It Works
1.Clone this repo and activate your virtual environment:
git clone https://github.com/Prathunotfound/Code-Review-Bot.git
cd Code-Review-Bot
python -m venv venv
venv/Scripts/activate

2. Set up your .env file with your OpenRouter API key:
   OPENROUTER_API_KEY=your_api_key_here

3.Start the FastAPI server:
uvicorn main:app --reload

4.Expose your local server using ngrok:
ngrok http 8000

````
````
## Create a GitHub webhook on your forked repo:

Payload URL: https://your-ngrok-url/webhook

Content type: application/json

Event type: Pull request

```
```
### When you create or update a PR, the bot will receive the webhook and respond with an AI-generated review in the terminal!

```
```
 Hey! I’m Prathamesh Jadhav  — a developer from Akola, India 🇮🇳 who loves blending AI with real-world tools. I build smart, useful, and sometimes fun automation projects that solve everyday problems.
 🧠Find me on GitHub: @prxthu04
 📬 Let’s connect: Prathunotfound@gmail.com










