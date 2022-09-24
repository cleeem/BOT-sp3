from PIL import Image

img2 = Image.open("images_bot/emote_stuff/blanc_original.png").resize(size=(384,288))
img2.save("test.png")