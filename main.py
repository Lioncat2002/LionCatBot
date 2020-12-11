import discord
import json
import os
if os.path.exists('commands.json'):
    with open('commands.json') as f:
        data=json.load(f)
        client = discord.Client()


        @client.event
        async def on_message(message):
            if message.content in data.keys():
                await message.channel.send(data[message.content])  # If the user says !hello we will send back hi


        client.run("Bot token")
else:
    print("Error File not found. press any key to exit")
    e=input()

