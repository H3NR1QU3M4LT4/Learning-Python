import discord
import random, sys, os, math

client = discord.Client()
num = random.randint(0, 9)
keywords=[""]

listinsults=[""]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.channel.send("MSG")

client.run('TOKEN')


