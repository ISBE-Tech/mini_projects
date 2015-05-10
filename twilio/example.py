import twilio
from twilio.rest import TwilioRestClient
import os

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.getenv('MY_ACCOUNT_SID')
auth_token  = os.getenv('MY_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi World",
    to="+17176026004",    # Replace with your phone number or text me if you really want to
    from_="") # Replace with your Twilio number
print message.sid