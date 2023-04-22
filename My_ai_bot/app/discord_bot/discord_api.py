from dotenv import load_dotenv
import discord
import os
from app.chatgpt_ai.openai import chatgpt_response

load_dotenv()

discord_token = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Successfully logged in as', self.user)

    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return

        if message.content.startswith(('/ai', '/bot', '/chatgpt')):
            command = message.content.split(' ')[0]
            user_message = message.content.replace(command, '').strip()
            if not user_message:
                return
            
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f"Answer: {bot_response}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

try:
    client.run(discord_token)
except Exception as e:
    print(f'Error: {str(e)}')