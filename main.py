import os
#db = sqlite3.connect('poke2auto.db')
#cur = db.cursor()
count = 0
f = open('pokes.txt', 'r')
file = f.read()
file = file.split('\n')
for i in file:
    if len(i) < 2:
        del file[file.index(i)]
mon_list = []
for i in file:
    if len(i) >= 3:
        mon_list.append(i)
from discord.ext import commands
from discord.ext import tasks
import asyncio
from keep_alive import keep_alive
import requests
cid = 946811847456206908
token = "OTQ2ODExMDk1NTg1Mjc1OTY0.YhkIvg.K3umRvgomfSQa2IS9Boo4SClSwo"
editing = {

}
req = requests.get("https://discord.com/api/path/to/the/endpoint")

print(req)
import time
#mon_url=input('url')
gg = open('caught.txt', 'a')
import random
#cid = 801907193754288249
client = commands.Bot(command_prefix='.')
client._skip_check = lambda x, y: False
@tasks.loop(seconds=0.2)
async def spammer():
  text_channel = client.get_channel(cid)
 # print(text_channel)
  if text_channel != None:
   # words = ["gaeming","om","ap","harry","nato"]
    #print(x)
    num = random.randint(1,10000000000000000000000000)
    await text_channel.send(num)
    intervals = [1, 1.7, 1.6, 1.5, 1.4, 1.3, 1.2, 1.8, 1.9]
    await asyncio.sleep(random.choice(intervals))

@tasks.loop(seconds=14400)
async def sleeper():
  time.sleep(seconds = 3600)
  spammer.start()
#pokes = ['pikachu','charixadd','swellow','pidove',input('option')]
spammer.start()


keep_alive()
client.run(token,bot=False)