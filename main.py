import discord
import json
import os

logfile=open("Serverlog.txt",'a')
if os.path.exists('commands.json'):
    with open('commands.json') as f:
        data=json.load(f)
        client = discord.Client()


    @client.event
    async def on_message(message):
        if message.content in data["commands"].keys():
            await message.channel.send(data["commands"][message.content])

            print(f"message {message.content} written by",message.author,f"at time {message.created_at}")
            logfile.write(f"message {message.content} written by {message.author} at time {message.created_at} \n")

            print("sent message ",data["commands"][message.content]," to ",message.author)
            logfile.write("lioncatbot sent message "+data["commands"][message.content]+"\n")
            logfile.flush()
    client.run(data["token"])


else:
    print("Error File not found. press Enter to exit")
    e=input()
logfile.close()