import re
import fbchat
from fbchat import Client
from fbchat.models import *
import smtplib

EMAIL = ""# YOUR FB MESSENGER EMAIL HERE
PASS = ""# YOUR FB MESSENGER PASSWORD HERE
GROUP_ID = ""# THE THREAD ID OF THE GROUP HERE
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = ""# YOUR EMAIL HERE
MY_PASSWORD = ""# YOUR PASSWORD HERE

fbchat._util.USER_AGENTS = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')


class NotificationManager:

    def __init__(self):
        pass
    #     self.client = Client(EMAIL, PASS)
    #
    # def send_notification(self, msg):
    #     sent = self.client.send(Message(text=msg), thread_id=GROUP_ID, thread_type=ThreadType.USER)
    #     if sent:
    #         print("Message sent successfully")

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )