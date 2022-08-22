# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['ACa29017b22b90b29d632cf6c138f08d4e']
auth_token = os.environ['0709e3352970444866134ac09d18d2ec']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+13608182646',
                     to='+5565996059911'
                 )

print(message.sid)
