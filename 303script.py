from twilio.rest import Client
# latest commit HTML tag - needs spaces at front and new line at end since that is how wget file is parsed into toCompare
original = '      <a class="commit-tease-sha" href="/jin-guo/COMP303_Winter2019/commit/8e505caea1aa071b7b5876bafcda2c4244697d9b" data-pjax>' + '\n'

# breaks loop in interating through wget file - only pattern that matters for seeing difference in commit
breaker = '<a class="commit-tease-sha" href="/jin-guo/COMP303_Winter2019/'

toCompare = ""

account_sid = 'ACa8bc6c3ea340029f822d1d95dfafb44f'
auth_token = 'f616832e098753abf4e16d339aa3f1c3'
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
                     from_='+17094000348',
                     to='[PHONE NUMBER]'
                 )
	print(message.sid)
	
