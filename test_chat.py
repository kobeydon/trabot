import slackapi

data = {'channel':'C010QDX9L69', 'text':'こんにちは！私はボットだよ'}
with open('./auth.txt') as f:
    key = f.read().strip()

instance = slackapi.chatbot(data, key)

response = instance.postmsg()
print(response)