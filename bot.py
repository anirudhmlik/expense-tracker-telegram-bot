import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from database import SessionLocal, engine
from models import Base, Budget, Expense, MessageHistory
from ai_engine import chat_with_llm
from sqlalchemy.orm.exc import NoResultFound

Base.metadata.create_all(bind=engine)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! I’m your Budget Assistant. Please tell me your monthly budget or log an expense.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user_id = str(update.message.from_user.id)
    db = SessionLocal()
    reply = ""

    if "budget" in text.lower():
        amount = extract_amount(text)
        if amount:
            budget = db.query(Budget).filter_by(user_id=user_id).first()
            if budget:
                budget.monthly_budget = amount
            else:
                db.add(Budget(user_id=user_id, monthly_budget=amount))
            db.commit()
            reply = f"💰 Budget set to ₹{amount}."
        else:
            reply = "Please specify the budget amount."

    elif any(word in text.lower() for word in ["spent", "paid", "bought"]):
        amount = extract_amount(text)
        if amount:
            db.add(Expense(user_id=user_id, amount=amount, category="general", description=text))
            db.commit()
            reply = f"📝 Logged ₹{amount} as expense."
        else:
            reply = "Please mention the expense amount."

    elif "total" in text.lower() or "balance" in text.lower():
        expenses = db.query(Expense).filter_by(user_id=user_id).all()
        total_spent = sum(e.amount for e in expenses)
        budget = db.query(Budget).filter_by(user_id=user_id).first()
        remaining = budget.monthly_budget - total_spent if budget else 0
        reply = f"📊 Total spent: ₹{total_spent}. Remaining budget: ₹{remaining}."

    else:
        reply = await chat_with_llm(text)

    db.add(MessageHistory(user_id=user_id, message=text, reply=reply))
    db.commit()
    db.close()

    await update.message.reply_text(reply)

def extract_amount(text):
    import re
    matches = re.findall(r'\d+(?:\.\d+)?', text)
    return float(matches[0]) if matches else None

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

if __name__ == '__main__':
    print("🚀 Bot Running")
    app.run_polling()