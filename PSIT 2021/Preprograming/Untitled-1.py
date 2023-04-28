

# import discord
# from discord.ext import commands
# import youtube_dl
# import os
# import random

# # musiclist = ['!p https://youtu.be/ICtULYYjrrU','!p https://www.youtube.com/watch?v=DXHgBUMnlvY']
# # alphaeng = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# client = discord.Client()
# client2 = commands.Bot(command_prefix="+")

# # sad_words =['ahh', 'val?', 'what', 'so?']
# # request_word = ['@Plasterbate', 'Guy', 'Plaster', 'Plasterbate', 'plaster', 'ปลาสเตอร์', 'ปลาสลิด', 'ปลาสเตอร์เจี้ยน']
# # start_to_do = ['you can play with me', 'come'
# # ]

# @client.event
# async def on_ready():
#   print('We have logged in as {0.user}'.format(client))


# @client.event
# async def on_message(message):
  
#   if message.author == client.user:
#     return
#   msg = message.content
#   if message.content.startswith('+hello'):
#     await message.channel.send("Hello There!")
#   if message.content.startswith('+your boss'):
#     await message.channel.send("Hi Mr.Owen")
#   if message.content.startswith('+how are you?'):
#     await message.channel.send("Fine , Thanks")
#   if message.content.startswith('+what is your name'):
#     await message.channel.send("Ocimchi ,Sir!")
#   if message.content.startswith('+++'):
#     await message.channel.send("Hello There!,how I can help you")
#   if any(word in msg for word in sad_words):
#     await message.channel.send(random.choice(start_to_do))
#   if any(word in msg for word in sad_words):
#     for i in range(0,11):
#       await message.channel.send(i)
#       if i == 10:
#         await message.channel.send('ไม่มีใครเล่นเลยหรอ')
#   if any(word in msg for word in request_word):
#     # x = request_word
#     await message.channel.send("Owen เรียกคุณอยู่ "+" @Plasterbate")
#   '''if any(word in msg for word in alphaeng):
#     await message.channel.send("Hello " +'Im Ocimchi')'''
# #   if message.content.startswith('+quote'):
# #     await message.channel.send(random.choice(start_to_do))
# #   if message.content.startswith('music on'):
# #     await message.channel.send((random.choice(musiclist)))
#   if message.content.startswith('+pic1'):
#     await message.channel.send(file=discord.File('D:\Testbot/pic1.png'))

# @client2.command()
# async def play(ctx, url : str):
#     song_there = os.path.isfile("song.mp3")
#     try:
#         if song_there:
#             os.remove("song.mp3")
#     except PermissionError:
#         await ctx.send("Wait for the current playing music to end or use the 'stop' command")
#         return

#     voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
#     await voiceChannel.connect()
#     voice = discord.utils.get(client2.voice_clients, guild=ctx.guild)

#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#     }
#     with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([url])
#     for file in os.listdir("./"):
#         if file.endswith(".mp3"):
#             os.rename(file, "song.mp3")
#     voice.play(discord.FFmpegPCMAudio("song.mp3"))

# '''
# @client2.command()
# async def leave(ctx):
#     voice = discord.utils.get(client2.voice_clients, guild=ctx.guild)
#     if voice.is_connected():
#         await voice.disconnect()
#     else:
#         await ctx.send("The bot is not connected to a voice channel.")


# @client2.command()
# async def pause(ctx):
#     voice = discord.utils.get(client2.voice_clients, guild=ctx.guild)
#     if voice.is_playing():
#         voice.pause()
#     else:
#         await ctx.send("Currently no audio is playing.")


# @client2.command()
# async def resume(ctx):
#     voice = discord.utils.get(client2.voice_clients, guild=ctx.guild)
#     if voice.is_paused():
#         voice.resume()
#     else:
#         await ctx.send("The audio is not paused.")


# @client2.command()
# async def stop(ctx):
#     voice = discord.utils.get(client2.voice_clients, guild=ctx.guild)
#     voice.stop()'''


# client.run('ODE5NTQ4ODM4NzMzMDIxMjA0.YEoOVQ.qL7VNEu6ShnBBjwmFsVUAsSSb4Y')

# #client.run(os.environ['Tok'])

import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import datetime as dt

bot = commands.Bot(command_prefix='!')

# Things to run when the bot connects to Discord
@bot.event
async def on_ready():
    print('Connected!')
    
# @bot.event
# async def on_message(message):
#     if message.content.startswith('+pic1'):
#         await ctx.send('Working!', file=discord.File('pic1.png'))


# Test command
@bot.command(pass_context=True)
async def test(ctx):
    if ctx.content.startswith('+pic1'):
        await ctx.send('Working!', file=discord.File('pic1.png'))

bot.run('ODE5NTQ4ODM4NzMzMDIxMjA0.YEoOVQ.qL7VNEu6ShnBBjwmFsVUAsSSb4Y')