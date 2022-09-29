###################
# DISCORD IMPORTS #
###################
from os import listdir
from xmlrpc.server import list_public_methods
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
    stuf = []

    for i,elt in enumerate(liste):
        if elt == "ssu":
            stuf.append("<:ssu:855390371827023882>")

        elif elt == "rsu":
            stuf.append('<:rsu:855390367264407572>')

        elif elt == "ism":
            stuf.append('<:ism:855390367586975745>')

        elif elt == "scu":
            stuf.append('<:scu:855390371840000001>')

        elif elt == "spu":
            stuf.append('<:spu:855390372254318622>')
        
        elif elt == "ss":
            stuf.append('<:ss:855390372129144842>')
            
        elif elt == "qsj":
            stuf.append('<:qsj:855390367745310750>')
            
        elif elt == "qr":
            stuf.append('<:qr:855390372208312330>')
            
        elif elt == "os":
            stuf.append('<:os:855390368778027038>')
            
        # elif elt == "mpu":
        #     stuf.append('<:mpu:855390368131842068>')

        # elif elt == "bdu":
        #     stuf.append('<:bdu:855390365708058624>')
            
        elif elt == "iss":
            stuf.append('<:iss:855390372125868063>')
            
        elif elt == "cbk":
            stuf.append('<:bdu:855390365708058624>')
            
        elif elt == "ir":
            stuf.append('<:ir:855390370362556436>')
            
        elif elt == "dr":
            stuf.append('<:dr:855390372204773387>')
            
        elif elt == "iru":
            stuf.append('<:iru:855390367464292352>')
            
        elif elt == "lde":
            stuf.append('<:lde:855390366755717120>')
            
        elif elt == "sbpu":
            stuf.append('<:sbpu:855390365895753749>')
            
        elif elt == "tnty":
            stuf.append('<:tnty:855390368065388576>')
            
        elif elt == "hnt":
            stuf.append('<:hnt:855390366453989426>')
            
        elif elt == "ns":
            stuf.append('<:ns:855390376185692180>')
            
        elif elt == "thi":
            stuf.append('<:ti:855390376374304798>')
            
        elif elt == "rsp":
            stuf.append('<:rp:855390366991646730>')
            
        elif elt == "sj":
            stuf.append('<:sj:855390376235892756>')
            
        elif elt == "og":
            stuf.append('<:og:855390372141465610>')

        elif elt == "sru":
            stuf.append("<:sru:1019332176782839868>")

        elif elt == "ia":
            stuf.append("<:ia:1019332137687724032>")
            
        elif elt == "ab":
            stuf.append('<:ab:855479824009527306> ')         
        
        elif elt == "uk":
            stuf.append('<:uk:855479856511057951>')
        
        else:
            stuf.append('<:uk:855479856511057951>')

        if i == 3 or i == 7:
            stuf.append("oui")

    res = str(stuf).replace("'","").replace(",","").replace("[","").replace("]","").replace("oui","""
""")
    return res

