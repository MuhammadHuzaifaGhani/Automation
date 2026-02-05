import streamlit as st
import subprocess
import json
import os
from PIL import Image

st.set_page_config(page_title="SlideShow Automation", layout="centered")

st.title("🟦 Fitness Slideshow Generator")

# -------- HOOK --------
st.subheader("Slide 1 — Hook")

hook_title = st.text_input("Hook Title", "WRONG SQUAT ❌").strip()
hook_sub = st.text_input("Hook Subtitle", "This wrecks your knees & back").strip()

# -------- EXERCISES --------
st.subheader("Slides 2–5 — Exercises")

exercises = []
for i in range(1, 5):
    st.markdown(f"### Exercise {i}")
    title = st.text_input(f"Title {i}", f"Exercise {i}").strip()
    subtitle = st.text_input(f"Subtitle {i}", "Short explanation").strip()
    footer = st.text_input(f"Sets/Reps {i}", "3 x 10 reps").strip()

    exercises.append({
        "title": title,
        "subtitle": subtitle,
        "footer": footer
    })

# -------- CTA --------
st.subheader("Slide 6 — CTA")

cta_title = st.text_input("CTA Title", "YOUR TURN").strip()
cta_sub = st.text_input("CTA Subtitle", "Start training them").strip()

# -------- SAVE DATA FUNCTION --------
def save_input_json():
    slide_data = {
        "hook": {
            "title": hook_title,
            "subtitle": hook_sub
        },
        "exercises": exercises,
        "cta": {
            "title": cta_title,
            "subtitle": cta_sub
        }
    }

    with open("input.json", "w") as f:
        json.dump(slide_data, f, indent=4)

# -------- PREVIEW BUTTON --------
if st.button("👀 Preview Slides"):
    save_input_json()

    subprocess.run(["python", "generate_slides.py"])

    st.success("Slides generated. Preview below:")

    for i in range(1, 7):
        slide_path = f"slides/slide{i}.png"
        if os.path.exists(slide_path):
            image = Image.open(slide_path)
            st.image(image, caption=f"Slide {i}", use_column_width=True)

# -------- GENERATE VIDEO BUTTON --------
if st.button("🎬 Generate Video"):
    save_input_json()

    subprocess.run(["python", "generate_slides.py"])
    subprocess.run(["python", "make_video.py"])

    if os.path.exists("squat_slideshow.mp4"):
        st.success("✅ Video created successfully!")
        st.video("squat_slideshow.mp4")
    else:
        st.error("❌ Video generation failed. Check terminal.")