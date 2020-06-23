import discord
import json
import openpyxl
import requests
import asyncio
import os
from discord.ext import commands
from json import loads

token_path = os.path.dirname( os.path.abspath(__file__) )+"\Discord_Bot_Jamong_Token.txt"
t = open(token_path, "r", encoding="utf-8")
token = t.read().split()[0]
print('Token_Key: ', token)

game = discord.Game('!명령어')
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity=game, help_command=None)

twitch = 'https://www.twitch.tv/ja_o_mong'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('ver 2.0.0')
    print('본 프로그램을 종료할시 디스코드 봇을 이용하실 수 없습니다.')
    print('------')

@bot.event 
async def on_member_join(member):
    await member.send('자몽님과 트수들의 소통디코방에 오신걸 환영합니다!\n'
                      '처음오신분은 <#586920305016963083> 를 확인해주세요!')

@bot.command()
async def 방온(ctx):
    embed=discord.Embed(title="자몽님이 방송을 켜셨어요!", url="https://www.twitch.tv/ja_o_mong", description="이걸 보고도 안오시면 3대가 머머리가 될거에요!", color = 0xffd400)
    embed.set_author(name="권자몽님", url="https://asdfasdfasdfsadfsaf.com", icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/240687b0-6e37-407e-ae80-bfde51b8c0ed-profile_image-70x70.png")
    embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/240687b0-6e37-407e-ae80-bfde51b8c0ed-profile_image-70x70.png")
    await ctx.send('@everyone', embed=embed)

@bot.command()
async def 뱅온(ctx):
    embed=discord.Embed(title="자몽님이 방송을 켜셨어요!", url="https://www.twitch.tv/ja_o_mong", description="이걸 보고도 안오시면 3대가 머머리가 될거에요!", color = 0xffd400)
    embed.set_author(name="권자몽님", url="https://asdfasdfasdfsadfsaf.com", icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/240687b0-6e37-407e-ae80-bfde51b8c0ed-profile_image-70x70.png")
    embed.set_thumbnail(url="https://static-cdn.jtvnw.net/jtv_user_pictures/240687b0-6e37-407e-ae80-bfde51b8c0ed-profile_image-70x70.png")
    await ctx.send('@everyone', embed=embed)

@bot.command()
async def 명령어(ctx):
    await ctx.send('!를 붙인상태로 명령어를 입력해주세요.\n'
                   '구독, 블로그, 유튜브, 트게더, 커미션')

@bot.command()
async def 구독(ctx):
    await ctx.send('https://www.twitch.tv/products/ja_o_mong/ticket')

@bot.command()
async def 블로그(ctx):
    await ctx.send('http://blog.naver.com/ja_o_mong')

@bot.command()
async def 유튜브(ctx):
    await ctx.send('https://www.youtube.com/channel/UCAvCa_bYLpdCrTVVrPfor2w')

@bot.command()
async def 트게더(ctx):
    await ctx.send('https://tgd.kr/ja_o_mong')

@bot.command()
async def 커미션(ctx):
    await ctx.send('https://blog.naver.com/ja_o_mong/221215218612')

@bot.command()
async def 휴방(ctx):
    await ctx.send('@everyone 오늘은 휴방입니다.')

@bot.command()
async def 휴뱅(ctx):
    await ctx.send('@everyone 오늘은 휴방입니다.')

bot.run(token)
