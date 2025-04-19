import os
import json
import http.client
import urllib.parse
from dotenv import load_dotenv
from dataclasses import dataclass

@dataclass
class PaymentSession:
    id: str
    status: str
    url: str

load_dotenv()

API_KEY = os.getenv('API_KEY')
DOMAIN = os.getenv('DOMAIN')



def create_checkout_session(amount_cents):
    conn = http.client.HTTPSConnection(DOMAIN)

    payload = {
        "success_url": "https://yourdomain.com/success",
        "cancel_url": "https://yourdomain.com/cancel",
        "mode": "payment",
        "line_items[0][price_data][currency]": "eur",
        "line_items[0][price_data][product_data][name]": "FreshMClean",
        "line_items[0][price_data][unit_amount]": amount_cents,
        "line_items[0][quantity]": 1
    }

    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    conn.request("POST", "/v1/checkout/sessions", body=urllib.parse.urlencode(payload), headers=headers)
    res = conn.getresponse()
    data = res.read()
    response_dict = json.loads(data.decode("utf-8"))
    session_id = response_dict.get('id')
    status = response_dict.get('status')
    redirect_url = response_dict.get('url')
    return PaymentSession(
        id=response_dict.get("id"),
        status=response_dict.get("status"),
        url=response_dict.get("url")
    )

