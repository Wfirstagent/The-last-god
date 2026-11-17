import os
import urllib.request
import json

def ask_ai(prompt):
    api_key = os.environ.get("OPENROUTER_API_KEY", "")
    url = "http://localhost:8000/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "deepseek/deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 4000
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode('utf-8'), headers=headers, method='POST')
    try:
        with urllib.request.urlopen(req) as resp:
            res_data = json.loads(resp.read().decode('utf-8'))
            return res_data['choices'][0]['message']['content']
    except Exception as e:
        return f"Error: {e}"

