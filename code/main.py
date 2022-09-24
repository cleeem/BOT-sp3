###################
# DISCORD IMPORTS #
###################
import discord.ui as bt
from discord import *
from discord.ext import commands
from discord.utils import get


######################
# MY MODULES IMPORTS #
######################
import schedule
import fichier_stuff as fs

#################
# OTHER IMPORTS #
#################
from random import randint
import time


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
async def rw(ctx, *args):
    liste_weapons = ['Rapid_Blaster_Pro', 'Clash_Blaster', 'Rapid_Blaster', 'Range_Blaster', 'Blaster', 'Luna_Blaster', 'Inkbrush', 'Octobrush', 'Gootuber', 'Bamboozler', 'E-Liter_Scope', 'E-Liter', 'Splatterscope', 'Charger', 'Squiffer', 'Dualies_Squelshers', 'Glooga_Dualies', 'Dualies', 'Dapple_Dualies', 'Tetra_Dualies', 'Carbon_Roller', 'Dynamo_Roller', 'Flingza_Roller', 'Roller', 'Splatana', 'Splatana_Stamper', 'Undercover_Brella', 'Brella', 'Tenta_Brella', 'Aerospray', 'Splattershot_Pro', 'Splattershot_Jr', 'Squeezer', '52_Gal', '96_Gal', 'Jet_Squelsher', 'Splattershot', 'Splash-o-matic', 'Nzap', 'Sploosh-o-matic', 'H-3_Nozzlenose', 'L-3_Nozzlenose', 'Bloblober', 'Tri_Slosher', 'Sloshing_Machine', 'Slosher', 'Explosher', 'Ballpoint_Splatling', 'Hydra_Splatling', 'Mini_Splatling', 'Nautilus', 'Heavy_Splatling', 'Tri_Stringer', 'Reef_lux']

    liste_shooters = ['Aerospray', 'Splattershot_Pro', 'Splattershot_Jr', 'Squeezer', '52_Gal', '96_Gal', 'Jet_Squelsher', 'Splattershot', 'Splash-o-matic', 'Nzap', 'Sploosh-o-matic', 'H-3_Nozzlenose', 'L-3_Nozzlenose']

    liste_blasters = ['Rapid_Blaster_Pro', 'Clash_Blaster', 'Rapid_Blaster', 'Range_Blaster', 'Blaster', 'Luna_Blaster']

    liste_rollers = ['Inkbrush', 'Octobrush','Carbon_Roller', 'Dynamo_Roller', 'Flingza_Roller', 'Roller']

    liste_chargers = ['Gootuber', 'Bamboozler', 'E-Liter_Scope', 'E-Liter', 'Splatterscope', 'Charger', 'Squiffer']

    liste_dualies = ['Dualies_Squelshers', 'Glooga_Dualies', 'Dualies', 'Dapple_Dualies', 'Tetra_Dualies']

    liste_sloshers = ['Bloblober', 'Tri_Slosher', 'Sloshing_Machine', 'Slosher', 'Explosher']

    liste_splatlings = ['Ballpoint_Splatling', 'Hydra_Splatling', 'Mini_Splatling', 'Nautilus', 'Heavy_Splatling']

    liste_brellas = ['Undercover_Brella', 'Brella', 'Tenta_Brella']

    liste_splatanas = ['Splatana', 'Splatana_Stamper']

    liste_stringers = ['Tri_Stringer', 'Reef_lux']

    if len(args) == 0 or args[0]=="random":
        indice = randint(0,len(liste_weapons)-1)
        weapon_name = liste_weapons[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "shooter":
        indice = randint(0,len(liste_shooters)-1)
        weapon_name = liste_shooters[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "roller":
        indice = randint(0,len(liste_rollers)-1)
        weapon_name = liste_rollers[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "charger":
        indice = randint(0,len(liste_chargers)-1)
        weapon_name = liste_chargers[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "blaster":
        indice = randint(0,len(liste_blasters)-1)
        weapon_name = liste_blasters[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "slosher":
        indice = randint(0,len(liste_sloshers)-1)
        weapon_name = liste_sloshers[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "brella":
        indice = randint(0,len(liste_brellas)-1)
        weapon_name = liste_brellas[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "dualies":
        indice = randint(0,len(liste_dualies)-1)
        weapon_name = liste_dualies[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "splatling":
        indice = randint(0,len(liste_splatlings)-1)
        weapon_name = liste_splatlings[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "splatana":
        indice = randint(0,len(liste_splatanas)-1)
        weapon_name = liste_splatanas[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
        await ctx.send(file=file, embed=embed)

    elif args[0] == "stringer":
        indice = randint(0,len(liste_stringers)-1)
        weapon_name = liste_stringers[indice]
        url_weapon = f"images_bot/images_armes/{weapon_name}.png"
        
        file = File(url_weapon, filename=f"{weapon_name}.png")
        temp = weapon_name.replace("_"," ")
        embed = Embed(title="Random Weapon", description=f"{ctx.author.mention}, you must play : {temp}", color=0x33CAFF)
        embed.set_image(url=f"attachment://{weapon_name}.png")
        embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
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