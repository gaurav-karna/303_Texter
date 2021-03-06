from secrets import account_sid_secret, auth_token_secret, twilio_phone, my_phone
from twilio.rest import Client
# latest commit HTML tag - needs spaces at front and new line at end since that is how wget file is parsed into toCompare
original = '      <a class="commit-tease-sha" href="/jin-guo/COMP303_Winter2019/commit/2739c87ba8b5e311ba19b850d90d0b05fd0d7ce7" data-pjax>' + '\n'

# breaks loop in interating through wget file - only pattern that matters for seeing difference in commit
breaker = '<a class="commit-tease-sha" href="/jin-guo/COMP303_Winter2019/'

toCompare = ""

account_sid = account_sid_secret
auth_token = auth_token_secret
client = Client(account_sid, auth_token)


# keeo iterating until that line is parsed in
file = open ("update.txt", "r")
for line in file:
	if breaker in line:
		toCompare = line
		break

# check if commit tags are the same
if (toCompare == original):
	print("It's all good")
else:
	print("Check website")
	message = client.messages \
                .create(
                     body="Changes have been made! Check https://github.com/jin-guo/COMP303_Winter2019 ",
                     from_=twilio_phone,
                     to=my_phone
                 )
	print(message.sid)
	
