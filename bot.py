import discord
import random, sys, os, math

client = discord.Client()
num = random.randint(0, 9)
keywords=["fds", "teste", "diagramas", "uia", "ahahah", "coisa", "sim", "não", "s", "n", "@MarcoFerreira", "ya", "missa", "louco", "gajo"]

listinsults=["Vai pró caralho pah", "És mesmo um zé do caralho", "E se te fosses foder? Não?", 
"Vai-te foder masé pah!", "Que é queres? Deves ter um atraso tu.... Palhaço do caralho",
"Olha-me este! FODASSE PAH"]

@client.event
async def on_message(message):
    for i in range(len(keywords)):
        if keywords[i] in message.content:
            for j in range(1):
                await message.channel.send("Vai pró caralho pah")

client.run('ODIyMTg4NTgyODMxMjU5NzM5.YFOoyQ.PwXA4PzabObsZbIdv5PEntM25lQ')


