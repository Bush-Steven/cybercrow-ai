from PIL import Image, ImageDraw

img = Image.new("RGB",(1400,1400),"black")
draw = ImageDraw.Draw(img)

draw.text((300,600),"CyberCrow\nCyber Intelligence",fill="white")

img.save("cover.jpg")
