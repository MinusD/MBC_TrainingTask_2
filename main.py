import re
import discord
import config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.CMD_PREFIX, intents=intents)


class User:
    def __init__(self, user_id: int):
        self.id: int = user_id
        self.win: int = 0
        self.lose: int = 0


def repl(t):
    return f'***{t.group()}***' if int(t.group()) > 100 else f'*{t.group()}*'


@bot.command()
async def numbers(ctx):
    text = ctx.message.content[len(str(ctx.command)) + len(str(ctx.prefix)):] + '\n'
    pattern = r'([\d]+)'
    result = f'> {text}'
    result += re.sub(pattern, repl, text)
    await ctx.send(result)



bot.run(config.TOKEN)
