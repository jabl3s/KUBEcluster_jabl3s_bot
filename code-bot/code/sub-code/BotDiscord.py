import discord

class BotDiscord(discord.Client):
    def __init__(self,jstore):
        self.__jstore=jstore
    async def on_ready(self):
        print('Logged on as', self.user)
    async def on_message(self, message):
        if message.author.name == "jabl3s":
            self.__jstore.__setDiscord(message.content)
        else:
            return

intents = discord.Intents.default()
intents.message_content = True
BotDiscord = BotDiscord(intents=intents)

#if message.content == 'ping':
#    await message.channel.send('pong')