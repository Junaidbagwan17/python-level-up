# here we are extracting colors from the image
# the colors will be in rgb format

import colorgram as c

colors = c.extract("dot.jpg", 20)

rgb_colors = []
for col in colors:
    r = col.rgb.r
    g =col.rgb.g
    b = col.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)
print(rgb_colors)

# colors = [
#     (226, 231, 236),
#     (58, 106, 148),
#     (224, 200, 109),
#     (134, 84, 58),
#     (223, 138, 62),
#     (196, 145, 171),
#     (234, 226, 204),
#     (224, 234, 230),
#     (141, 178, 204),
#     (139, 82, 105),
#     (209, 90, 69),
#     (188, 80, 120),
#     (68, 105, 90),
#     (237, 225, 233),
#     (134, 182, 136),
#     (133, 133, 74),
#     (63, 156, 92),
#     (48, 156, 194),
#     (183, 192, 201),
#     (214, 177, 191)
# ]
