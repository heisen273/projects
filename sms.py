from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACdceaa0fd0031b2278ec5918587bc70a1"
auth_token  = "c361064e630ffe428fc8d7eb327bee8c"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="My name is OLOL?",
    to="+16148435837",    # Replace with your phone number
    from_="+16123516544") # Replace with your Twilio number
print message.sid
