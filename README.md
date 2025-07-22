# Expense Tracker Telegram Bot 🤖

A simple Telegram bot for tracking monthly budgets and daily expenses using Hugging Face APIs for lightweight NLP processing.

---

## 🚀 Features
- **Friendly chat interface**
- **Track monthly budget**
- **Log daily expenses (amount, category, description)**
- **Get real-time expense reports**
- **Persistent storage using SQLite**

---

## 🛠️ Technologies Used
- Python
- python-telegram-bot (v20.3)
- Hugging Face Inference API
- SQLAlchemy (SQLite)
- httpx (for API calls)
- dotenv (for secret management)

---

## ⚙️ Setup Instructions

1. **Clone repository:**

bash
git clone https://github.com/anirudhmlik/expense-tracker-telegram-bot.git
cd expense-tracker-telegram-bot


2.	**Setup virtual environment (optional but recommended):**

bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3.	**Install dependencies:**

bash
pip install -r requirements.txt

4.	**Setup environment variables:**
Create a .env file:
TELEGRAM_BOT_TOKEN=your_telegram_token_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here

5.	Run the bot:
bash
python bot.py

## 📊 Commands

	•	/start — Start interaction
	•	/setbudget <amount> — Set monthly budget
	•	/addexpense <amount> <category> [description] — Add expense
	•	/report — See spending summary


## 🛡️ Notes

	•	Hugging Face API used for intent parsing (can be swapped with local LLM if needed).
	•	SQLite stores expenses locally (expenses.db).



## 📤 Deployment
	•	Ideal for hosting on Railway, Render, or other Python-friendly platforms.

---

📄 License

MIT License.

---

## 📂 Suggested Repo Structure:

telegram_bot/
├── bot.py
├── ai_engine.py
├── database.py
├── models.py
├── requirements.txt
├── .env.example
├── README.md
├── expenses.db (auto-generated)
