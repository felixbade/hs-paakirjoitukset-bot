import requests
import json

# https://core.telegram.org/bots/api
# 'https://api.telegram.org/bot<token>/METHOD_NAME'

def get_me(token):
    resp = requests.get(f'https://api.telegram.org/bot{token}/getMe')
    return json.loads(resp.text)

def send_message(token, chat_id, text):
    resp = requests.post(f'https://api.telegram.org/bot{token}/sendMessage', data={'chat_id': chat_id, 'text': text})
    return json.loads(resp.text)