@bot.command()
async def stuff(ctx, *args):
    liste_bonus = [elt.lower() for elt in args]
    if len(liste_bonus)<12: 
        for i in range(12-len(liste_bonus)):
            liste_bonus.append("uk")
    
    embed_message = Embed(description = f"How do you want your stuff? \nNote, image can take some time" , color = 0x33CAFF)

    id = ctx.author.id

    def checkMessage(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    async def callback_save(interaction):
        await ctx.send("chose a name for your stuff")
        message_stuff = await bot.wait_for("message", check = checkMessage)
        nom_stuff = message_stuff.content
        nom_stuff = str(nom_stuff).replace(" ","_").replace("+","_")
        
        fs.save(id=id, nom_stuff=nom_stuff)
            
        

    async def callback_image(interaction):
        if interaction.user.id == ctx.author.id:
            stuff_image(liste=liste_bonus)

            file = File("images_bot/emote_stuff/blanc_resultat.png", filename="blanc_resultat.png")
            embed = Embed(title="STUFF", description="here is your stuff", color=0x33CAFF)
            embed.set_image(url=f"attachment://blanc_resultat.png")
            embed.set_footer(text=time.ctime(time.time()), icon_url=ctx.author.avatar)

            # button_save = bt.Button(label="save", style=ButtonStyle.primary)
            # button_save.callback = callback_save

            # view.add_item(button_save)

            await interaction.message.delete()
            await ctx.send(file=file, embed=embed)
            fs.clear()

    async def callback_emote(interaction):
        if interaction.user.id == ctx.author.id:
            res_stuff = stuff_emote(liste=liste_bonus)
            embed_stuff = Embed(title="STUFF", description="here is your stuff \n" + res_stuff, color=0x33CAFF)
            await interaction.message.edit(embed=embed_stuff)

    button_image = bt.Button(label="image", style=ButtonStyle.primary)
    button_image.callback = callback_image

    button_emote = bt.Button(label="emote", style=ButtonStyle.primary)
    button_emote.callback = callback_emote


    view = bt.View()
    view.add_item(button_emote)
    view.add_item(button_image)

    await ctx.send(view=view, embed=embed_message)

@bot.command()
async def bonus(ctx):
    embed = Embed(title="Bonus", description="""ssu <:ssu:855390371827023882> ; scu <:scu:855390371840000001> ; iss <:iss:855390372125868063> ; ss <:ss:855390372129144842> 
\nsbpu <:sbpu:855390365895753749> ; og <:og:855390372141465610> ; dr <:dr:855390372204773387> ; qr <:qr:855390372208312330>  
\nspu <:spu:855390372254318622> ; ns <:ns:855390376185692180> ; sj <:sj:855390376235892756> ; ti <:ti:855390376374304798>
\nsbpu <:sbpu:855390365895753749> ; hnt <:hnt:855390366453989426> ; lde <:lde:855390366755717120> ; rp <:rp:855390366991646730>
\nrsu <:rsu:855390367264407572> ; iru <:iru:855390367464292352> ; ism <:ism:855390367586975745> ; qsj <:qsj:855390367745310750>
\ntnty <:tnty:855390368065388576> ; os <:os:855390368778027038> ; ir <:ir:855390370362556436> ; ia <:ia:1019332137687724032>
\nsru <:sru:1019332176782839868> ; ab <:ab:855479824009527306> ; uk <:uk:855479856511057951>
                                                """, color=0x33CAFF)
    await ctx.send(embed=embed)
    
@bot.command()
async def github(ctx):
    await ctx.send("https://github.com/cleeem/BOT-sp3")

@bot.command()
async def help(ctx):
    message_commande = ctx.message

    membre = ctx.author

    dico_embed1 = {'fields': [
            {'inline': False, 'name': "Command : map ", 'value': "``` show the current rotation in every mode ```"}, 
            {'inline': False, 'name': "Command : drop ", 'value': "``` show the drop of the day ```"},
            {'inline': False, 'name': "Command : splatnet ", 'value': "``` show the current gears in the app ```"},
            {'inline': False, 'name': "Command : rw *type* ", 'value': "``` gives you a randow weapon \n (you can specifie the type) \n shooter ; roller; charger; slosher; splatling \n brella ; blaster ; dualies ; splatana ; stringer ```"},
            {'inline': False, 'name': "Command : stuff *bonus* ", 'value': "``` chose up to 12 bonuses in your stuff \n Use the bonus command to see their name```"},
            {'inline': False, 'name': "Command : bonus ", 'value': "``` show all the bonuses ```"}, 
            
            ], 'title' : 'Help' , 'color': 3394303, 'type': 'rich', 'description': ""}

    embed_help_1 = Embed.from_dict(dico_embed1)     

    dico_embed_docu = {'fields': [
            {'inline': False, 'name': "What language do i use?", 'value': "```I use Python and discord.py``` (https://discordpy.readthedocs.io/en/latest/api.html) "}, 
            {'inline': False, 'name': "Where do i host the bot? ", 'value': "```I currently use Alwaydata, it provide free machine you can use with ssh\n(free under 100Mb of data) ```"},
            {'inline': False, 'name': "What IDE do i use?", 'value': "```I use Visual Studio Code (it's free) ```"}, 
            {'inline': False, 'name': "Splatoon.ink     (https://splatoon2.ink)", 'value': "```For all the splatnet informations ```"}, 
            {'inline': False, 'name': "Inkpedia     (https://splatoonwiki.org/wiki/Main_Page)", 'value': "```For the emotes and some images ```"}, 

            
            ], 'title' : 'Documentation' , 'color': 3394303, 'type': 'rich', 'description': "You will find here some informations about the code or what i used"}

    embed_docu = Embed.from_dict(dico_embed_docu)   


    async def callback_1(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(view=view, embed = embed_help_1)

    async def callback_docu(interaction):
        if interaction.user.id == membre.id:
            await interaction.message.edit(view=view, embed = embed_docu)

    async def callback_destroy(interaction):
        if interaction.user.id == membre.id:
            await message_commande.delete()


    button_1 = bt.Button(label="page 1", style=ButtonStyle.blurple)
    button_1.callback = callback_1

    button_docu = bt.Button(label="Documentation",style=ButtonStyle.green)
    button_docu.callback = callback_docu

    button_destroy = bt.Button(style=ButtonStyle.danger, label="X")
    button_destroy.callback = callback_destroy

    button_github = bt.Button(style=ButtonStyle.link, label="github", url="https://github.com/cleeem/BOT-sp3")


    view = bt.View()
    view.add_item(button_1)
    view.add_item(button_docu)
    view.add_item(button_destroy)
    view.add_item(button_github)

    await ctx.send(view=view, embed=embed_help_1)


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