import os

for fichier in os.listdir("images_bot/images_armes"):
    new_fichier = fichier.replace(" ","_")
    os.rename(f"images_bot/images_armes/{fichier}", f"images_bot/images_armes/{new_fichier}")