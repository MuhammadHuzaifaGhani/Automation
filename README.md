# 🟦 Fitness Slideshow Automation

This project automatically generates **Instagram‑ready fitness slideshow videos** using **Streamlit + Python**.

You can:

* Enter **editable text per post** via a Streamlit UI
* Auto‑generate **6 slides (1080×1350 – 4:5)**
* Convert slides into a **vertical video (1080×1920 – Reels/Shorts)**
* Apply smooth **transitions between slides**

---

## 📁 Project Structure

```
Automation/
│
├── app.py                 # Streamlit UI
├── generate_slides.py     # Creates slides (PNG)
├── make_video.py          # Converts slides → video
├── input.json             # Auto‑generated text data
│
├── slides/                # Generated slide images
│   ├── slide1.png
│   ├── slide2.png
│   └── ...
│
├── assets/
│   ├── bg_hook.png        # Hook background
│   ├── bg_exercise.png    # Exercise background (slides 2–5)
│   ├── bg_cta.png         # CTA background
│   └── font.ttf           # Font file
│
└── squat_slideshow.mp4    # Final output video
```

---

## 🎯 Slide Rules

| Slide | Purpose   | Background        | Text Color           |
| ----- | --------- | ----------------- | -------------------- |
| 1     | Hook      | `bg_hook.png`     | Custom (as provided) |
| 2–5   | Exercises | `bg_exercise.png` | As per design        |
| 6     | CTA       | `bg_cta.png`      | Custom               |

* **Slide size:** `1080 × 1350 (4:5)`
* **Video size:** `1080 × 1920 (9:16)`

---

## ⚙️ Installation

### 1️⃣ Install Python

Make sure **Python 3.10+** is installed.

Check:

```bash
python --version
```

---

### 2️⃣ Install Required Libraries

```bash
python -m pip install streamlit pillow moviepy
```

---

### 3️⃣ Install FFmpeg

FFmpeg is required for video generation.

**Windows:**

* Download FFmpeg from [https://ffmpeg.org](https://ffmpeg.org)
* Extract it
* Add `ffmpeg/bin` to **System PATH**

Verify:

```bash
ffmpeg -version
```

---

## 🚀 How to Run the Project

From the project folder:

```bash
python -m streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧠 Workflow

1. Enter **Hook, Exercises, CTA text** in Streamlit UI
2. Click **Generate Slideshow**
3. Slides are created → `slides/`
4. Slides are converted into video
5. Final output → `squat_slideshow.mp4`

---

## 📦 Output

* ✅ Instagram Reels
* ✅ YouTube Shorts
* ✅ TikTok videos

Fully automated & reusable 💪

---

## 🛠 Troubleshooting

### Streamlit command not found

Use:

```bash
python -m streamlit run app.py
```

### Blank Streamlit screen

* Stop terminal (`Ctrl + C`)
* Run again
* Ensure **no Python errors** in terminal

---

## 📌 Notes

* Replace background images freely
* Change fonts by replacing `font.ttf`
* Text is fully editable per post

---

## ✨ Future Enhancements

* Music support
* Auto captions
* Multiple post batch generation
* Canva‑style themes

---

## 👨‍💻 Author

**Muhammad Huzaifa Ghani**
Automation • Generative AI • Content Systems

---

⭐ If this helped you, star the repo and build more content faster!
