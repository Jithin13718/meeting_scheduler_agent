import requests
import json
from app.config import settings

SCALEDOWN_URL = "https://api.scaledown.xyz/compress/raw/"

def compress_prompt(context: str, prompt: str, model: str = "gpt-4o", rate: str = "auto") -> dict:
    """
    Compress a prompt using the ScaleDown API.
    """
    headers = {
        "x-api-key": settings.SCALEDOWN_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "context": context,
        "prompt": prompt,
        "model": model,
        "scaledown": {"rate": rate}
    }

    response = requests.post(SCALEDOWN_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"ScaleDown API error: {response.status_code} - {response.text}")