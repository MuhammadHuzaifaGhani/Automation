import subprocess

output_video = "squat_slideshow.mp4"

ffmpeg_cmd = [
    "ffmpeg",
    "-y",

    "-i", "slides/slide1.png",
    "-i", "slides/slide2.png",
    "-i", "slides/slide3.png",
    "-i", "slides/slide4.png",
    "-i", "slides/slide5.png",
    "-i", "slides/slide6.png",

    "-filter_complex",
    """
    [0:v]scale=1080:1350,pad=1080:1920:0:(oh-ih)/2:black,setsar=1,format=rgba[v0];
    [1:v]scale=1080:1350,pad=1080:1920:0:(oh-ih)/2:black,setsar=1,format=rgba[v1];
    [2:v]scale=1080:1350,pad=1080:1920:0:(oh-ih)/2:black,setsar=1,format=rgba[v2];
    [3:v]scale=1080:1350,pad=1080:1920:0:(oh-ih)/2:black,setsar=1,format=rgba[v3];
    [4:v]scale=1080:1350,pad=1080:1920:0:(oh-ih)/2:black,setsar=1,format=rgba[v4];
    [5:v]scale=1080:1350,pad=1080:1920:0:(oh-ih)/2:black,setsar=1,format=rgba[v5];

    [v0][v1]xfade=transition=fade:duration=0.5:offset=1[v01];
    [v01][v2]xfade=transition=fade:duration=0.5:offset=2[v02];
    [v02][v3]xfade=transition=fade:duration=0.5:offset=3[v03];
    [v03][v4]xfade=transition=fade:duration=0.5:offset=4[v04];
    [v04][v5]xfade=transition=fade:duration=0.5:offset=5
    """,

    "-t", "7",
    "-c:v", "libx264",
    "-pix_fmt", "yuv420p",
    "-movflags", "+faststart",
    output_video
]

subprocess.run(ffmpeg_cmd)

print("🎬 Video created successfully (1080x1920)")