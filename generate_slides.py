import json
from PIL import Image, ImageDraw, ImageFont

# ---------------- CONFIG ----------------
WIDTH, HEIGHT = 1080, 1350

FONT_BIG_SIZE = 80
FONT_MED_SIZE = 50

FONT_PATH = "assets/font.ttf"

BG_HOOK = "assets/bg_hook.png"
BG_EX = "assets/bg_exercise.png"
BG_CTA = "assets/bg_cta.png"

OUTPUT_DIR = "slides"

# ---------------- LOAD DATA ----------------
with open("input.json", "r") as f:
    data = json.load(f)

# ---------------- LOAD FONT ----------------
font_big = ImageFont.truetype(FONT_PATH, FONT_BIG_SIZE)
font_med = ImageFont.truetype(FONT_PATH, FONT_MED_SIZE)

# ---------------- SLIDE DATA ORDER ----------------
slides = [
    ("hook", BG_HOOK, data["hook"]),
    ("ex1", BG_EX, data["exercises"][0]),
    ("ex2", BG_EX, data["exercises"][1]),
    ("ex3", BG_EX, data["exercises"][2]),
    ("ex4", BG_EX, data["exercises"][3]),
    ("cta", BG_CTA, data["cta"]),
]

# ---------------- CREATE SLIDES ----------------
for i, (_, bg_path, content) in enumerate(slides, start=1):
    bg = Image.open(bg_path).resize((WIDTH, HEIGHT))
    draw = ImageDraw.Draw(bg)

    # TITLE
    draw.text(
        (80, 220),
        content["title"],
        font=font_big,
        fill="white"
    )

    # SUBTITLE
    draw.text(
        (80, 360),
        content["subtitle"],
        font=font_med,
        fill="#c7d2fe"
    )

    # FOOTER (ONLY FOR EXERCISES)
    if "footer" in content:
        draw.text(
            (80, 1120),
            content["footer"],
            font=font_med,
            fill="white"
        )

    bg.save(f"{OUTPUT_DIR}/slide{i}.png")

print("✅ Slides generated successfully (1080x1350)")