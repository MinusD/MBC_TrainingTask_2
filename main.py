import re
import time as tm
import discord
import config
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.CMD_PREFIX, intents=intents)


def repl(t):
    return f'***{t.group()}***' if int(t.group()) > 100 else f'*{t.group()}*'


@bot.command()
async def numbers(ctx):
    """
    Принимает предложение в качестве аргумента. Возвращает то же самое предложение,
    но все числа становятся курсивными, а числа > 100 ещё жирными.
    """
    text = ctx.message.content[len(str(ctx.command)) + len(str(ctx.prefix)):] + '\n'
    pattern = r'([\d]+)'
    result = f'> {text}'
    result += re.sub(pattern, repl, text)
    await ctx.send(result)


@bot.command()
async def time(ctx):
    """
    Возвращает текущее время, сколько секунд осталось до следующего ровного часа.
    Время, которое будет через данное количество секунд. (Т.е. как раз ровное время по часам)
    """
    t = round(tm.time())
    mod = t % 3600
    result = f'<t:{t}>\nОсталось секунд **{mod}**\n<t:{t - mod + 3600}>'
    await ctx.send(result)


bot.run(config.TOKEN)
