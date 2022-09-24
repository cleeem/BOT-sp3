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
        embed_stuff.set_image(url=data.gear_url)
        await ctx.send(embed=embed_stuff)


@bot.command()
async def drop(ctx):
    daily_brand = schedule.get_daily()
    embed_brand = Embed(title=f"THE DAILY DROP", description=f"Brand Name : {daily_brand.current_brand} \nFrequent Bonus : {daily_brand.frequent_bonus} {daily_brand.frequent_bonus_emote} \nEnd Time : {daily_brand.end_time}", color=0x33CAFF)
    embed_brand.set_thumbnail(url=daily_brand.brand_image)
    await ctx.send(embed=embed_brand)

    for stuff in daily_brand.liste_stuff:
        dico = { 'color': 3394303, 'type': 'rich', 'description': f"\n Price : {stuff.price}<:sp_coin:1010654259425062952> \n\n Ability : {stuff.bonus_emote} \n\n Name : {stuff.name}"}

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


def stuff_image(liste):
    for i,elt in enumerate(liste):
        if elt == "ssu":
            fs.ssu(i+1)

        elif elt == "rsu":
            fs.rsu(i+1)

        elif elt == "ism":
            fs.ism(i+1)

        elif elt == "scu":
            fs.scu(i+1)

        elif elt == "spu":
            fs.spu(i+1)
            
        elif elt == "ss":
            fs.ss(i+1)
            
        elif elt == "qsj":
            fs.qsj(i+1)
            
        elif elt == "qr":
            fs.qr(i+1)
            
        elif elt == "os":
            fs.os(i+1)
            
        # elif elt == "mpu":
        #     fs.mpu(i+1)

        # elif elt == "bdu":
        #     fs.bdu(i+1)
            
        elif elt == "iss":
            fs.iss(i+1)
            
        elif elt == "cbk":
            fs.cbk(i+1)
            
        elif elt == "ir":
            fs.ir(i+1)
            
        elif elt == "dr":
            fs.dr(i+1)
            
        elif elt == "iru":
            fs.iru(i+1)
            
        elif elt == "lde":
            fs.lde(i+1)
            
        elif elt == "sbpu":
            fs.sbpu(i+1)
            
        elif elt == "tnty":
            fs.tnty(i+1)
            
        elif elt == "hnt":
            fs.hnt(i+1)
            
        elif elt == "ns":
            fs.ns(i+1)
            
        elif elt == "thi":
            fs.thi(i+1)
            
        elif elt == "rsp":
            fs.rsp(i+1)
            
        elif elt == "sj":
            fs.sj(i+1)
            
        elif elt == "og":
            fs.og(i+1)

        elif elt == "sru":
            fs.sru(i+1)

        elif elt == "ia":
            fs.ia(i+1)
            
        elif elt == "ab":
            fs.ab(i+1)         
        
        elif elt == "uk":
            fs.uk(i+1)

        else:
            fs.uk(i+1)

    
def stuff_emote(liste):


@bot.command()
async def stuff(ctx, *args):
    liste_bonus = [elt.lower() for elt in args]
    if len(liste_bonus)<12: 
        for i in range(12-len(liste_bonus)):
            liste_bonus.append("uk")
    
    embed_message = Embed(description = f"How do you want your stuff? \nNote, image can take some time \nYou can save you stuff if you chose image" , color = 0x33CAFF)

    async def callback_image(interaction):
        if interaction.user.id == ctx.author.id:
            stuff_image(liste=liste_bonus)

            file = File("images_bot/emote_stuff/blanc_resultat.png", filename="blanc_resultat.png")
            embed = Embed(description="here is your stuff", color=0x33CAFF)
            embed.set_image(url=f"attachment://blanc_resultat.png")
            embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)
            await interaction.message.delete()
            await ctx.send(file=file, embed=embed)

    async def callback_emote(interaction):
        if interaction.user.id == ctx.author.id:
            pass

    button_image = bt.Button(label="image", style=ButtonStyle.primary)
    button_image.callback = callback_image

    button_emote = bt.Button(label="emote", style=ButtonStyle.primary)
    button_emote.callback = callback_emote


    view = bt.View()
    view.add_item(button_emote)
    view.add_item(button_image)

    await ctx.send(view=view, embed=embed_message)



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