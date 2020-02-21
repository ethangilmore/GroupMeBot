import requests
import os

class GroupMeBot():
    def __init__(self, token, botId, groupId):
        self.baseUrl = "https://api.groupme.com/v3"

        self.token = token
        self.botId = botId
        self.groupId = groupId

    def postMsg(self, msg):
        if type(msg) is not str:
            raise TypeError('msg parameter is not of type str')

        postUrl = "{}/bots/post".format(self.baseUrl)
        data = {
            "bot_id"  : self.botId,
            "text"    : msg
        }
        requests.post(postUrl, data)

    def getLatestPosts(self, numPosts):
        getUrl = "{}/groups/{}/messages?limit={}&token={}".format(self.baseUrl, self.groupId, numPosts, self.token)
        r = requests.get(getUrl).json()
        posts = r['response']['messages']
        return posts

    def getLatestPost(self):
        return self.getLatestPosts(1)[0]

    def getLatestMsgs(self, numMessages):
        msgs = []
        for post in self.getLatestPosts(numMessages):
            if post['text']:
                msgs.append(post['text'])
            else:
                msgs.append("")
        return msgs

    def getMembers(self):
        getUrl = "{}/groups/{}?token={}".format(self.baseUrl, self.groupId, self.token)
        r = requests.get(getUrl).json()
        members = r['response']['members']
        return members


if __name__ == "__main__":
    TOKEN = os.getenv("TOKEN")
    BOT_ID = os.getenv("BOT_ID")
    GROUP_ID = os.getenv("GROUP_ID")

    bot = GroupMeBot(TOKEN, BOT_ID, GROUP_ID)
    # bot.postMsg(46)
    print(bot.getLatestMsgs(5))
