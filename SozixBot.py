# Import libraries
import discord
from discord.ext import commands
import time

# Bot Prefix
bot = commands.Bot(command_prefix='!', help_command=None, intents=discord.Intents.all())

# Constants
TOKEN = ''  # bot token
BOT_NAME = 'Sozix'
DEVELOPER_NAME = 'Salman Rajab'
OWNER_OF_THE_BOT = 'Salman Rajab'
PREFIX = '!'






# Bot event
@bot.event
async def on_ready():  # send message when the bot is ready
    activity = discord.Game(name=f"{PREFIX}help", type=3)
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=activity)
    print("-----------------------------")
    print(f"Bot logged as {bot.user}")
    print("The bot is now ready to use.")
    print("This Bot Made by", DEVELOPER_NAME, "Bot name :", BOT_NAME, "\nOwner of the bot is", OWNER_OF_THE_BOT)
    print("-----------------------------")


@bot.command()  # Clear chat command
async def clear(ctx, *, amount=0):
    await ctx.channel.purge(limit=amount + 1)
    if amount > 1:
        await ctx.send(f"`{amount} messages has been deleted`")
    else:
        await ctx.send(f"`{amount} message has been deleted`")
        time.sleep(1.2)
        await ctx.channel.purge(limit=1)



# Help command
@bot.command()
async def help(context):
    embed = discord.Embed(
        colour=discord.Colour.random(),
        title="About Sozix Bot",
        description="**Sozix Bot is a General bot**\n"
                    "It can show your ping, display avatars, and clear chat.\n"

    )
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/1088247207397953558/1091829023660847154/sozixn.jpg')

    embed.set_footer(text=f"Need More help? Please contact us")

    embed.add_field(
        name="General commands",
        value=f"{PREFIX}avatar - Displays your avatar or someone else's avatar.\n"
              f"{PREFIX}ping - Checks the bot's latency.\n"
              f"{PREFIX}clear - Clears the chat messages.",
        inline=False
    )

    await context.send(embed=embed)




# Avatar command
@bot.command()  # avatar command
async def avatar(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author
    favatar = discord.Embed(title=f"{member.name}'s avatar", colour=discord.Colour.random())
    favatar.set_footer(text=f"Requested by {ctx.author.name}")

    favatar.set_image(url='{}'.format(member.avatar.url))
    await ctx.send(embed=favatar)


# Ping command
@bot.command()  # ping command
async def ping(ctx):
    await ctx.send(f'Pong! **{round(bot.latency * 1000)}ms**')




bot.run(TOKEN)
