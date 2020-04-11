import requests

class chatbot:
    def __init__(self, msg, auth):
        self.msg = msg
        self.url = 'https://slack.com/api/chat.postMessage'
        self.headers = {'Authorization':'Bearer {}'.format(auth)}

    def postmsg(self):
        response = requests.post(self.url, headers=self.headers, json=self.msg)
        return(response.json())