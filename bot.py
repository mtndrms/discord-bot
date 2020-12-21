import discord
from discord.ext import commands
from youtube_search import YoutubeSearch

TXT = open('token.txt', 'r')
TOKEN = TXT.read()

print(TOKEN)
client = commands.Bot(command_prefix = "!")
client.remove_command("help")

def search_yt(keyword):
    results = YoutubeSearch(keyword, max_results=3).to_dict()
    first_video_id = results[0]["id"]
    video_url = "https://www.youtube.com/watch?v=" + first_video_id
    return video_url

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Code'))
    print("Bot is ready!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello")

@client.command()
async def echo(ctx, *, arg):
    await ctx.send(arg)

@client.command()
async def delete(ctx, arg):
    channel = ctx.message.channel
    async for m in channel.history(limit = int(arg) + 1): # type of m is a message & +1 exists because it's deletes the line of command called
        await m.delete() # delete() can only be use with a message
    await ctx.send("Message(s) deleted!")

@client.command()
async def yt(ctx, *, arg):
    result = search_yt(arg)
    await ctx.send(result)

@client.command()
async def help(ctx):
    author = ctx.message.author
    embedHelp = discord.Embed(colour = discord.Colour.dark_grey())   
    
    embedHelp.set_author(name="HELP")
    embedHelp.add_field(name="!hello", value="---", inline=True)
    embedHelp.add_field(name="!echo", value="--- ", inline=True)
    embedHelp.add_field(name="!delete <number>", value="Deletes the message for the number entered.", inline=False)
    embedHelp.add_field(name="!yt", value="Search on youtube.", inline=False)

    await ctx.send(embed=embedHelp)

client.run(TOKEN)