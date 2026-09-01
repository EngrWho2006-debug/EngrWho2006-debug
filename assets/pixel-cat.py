from PIL import Image, ImageDraw
import os

os.makedirs("assets", exist_ok=True)

frames = []

for frame in range(4):

    img = Image.new("RGBA", (160, 120), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Walking animation
    offset = [0, 2, 0, -2][frame]

    # Tail
    draw.rectangle((25, 65 + offset, 35, 75 + offset), fill="#888888")
    draw.rectangle((20, 55 + offset, 30, 65 + offset), fill="#888888")

    # Body
    draw.rectangle((55, 60 + offset, 110, 95 + offset), fill="#888888")

    # Head
    draw.rectangle((50, 30 + offset, 115, 70 + offset), fill="#999999")

    # Ears
    draw.polygon(
        [(50, 35 + offset), (50, 15 + offset), (70, 30 + offset)],
        fill="#999999"
    )

    draw.polygon(
        [(95, 30 + offset), (115, 15 + offset), (115, 35 + offset)],
        fill="#999999"
    )

    # Eyes
    draw.rectangle((65, 45 + offset, 71, 51 + offset), fill="black")
    draw.rectangle((94, 45 + offset, 100, 51 + offset), fill="black")

    # Nose
    draw.rectangle((80, 55 + offset, 86, 61 + offset), fill="#444444")

    # Legs
    if frame % 2 == 0:
        draw.rectangle((65, 90 + offset, 75, 108 + offset), fill="#777777")
        draw.rectangle((95, 95 + offset, 105, 113 + offset), fill="#777777")
    else:
        draw.rectangle((65, 95 + offset, 75, 113 + offset), fill="#777777")
        draw.rectangle((95, 90 + offset, 105, 108 + offset), fill="#777777")

    frames.append(img)

frames[0].save(
    "assets/pixel-cat.gif",
    save_all=True,
    append_images=frames[1:],
    duration=180,
    loop=0,
    disposal=2
)

print("Pixel cat created!")
