import os

for fichier in os.listdir("images_bot/emote_stuff"):
    new_name = fichier.replace(".webp",".png")
    os.rename("images_bot/emote_stuff/" + fichier, "images_bot/emote_stuff/" + new_name)