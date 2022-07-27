from __future__ import unicode_literals
import pymongo

import discord
from discord.utils import get
from discord.ext import commands

client = pymongo.MongoClient("mongodb+srv://bot:violeta17@botdb.qeffd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = ""
col = ""

intents = discord.Intents.default()
intents.members = True  
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print("test")
    await bot.change_presence(activity=discord.Game(name="Comprar una xbox"))

@bot.event 
async def on_message(message):
    global db
    global col
    db = client[str(message.guild.id)]
    col = db[str(message.author.id)]
    
    if message.content.startswith('!gamertag'):
        a = message.content[len("!gamertag") + 1: ]
        if a != "" and "<@" not in a:
            print(a)
            a = a.split(":")
            
            x = col.insert_one({a[0]: a[1].replace(" ", "")})
            await message.channel.send("Añadadido UwU")
        if "<@" in a:
            try:
                a = a[2: -1]
                col = db[str(a)]
                print(a)
                m = col.find()
                
                for z in m:
                    w = []
                    del z["_id"]
                    w.append(z)
                    w = w[0]
                    for f in w.values():
                        wv = f
                    
                    for i in w.keys():
                        wk = i
                    await message.channel.send(f"{wk}: {wv}")
                    del w
                


            
            except Exception:
                await message.channel.send("Esta persona no ha puesto sus gamertags :(")
                



bot.run("TOKEN")

        
    