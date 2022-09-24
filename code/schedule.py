import json
import requests


##################################
# Toutes les données nécessaires #
##################################


dico_emote = {
    "Clam Blitz" : "<:cb:853656449825243166>",
    "Rainmaker" : "<:rm:853656465725456424>",
    "Tower Control" : "<:tc:853656463846146068>",
    "Splat Zones" : "<:sz:853656465423990807>",
    "Turf War" : "<:turf:1010462680663994418>"
}

dico_armes = {
    "Sploosh-o-matic" : "<:sploosh:1010480744860221440>",
    "Splattershot Jr." : "<:jr:1010480455935606835>",
    "Splash-o-matic" : "<:splash:1010480508263739442>",
    "Splattershot" : "<:splattershot:1010480502341378078>",
    ".52 Gal" : "<:52:1010480347051470889>",
    "N-ZAP '85" : "<:zap:1010480527041626212>",
    "Splattershot Pro" : "<:pro:1010480489150283797>",
    ".96 Gal" : "<:96:1010480370225000488>",
    "Jet Squelcher" : "<:vjs:1010480520624349246>",
    "Luna Blaster" : "<:luna:1010480475581718559>",
    "Blaster" : "<:blaster:1010480387379703879>",
    "Range Blaster" : "<:rb:1010480513833783296>",
    "Clash Blaster" : "<:clash:1010480411757002752>",
    "Rapid Blaster" : "<:rapid:1010480495102005281>",
    "Rapid Blaster Pro" : "<:rapid_pro:1010480546431897680>",
    "L-3 Nozzlenose" : "<:l3:1010480468896002049>",
    "H-3 Nozzlenose" : "<:h3:1010480445378543687>",
    "Squeezer" : "<:squeezer:1010480536365576272>",
    "Carbon Roller" : "<:carbon:1010480104100606002>",
    "Splat Roller" : "<:roller:1010480240310628372>",
    "Dynamo Roller" : "<:dynamo:1010480141153095731>",
    "Flingza Roller" : "<:flingza:1010480170009890837>",
    "Inkbrush" : "<:brush:1010480211462201374>",
    "Octobrush" : "<:octobrush:1010480271633694760>",
    "Classic Squiffer" : "<:squiffer:1010479578654978119>",
    "Splat Charger" : "<:charger:1010479663367331871>",
    "Splatterscope" : "<:scope:1010479699861970984>",
    "E-liter 4K" : "<:eliter:1010479738592165959>",
    "E-liter 4K Scope" : "<:scope_e:1010479773698498610>",
    "Bamboozler 14 Mk I" : "<:bamboo:1010479551522033674>",
    "Goo Tuber" : "<:gootuber:1010479619562029076>",
    "Slosher" : "<:slosher:1010480833368428594>",
    "Tri-Slosher" : "<:tri:1010480890545193072>",
    "Sloshing Machine" : "<:machine:1010480865450676305>",
    "Bloblobber" : "<:blob:1010480782315372564>",
    "Explosher" : "<:explo:1010480807955152917>",
    "Mini Splatling" : "<:mini:1010480997260865678>",
    "Heavy Splatling" : "<:heavy:1010481066408149025>",
    "Hydra Splatling" : "<:hydra:1010480972552228884>",
    "Ballpoint Splatling" : "<:bp:1010480947373817876>",
    "Nautilus 47" : "<:naut:1010481030689472532>",
    "Dapple Dualies" : "<:dapple:1010479913746309130>",
    "Splat Dualies" : "<:dualies:1010479952006750240>",
    "Glooga Dualies" : "<:glooga:1010480064770605087>",
    "Dualie Squelchers" : "<:vds:1010479983501791252>",
    "Dark Tetra Dualies" : "<:tetra:1010480021611221042>",
    "Splat Brella" : "<:brella:1010479399881150474>",
    "Tenta Brella" : "<:tent:1010479510581411880>",
    "Undercover Brella" : "<:under:1010479455338242069>",
    "Random" : "<:uk:1009071227043852310>",

}

