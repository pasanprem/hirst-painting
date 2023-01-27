import colorgram

colors = colorgram.extract('image.jpg', 6)

print(type(colors))

i = 0
color_list = []
for i in colors:
    rgb = i.rgb
    color_tup = (rgb.r, rgb.g, rgb.b)
    color_list.append(color_tup)

print(color_list)