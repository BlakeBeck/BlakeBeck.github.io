import requests 

def refresh_access_token():
    url = "https://accounts.zoho.com/oauth/v2/token?client_id=1000.VU3FOQGH4CZEZVW4JHJ9NEWLUNDAHH&client_secret=68259d272eb6bdfddfa1fd0144075148051b4f18d2&grant_type=refresh_token&refresh_token=1000.979f41e825cba3e17b9556a028342764.a64fd81c09842ada68df623072465e3c"
    response = requests.post(url)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception(f"Failed to refresh access token: {response.status_code} - {response.text}")

access_token = refresh_access_token()
email = "blake@salsburyandco.com"
url = "https://cliq.zoho.com/company/674987737/api/v2/bots/kioskbot/message"

headers = {
    "Authorization": f"Zoho-oauthtoken {access_token}",
    "Content-Type": "application/json"
}
user_name = "Blake"
user_id = "804012052"
data = {
    "text": "Hello! This is a test message sent from the Zoho Cliq API. {@" + user_id + "}"
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print("Success!")
else:
    print("Failed to send message.")
    print("Response:", response.json())

    
"""

    "access_token": "1000.66e0ab3847f795b0ffa038adb4ef78dc.b5836ed3fbd0d56443983b8efa022c70",
    "refresh_token": "1000.979f41e825cba3e17b9556a028342764.a64fd81c09842ada68df623072465e3c",
    "scope": "ZohoCliq.Webhooks.CREATE",
    "api_domain": "https://www.zohoapis.com",
    "token_type": "Bearer",
    "expires_in": 3600

"""