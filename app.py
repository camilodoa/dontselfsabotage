from twilio.rest import Client
import requests
from datetime import datetime
import schedule
import time

# Meta info you need to fill out
sid = ""
auth_token = ""

me = ""
you = ""
body = "Kayla, don't self sabotage!!"

# Twilio Account SID and Auth Token
client = Client(sid, auth_token)

def job():
    client.messages.create(to=you, from_=me, body=body)
    print("Sent Kayla a support message at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

def main():
    schedule.every().day.at("06:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
