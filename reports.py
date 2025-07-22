import matplotlib.pyplot as plt
from io import BytesIO
from database import get_monthly_summary

def generate_monthly_expense_pie(user_id):
    data = get_monthly_summary(user_id)
    if not data:
        return None

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Monthly Expenses")
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return buf