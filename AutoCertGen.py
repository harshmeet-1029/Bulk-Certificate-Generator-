from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('list.csv')
font = ImageFont.truetype('arial.ttf',60)
font1 = ImageFont.truetype('arial.ttf',35)
for index,j in df.iterrows():
    img = Image.open('certificate.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(170,507),text='{}'.format(j['name']),fill=(247,111,23),font=font)
    draw.text(xy=(539,739),text='{}'.format(j['date']),fill=(0,0,0),font=font1)
    img.show()
    img.save('pictures/{}.jpg'.format(j['name']))
