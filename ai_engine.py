import httpx
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

async def chat_with_llm(prompt):
    url = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
    payload = {"inputs": prompt}

    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(url, headers=HEADERS, json=payload)
        data = response.json()
        return data[0]['generated_text'] if isinstance(data, list) else "Sorry, no response."