import os
import discord
from discord.ext import commands
from dotenv import load
from neuralintents import GenericAssistant

load()
TOK = os.getenv('TOKEN')
chatbot = GenericAssistant('intents.json', model_name="test_model")
chatbot.train_model()
chatbot.save_model()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


class MyClient(discord.Client):
    async def on_ready(self):
        print("Bot Initialized ( ͡° ͜ʖ ͡°)")

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$'):
            if message.content.startswith('$black'):
                await message.reply('Black Eat Ass')
            else:
                response = chatbot.request(message.content[1:])
                await message.reply(response)


# @client.event

client = MyClient(intents=intents)
client.run(TOK)
