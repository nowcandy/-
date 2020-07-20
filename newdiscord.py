from random import randrange
from turtledemo.minimal_hanoi import play

import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print((client.user.id))
    print("ready")

@client.event
async def on_message(message):
    if message.content.startswith("씨발"):
        await message.channel.send("오우 싸발적이고")
    if message.content.startswith("병신"):
        await message.channel.send("오우 싸발적이고")
    if message.content.startswith("또라이"):
        await message.channel.send("오우 싸발적이고")
    if message.content.startswith("!"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))
        await message.channel.send("안녕하시고")
    if message.content.startswith("에바"):
        await message.channel.send("https://www.youtube.com/watch?v=cVsBeK_3yHA")
    if message.content.startswith("오마니"):
        await message.channel.send("https://www.youtube.com/watch?v=8p0G_pq0014")
    if message.content.startswith("개새끼"):
        await message.channel.send("오우 싸발적이고")
    if message.content.startswith("복권"):
        await message.channel.send("이번 당첨번호는") and await message.channel.send(randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send("입니다")
    if message.content.startswith("사계"):
        await message.channel.send("https://www.youtube.com/watch?v=G47OzeUqGU0")
    if message.content.startswith("미스포차"):
        await message.channel.send("https://www.youtube.com/watch?v=AGQCHmqrQoE")
    if message.content.startswith("리중딱"):
        await message.channel.send("https://www.youtube.com/watch?v=YvB8jIU1oaI")
    if message.content.startswith("정보"):
        await message.channel.send("생년월일:1990년월8일") and await message.channel.send("롤티어:브론즈") and await message.channel.send("좋아하는 축구팀:맨체스터유나이티드")
    if message.content.startswith("관제탑"):
        await message.channel.send("https://www.youtube.com/watch?v=QDo5VD5znYM")


access_token = os.environ
client.run("access_token")
