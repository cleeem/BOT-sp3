###################
# DISCORD IMPORTS #
###################
from random import randint
from unicodedata import name
import discord.ui as bt
from discord import *
from discord.ext import commands
from discord.utils import get
from schedule import Daily_brand

######################
# MY MODULES IMPORTS #
######################
import schedule
# import fichier_stuff as fs

#################
# OTHER IMPORTS #
#################


client = Client()

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description="Bot de clem#1777", intents=intents)

bot.remove_command('help')


@bot.event
async def on_ready():
    print("Ready !")
    activity = Game(name=f"$help\nOn {len(bot.guilds)} servers", type=1)
    await bot.change_presence(status=Status.online, activity=activity)  


@bot.command()
async def map(ctx):
    for key in schedule.list_mode:
        rotatio_data = schedule.get_data(key)
        embed_rotation = Embed(title=f"MAPS : {rotatio_data.type}", description=rotatio_data, color=0x33CAFF)
        embed_rotation.set_thumbnail(url=rotatio_data.thumbnail_url)
        await ctx.send(embed=embed_rotation)

@bot.command()
async def rotation(ctx):
    await map(ctx)

@bot.command()
async def splatnet(ctx):

    for i in range(6):
        data = schedule.get_stuff(indice=i)
        dico = {'fields': [
            {'inline': True, 'name': "New Price", 'value': f"{data.new_price} <:sp_coin:1010654259425062952>"}, 
            {'inline': True, 'name': "New Ability", 'value': data.new_main_emote},
            {'inline': True, 'name': "Brand", 'value': data.brand},
            
            ], 'color': 3394303, 'type': 'rich', 'description': f"Available until {data.end_time}", "title" : data.name_stuff}

        embed_stuff = Embed.from_dict(dico)
        embed_stuff.set_thumbnail(url=data.gear_url)
        await ctx.send(embed=embed_stuff)


@bot.command()
async def drop(ctx):
    daily_brand = schedule.get_daily()
    embed_brand = Embed(title=f"THE DAILY DROP", description=f"Brand Name : {daily_brand.current_brand} \nFrequent Bonus : {daily_brand.frequent_bonus} {daily_brand.frequent_bonus_emote} \nEnd Time : {daily_brand.end_time}", color=0x33CAFF)
    embed_brand.set_thumbnail(url=daily_brand.brand_image)
    await ctx.send(embed=embed_brand)

    for stuff in daily_brand.liste_stuff:
        dico = {'fields': [
            {'inline': True, 'name': "Price", 'value': f"{stuff.price} <:sp_coin:1010654259425062952>"}, 
            {'inline': True, 'name': "Ability", 'value': stuff.bonus_emote},
            {'inline': False, 'name': "name", 'value': stuff.name},
            
            ], 'color': 3394303, 'type': 'rich', 'description': ""}

        embed_stuff = Embed.from_dict(dico)
        embed_stuff.set_thumbnail(url=stuff.url_image)
        await ctx.send(embed=embed_stuff)

@bot.command()
async def rw(ctx):
    liste_weapons = ['Rapid Blaster Pro', 'Clash Blaster', 'Rapid Blaster', 'Range Blaster', 'Blaster', 'Luna Blaster', 'Inkbrush', 'Octobrush', 'Gootuber', 'Bamboozler', 'E-Liter Scope', 'E-Liter', 'Splatterscope', 'Charger', 'Squiffer', 'Dualies Squelshers', 'Glooga Dualies', 'Dualies', 'Dapple Dualies', 'Tetra Dualies', 'Carbon Roller', 'Dynamo Roller', 'Flingza Roller', 'Roller', 'Splatana', 'Heavy Splatana', 'Undercover Brella', 'Brella', 'Tenta Brella', 'Aerospray', 'Splattershot Pro', 'Splattershot Jr', 'Squeezer', '.52 Gal', '.96 Gal', 'Jet Squelsher', 'Splattershot', 'Splash-o-matic', 'Nzap', 'Sploosh-o-matic', 'H-3 Nozzlenose', 'L-3 Nozzlenose', 'Bloblober', 'Tri Slosher', 'Sloshing Machine', 'Slosher', 'Explosher', 'Ballpoint Splatling', 'Hydra Splatling', 'Mini Splatling', 'Nautilus', 'Heavy Splatling', 'Stringer']
    indice = randint(0,len(liste_weapons)-1)
    weapon_name = liste_weapons[indice]
    url_weapon = f"images_bot/images_armes/{weapon_name}.png"
    
    file = File(url_weapon, filename=f"{weapon_name}.png")
    embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, vous devez prendre {weapon_name}")
    embed.set_image(url=f"attachment://{weapon_name}.png")
    await ctx.send(file=file, embed=embed)


import sys

try:
    sys.path.append("../token")
    import token_bot
except:
    sys.path.append("/home/cleeem/python/token")
    import token_bot
    
#bot principal
token_run_main = token_bot.tokens["token_bot_principal"]

#2eme bot
token1 = token_bot.tokens["token_bot_test"]

bot.run(token1)