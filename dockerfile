# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose no ports (Telegram bot is pull-based)
CMD ["python", "bot.py"]