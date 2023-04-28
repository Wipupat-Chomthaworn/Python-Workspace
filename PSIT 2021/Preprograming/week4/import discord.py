# import discord
# from discord.ext import commands
# tokens = ''
# client = commands.Bot(command_prefix = '.')

# @client.event
# async def on_ready():
#     print('We have logged in as {0.user}'.format(client))

# @client.command(pass_context=True)
# async def join(ctx):
#     channel = ctx.message.author.voice.voice_channel
#     await client.join_voice_channel(channel)

# @client.command(pass_context=True)
# async def leave(ctx):
#     server = ctx.message.server
#     voice_client = client.voice_client_in(server)
#     await voice_client.disconnect()



# client.run('ODE5NTQ4ODM4NzMzMDIxMjA0.YEoOVQ.qL7VNEu6ShnBBjwmFsVUAsSSb4Y')

# import discord
# from discord.ext import commands

# client = commands.Bot(command_prefix=".")

# @client.event
# async def on_ready():
# 	print("bot is ready")

# @client.command(pass_context=True)
# async def join(ctx):
#     if ctx.message.author.voice:
#         channel = ctx.message.author.voice.channel
#         await channel.connect()




# @client.command(pass_context=True)
# async def leave(ctx):
#     if ctx.message.author.voice:
#         #channel = ctx.message.author.voice.channel
#         server = ctx.message.guild.voice_client
#         await server.disconnect()


# client.run('ODE5NTQ4ODM4NzMzMDIxMjA0.YEoOVQ.qL7VNEu6ShnBBjwmFsVUAsSSb4Y')
# client.run('ODcwNTQ1MDcyMTAwMzYwMjYz.YQOURw.4R0pDZnZBQ6bTJ9HR_UjZYs2enc')
import discord
from discord.ext import commands
import youtube_dl
import os

client = commands.Bot(command_prefix="*")

@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.run('ODE5NTQ4ODM4NzMzMDIxMjA0.YEoOVQ.qL7VNEu6ShnBBjwmFsVUAsSSb4Y')

# If you wish to securely hide your token, you can do so in a .env file.
# 1. Create a .env in the same directory as your Python scripts
# 2. In the .env file format your variables like this: VARIABLE_NAME=your_token_here
# 3. At the top of the Python script, import os
# 4. In Python, you can read a .env file using this syntax:
# token = os.getenv(VARIABLE_NAME)