dico_stuff = {
    "Main Power Up" : "<:mpu:1009070739170799626>",
    "Ability Doubler" : "<:ab:1009070271661084733>",
    "Run Speed Up" : "<:rsu:1009070594911907901>",
    "Swim Speed Up" : "<:ssu:1009071046105759865>",
    "Ink Saver (Main)" : "<:ism:1009070712822181901>",
    "Ink Saver (Sub)" : "<:iss:1009071116842717275>",
    "Special Saver" : "<:ss:1009070872616763463>",
    "Special Charge Up" : "<:scu:1009070989474271322>",
    "Quick Respawn" : "<:qr:1009070895383466046>",
    "Quick Super Jump" : "<:qsj:1009070688256151624>",
    "Comeback" : "<:cbk:1009070396429062195>",
    "Ink Resistance Up" : "<:ir:1009070848931532881>",
    "Sub Resistance Up" : "<:sru:1019332176782839868>",
    "Respawn Punisher" : "<:rsp:1009070563580452914>",
    "question mark" : "<:uk:1009071227043852310>",
    "uk" : "<:uk:1009071227043852310>",
    "Stealth Jump" : "<:sj:1009071141664604200>",
    "Special Power Up" : "<:spu:1009071008021483530>",
    "Ink Recovery Up" : "<:iru:1009070659843919913>",
    "Object Shredder" : "<:os:1009070825023995996>",
    "Last-Ditch Effort" : "<:lde:1009070541711343756>",
    "Ninja Squid" : "<:ns:1009071068360753242>",
    "Drop Roller" : "<:dr:1009070967785525299>",
    "Thermal Ink" : "<:ti:1009071170018095126>",
    "Tenacity" : "<:tnty:1009070763745234944>",
    "Opening Gambit" : "<:og:1009071094352838727>",
    "Haunt" : "<:hnt:1009070429064941628>",
    "Sub Power Up" : "<:sbpu:1009070353810735196>",
    "Intensify Action" : "<:ia:1019332137687724032>",
}


list_mode = ["regularSchedules", "xSchedules", "bankaraSchedules"]

url_assets = "https://splatoon2.ink/assets/splatnet/"


#############################################################################
# Creation des différentes classes pour accéder aux données plus facilement #
#############################################################################


class Rotation:
    def __init__(self, data) -> None:
        self.thumbnail_url = ""

        for k in data.keys():

            if "regular" in k:
                settings = "regularMatchSetting"
                self.thumbnail_url = "http://splating.ink/turf.png"
            elif "bankara" in k:
                settings = "bankaraMatchSettings"
                self.thumbnail_url = "http://splating.ink/rank.png"
            elif "x" in k:
                settings = "xMatchSetting"
                self.thumbnail_url = "http://splating.ink/rank.png"

        if settings == "bankaraMatchSettings":
            self.type = "Anarchy Battle Open"

            current_stage_a = data[settings][0]["vsStages"][0]["name"]
            current_stage_b = data[settings][0]["vsStages"][1]["name"]
            self.current_maps = f"{current_stage_a} and {current_stage_b}"
            self.current_mode = data[settings][1]["vsRule"]["name"] #+ " " + dico_emote[data["vsRule"]["name"]]
            self.current_start_time =data["startTime"][11:16]
            self.current_end_time = data["endTime"][11:16]
            
        else:
            if "Turf" in data[settings]["vsRule"]["name"]:
                self.type = data[settings]["vsRule"]["name"]
            else:
                self.type = "Anarchy Battle Series"

            current_stage_a = data[settings]["vsStages"][0]["name"]
            current_stage_b = data[settings]["vsStages"][1]["name"]
            self.current_maps = f"{current_stage_a} and {current_stage_b}"
            self.current_mode = data[settings]["vsRule"]["name"] #+ " " + dico_emote[data["vsRule"]["name"]]
            self.current_start_time =data["startTime"][11:16]
            self.current_end_time = data["endTime"][11:16]


    def __str__(self) -> str:
        return f"Current Rotation : \nMaps : {self.current_maps} \nMode : {self.current_mode} \n{self.current_start_time} to {self.current_end_time} \n\n"


