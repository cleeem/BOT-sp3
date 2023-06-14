import os
from PIL import Image

TRANSLATE_EMOTE = {
    "ab" : "<:AbilityDobler:1101961554343243867>",
    "cbk" : "<:Comeback:1101961559623880755>",
    "hnt" : "<:Haunt:1101961562765410314>",
    "lde" : "<:LastDitchEffort:1101961564485066842>",
    "rsp" : "<:RespawnPunisher:1101961566808715324>",
    "rsu" : "<:RunSpeedUp:1101961570747162704>",
    "iru" : "<:InkRecoveryUp:1101961572202586286>",
    "ia" : "<:IntensifyAction:1101961575297994863>",
    "qsj" : "<:QuickSuperJump:1101961577168654528>",
    "ism" : "<:InkSaverMain:1101961579639087145>",
    "tnty" : "<:Tenacity:1101961582717710387>",
    "ir" : "<:InkResistance:1101961586257703024>",
    "qr" : "<:QuickRespawn:1101961591269888000>",
    "dr" : "<:DropRoller:1101961594109444136>",
    "spu" : "<:SpecialPowerUp:1101961596969955439>",
    "ns" : "<:NinjaSquid:1101961600644161707>",
    "sru" : "<:SubResistanceUp:1101961605299843194>",
    "ti" : "<:ThermalInk:1101961614321791019>",
    "os" : "<:ObjectShredder:1101961872955166813>",
    "ss" : "<:SpecialSaver:1101961938654736434>",
    "scu" : "<:SpecialChargeUp:1101962014382886992>",
    "ssu" : "<:SwimSpeedUp:1101962031021699162>",
    "sj" : "<:StealthJump:1101962048360956046>",
    "sbpu" : "<:SubPowerUp:1101962124047159366>",
    "uk" : "<:Unknown:1101962135719907481>",
    "iss" : "<:InkSaverSub:1101965441691303966>",
    "og" : "<:OpenGambit:1101965472850780191>",
}

TRANSLATE_IMAGES = {
    "ab"    : "Ability Dobler",
    "cbk"   : "Comeback",
    "hnt"   : "Haunt",
    "lde"   : "Last-Ditch Effort",
    "rsp"   : "Respawn Punisher",
    "rsu"   : "Run Speed Up",
    "iru"   : "Ink Recovery Up",
    "ia"    : "Intensify Action",
    "qsj"   : "Quick Super Jump",
    "ism"   : "In kSaver (Main)",
    "tnty"  : "Tenacity",
    "ir"    : "Ink Resistance Up",
    "qr"    : "Quick Respawn",
    "dr"    : "Drop Roller",
    "spu"   : "Special Power Up",
    "ns"    : "Ninja Squid",
    "sru"   : "Sub Resistance Up",
    "ti"    : "Thermal Ink",
    "os"    : "Object Shredder",
    "ss"    : "Special Saver",
    "scu"   : "Special Charge Up",
    "ssu"   : "Swim Speed Up",
    "sj"    : "Stealth Jump",
    "sbpu"  : "Sub Power Up",
    "uk"    : "Unknown",
    "iss"   : "Ink Saver (Sub)",
    "og"    : "Opening Gambit",
}

def new():
    img = Image.new(mode="RGBA"  ,size=(400,300))

    return img


def add(img, elt: str, index: int):
    bonus_image = Image.open(
        f"images_bot/emote_stuff/{TRANSLATE_IMAGES[elt]}.png"
    )

    width  = int(400 * (index % 4 * 0.25))
    height = int((index // 4) * 100)

    img.paste(bonus_image, (width, height))

    