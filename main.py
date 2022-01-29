import discord
from discord_components import DiscordComponents, Button, ButtonStyle
import json
import requests
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])
@bot.remove_command('help')

@bot.command()
async def bird(ctx):
    response = requests.get('https://some-random-api.ml/img/birb') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Bird') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed


@bot.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Dog') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Cat') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command()
async def mem(ctx):
    await ctx.send('Итанчик лох')

@bot.command()
async def mem2(ctx):
    await ctx.send('Минар гей')

@bot.command()
async def mem3(ctx):
    await ctx.send('DarkenRal долбоеб')

@bot.command()
async def mem4(ctx):
    await ctx.send('Телек рукаблудник')
    
@bot.command()
async def mem5(ctx):
    await ctx.send('Zer1k15 писькагрыз')

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') # Get-запрос
    json_data = json.loads(response.text) # Извлекаем JSON

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') # Создание Embed'a
    embed.set_image(url = json_data['link']) # Устанавливаем картинку Embed'a
    await ctx.send(embed = embed) # Отправляем Embed

@bot.command() # Не передаём аргумент pass_context, так как он был нужен в старых версиях.
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!')

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount)

#kick
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def kick (ctx, member: discord.Member, *, reason = None):
    await ctx.channel.purge(limit = 1)

    await member.kick(reason = reason)
    await ctx.send(f'kick user {member.mention }')


#ban
@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def ban (ctx, member: discord.Member, *, reason):
    await ctx.channel.purge(limit = 1)

    await member.ban(reason = reason)
    await ctx.send(f'ban user {member.mention }')

@bot.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def help(ctx):
    emb = discord.Embed(title = 'Помощь с командами')

    emb.add_field(name = '!clear', value = 'Очистка чата')
    emb.add_field(name = '!ban', value = 'Бан пользователя')
    emb.add_field(name = '!kick', value = 'Кик пользователя')
    emb.add_field(name = '!mute', value = 'Мут пользователя')
    emb.add_field(name = '!fox', value = 'Рандомная лиса')
    emb.add_field(name = '!bird', value = 'Рандомная птица')
    emb.add_field(name = '!mem', value = 'Интересный факт')
    emb.add_field(name = '!cat', value = 'Рандомный кот')
    emb.add_field(name = '!dog', value = 'Рандомный пес')
    emb.add_field(name = '!mem2', value = 'Прикольный факт')
    emb.add_field(name = '!mem3', value = 'Страшный секрет')
    emb.add_field(name = '!mem4', value = 'Очевидный факт')
    emb.add_field(name = '!mem5', value = 'Ужасная тайна')
    
    await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions(administrator = True)

async def mute(ctx, member: discord.Member):
    await ctx.channel.purge(limit = 1)

    mute_role = discord.utils.get(ctx.message.guild.roles, name = 'mute')
    await member.add_roles(mute_role)
    await ctx.send(f'У {member.mention} ограничение чата за нарушение')

@bot.event
async def on_member_join(member):
    channel = client.get_channel(913837695774638102)

    role = discord.utils.get(member.guild.roles, id = 913763303568850954)

    await member.add_roles(role)
    await channel.send(embed = discord.Embed(description = f'Пользователь {member.name},присоединился к нам', color = 0x0c0c))

@bot.event
async def on_ready():
    print('Bot connected')

    await bot.change_presence(status = discord.Status.online, activity = discord.Game('Real Life'))

bot.run(input())
