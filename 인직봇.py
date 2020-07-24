from random import randrange
from turtledemo.minimal_hanoi import play
import asyncio
import os
from discord.ext import commands
import urllib
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote
import re # Regex for youtube link
import warnings
import requests
import time
import discord

client = discord.Client()

@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("도움말"))
    print("New log in as {0.user}".format(client))

@client.event
async def on_message(message, ):
    if message.content.startswith("모스키토"):
        await message.channel.send("https://www.youtube.com/watch?v=spHdWOYTZcE")
    if message.content.startswith("에바"):
        await message.channel.send("https://www.youtube.com/watch?v=cVsBeK_3yHA")
    if message.content.startswith("오마니"):
        await message.channel.send("https://www.youtube.com/watch?v=8p0G_pq0014")
    if message.content.startswith("복권"):
        await message.channel.send("이번 당첨번호는") and await message.channel.send(
            randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send(
            randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send(
            randrange(1, 46)) and await message.channel.send(randrange(1, 46)) and await message.channel.send("입니다")
    if message.content.startswith("사계"):
        await message.channel.send("https://www.youtube.com/watch?v=G47OzeUqGU0")
    if message.content.startswith("미스포차"):
        await message.channel.send("https://www.youtube.com/watch?v=AGQCHmqrQoE")
    if message.content.startswith("리중딱"):
        await message.channel.send("https://www.youtube.com/watch?v=YvB8jIU1oaI")
    if message.content.startswith("인직이정보"):
        await message.channel.send("생년월일:1990년월8일") and await message.channel.send(
            "롤티어:브론즈") and await message.channel.send("좋아하는 축구팀:맨체스터유나이티드")
        await message.channel.send("키:174cm 몸무게:79kg")
    if message.content.startswith("관제탑"):
        await message.channel.send("https://www.youtube.com/watch?v=QDo5VD5znYM")
    if message.content.startswith("/뮤트"):
        author = message.guild.get_member(int(message.content[4:22]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.add_roles(role)
    if message.content.startswith("/언뮤트"):
        author = message.guild.get_member(int(message.content[5:23]))
        role = discord.utils.get(message.guild.roles, name="뮤트")
        await author.remove_roles(role)
    if message.content.startswith("/채널메세지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await  client.get_channel(int(channel)).send(msg)
    if message.content.startswith("/DM"):
        author = message.guild.get_member(int(message.content[4:22]))
        msg = message.content[23:]
        await  author.send(msg)
    if message.content.startswith("도움말"):
        embed = discord.Embed(title='list')

        embed.add_field(name="복권", value="복권", inline=True)

        embed.add_field(name="모스키토", value="유튜브", inline=True)

        embed.add_field(name="에바", value="유튜브", inline=True)

        embed.add_field(name="미스포차", value="유튜브", inline=True)

        embed.add_field(name="사계", value="유튜브", inline=True)

        embed.add_field(name="관제탑", value="유튜브", inline=True)

        embed.add_field(name="리중딱", value="유튜브", inline=True)

        embed.add_field(name="인직아코로나", value="한국코로나현황", inline=True)

        embed.add_field(name="인직아먹어치워 (숫자)", value="메세지삭제(수량)", inline=True)

        embed.add_field(name="인직이정보", value="감스트 정보", inline=True)

        embed.add_field(name="/뮤트 ID(유저)", value="채팅 금지", inline=True)

        embed.add_field(name="/언뮤트 ID(유저)", value="채팅 금지풀기", inline=True)

        embed.add_field(name="/채널메세지 ID(채널) 할말", value="해당채널에 메세지전송", inline=True)

        embed.add_field(name="/DM ID(유저)", value="해당유저에게 메세지전송", inline=True)

        embed.add_field(name="편의기능(명령어X)", value="각종욕 필터링 채널입장시 인사", inline=True)

        embed.add_field(name="시간", value="시간", inline=True)

        await message.channel.send(embed=embed)

    if(message.content.split(" ")[0] == "!킥"):
       if(message.author.guild_permissions.kick_members):
           try:
               user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
               reason = message.content[25:]
               if(len(message.content.split(" ")) == 2):
                   reason = "None"
               await user.send(embed=discord.Embed(title="킥", description = f'당신은 {message.guild.name} 서버에서 킥당했습니다. 사유는 다음과 같습니다. ```{reason}```', color = 0xff0000))
               await user.kick(reason=reason)
               await message.channel.send(embed=discord.Embed(title="킥 성공", description = f"{message.author.mention} 님은 해당 서버에서 킥당하셨습니다. 사유:```{reason}```", color = 0x00ff00))
           except Exception as e:
               await message.channel.send(embed=discord.Embed(title="에러 발생", description = str(e), color = 0xff0000))
               return
       else:
           await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 유저를 킥할 수 있는 권한이 없습니다.", color = 0xff0000))
           return

async def on_member_join(member):
    channel = client.get_channel('736114981741002823')
    await member.send('도움말을 통해 다양한 서비스를 제공받을 수 있으니 해보라고 !')

client.run("NzMzOTI2MDQzNTcxODQ3MjI4.XxgtQA.8Mk-pyjUEetHDCX5i8QQzmPTbOg")