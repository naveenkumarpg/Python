import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('hirst.webp', 30)
rgb_colors =[]
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r,g,b))

print(rgb_colors)