class Stuff:
    def __init__(self, data, indice=0):
        self.name_stuff = data[indice]["gear"]["name"]
        self.brand = data[indice]["gear"]["brand"]["name"]
        self.new_price = data[indice]["price"]
        
        self.new_main = data[indice]["gear"]["primaryGearPower"]["name"]
        self.new_main_emote = dico_stuff[self.new_main]

        self.gear_url = data[indice]["gear"]["image"]["url"]
        self.end_time = data[indice]["saleEndTime"]
        
        try:
            self.frequent_bonus = data[indice]["gear"]["brand"]["frequent_skill"]["name"]
            self.frequent_bonus_emote = dico_stuff[self.frequent_bonus]
        except:
            self.frequent_bonus_emote = dico_stuff["uk"]
            self.frequent_bonus = "None"            
    
    def __str__(self) -> str:
        return f"{self.gear_url} \n{self.brand} jusqu'au \n{self.end_time} \n\nnew : {self.new_main} {self.new_price} "


class Daily_stuff:
    def __init__(self, data) -> None:
        self.price = data["price"]
        self.name = data["gear"]["name"]
        self.bonus = data["gear"]["primaryGearPower"]["name"]
        self.bonus_emote = dico_stuff[self.bonus]
        self.url_image = data["gear"]["image"]["url"]

    def __str__(self) -> str:
        return f"Name : {self.name}   Bonus : {self.bonus} {self.bonus_emote}    Price : {self.price}   url : {self.url_image} "


class Daily_brand:
    def __init__(self, data) -> None:
        self.current_brand = data["brand"]["name"]
        self.frequent_bonus = data["brand"]["usualGearPower"]["name"]
        self.frequent_bonus_emote = dico_stuff[self.frequent_bonus]
        self.end_time = data["saleEndTime"][11:16]
        self.brand_image = data["brandGears"][0]["gear"]["brand"]["image"]["url"]
        self.liste_stuff = []

        for stuff in data["brandGears"]:
            self.liste_stuff.append(Daily_stuff(stuff))

    def __str__(self) -> str:
        return f"Brand : {self.current_brand} \nfrequent bonus : {self.frequent_bonus} {self.frequent_bonus_emote} \nEnd Time : {self.end_time} \n Stuff 1 : {self.liste_stuff[0]} \n Stuff 2 : {self.liste_stuff[1]} \n Stuff 3 : {self.liste_stuff[2]}"

########################################################
# Fonctions permettant au bot de récupérer les données #
########################################################


def get_data(key):
    url = "https://splatoon3.ink/data/schedules.json"
    response_maps = requests.get(url=url)
    data_maps = json.loads(response_maps.text)

    data = data_maps["data"]

    for elt in data[key]["nodes"][0:1]:
        rotation_data = Rotation(data=elt)  

    return rotation_data

    
def get_stuff(indice):
    url_stuff = "https://splatoon3.ink/data/gear.json"
    response_stuff = requests.get(url=url_stuff)
    data_stuff = json.loads(response_stuff.text)
    data_stuff = data_stuff["data"]["gesotown"]["limitedGears"]

    stuff_data = Stuff(data=data_stuff, indice=indice)
    return stuff_data

def get_daily():
    url_stuff = "https://splatoon3.ink/data/gear.json"
    response_stuff = requests.get(url=url_stuff)
    data_stuff = json.loads(response_stuff.text)
    data_stuff = data_stuff["data"]["gesotown"]["pickupBrand"]

    daily_gears = Daily_brand(data=data_stuff)

    return daily_gears
    