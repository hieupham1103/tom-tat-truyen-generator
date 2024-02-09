from moviepy.editor import *
from gtts import gTTS
import urllib.request
import os
import shutil
from time import sleep
import requests
from auth_token import auth_token
import io
from PIL import Image
import math


# API_URL = "https://api-inference.huggingface.co/models/CompVis/stable-diffusion-v1-4"
# API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": f"Bearer {auth_token}"}

def get_image(prompt):
    payload = {
        "inputs": f"{prompt}",
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


language = 'vi'
ouput_dir = "./output/"
list_part_output = []

def make_part(id: str, prompt: str):
    print(f"=======PART {id}=======")
    print(prompt)
    part_dir = f"{ouput_dir}part-{id}/"
    if (os.path.isdir(part_dir)) == False:
        os.mkdir(part_dir)
    generate_voice(part_dir, prompt)
    generate_image(part_dir, prompt)
    combine_audio(part_dir)
    
def generate_voice(part_dir: str, prompt: str):
    print("=generate voice=")
    output = gTTS(text = prompt, lang = language, slow = False)
    output.save(f"{part_dir}audio.mp3")
    print("done!!")
    
def generate_image(part_dir: str, prompt: str):
    print("=generate image=")
    prompt = "generate a image with anime style about this story \"" + prompt + "\""
    for x in range(0, 20):
        try:
            print(f"Try: {x}")
            img = get_image(prompt)
            Image.open(io.BytesIO(img)).save(f"{part_dir}img.png")
            print("done!!")
            return
        except:
            print("failed")
            pass

def combine_audio(part_dir: str, fps=30): 
    audio_background = AudioFileClip(f"{part_dir}audio.mp3")
    my_clip = ImageClip(f"{part_dir}img.png").set_duration(audio_background.duration)
    final_clip = my_clip.set_audio(audio_background)
    
    list_part_output.append(final_clip)

def make_parts(final_dir: str):
    content = open(final_dir + "story.txt", "r", encoding="utf8").read()
    content = content.split('.')

    current_part = ""
    part_count = 0

    try:
        shutil.rmtree("./output/")
    except:
        pass
    try:  
        os.mkdir("./output")
    except:
        pass

    for sentence in content:
        current_part += sentence + "."
        
        if len(current_part) >= 100:
            current_part = current_part.replace('\n', "")
            make_part(part_count, current_part)
            current_part = ""
            part_count += 1
            # break

def combine_video(final_dir: str):
    combined = concatenate_videoclips(list_part_output, method="compose")

    combined.write_videofile(final_dir + "output.mp4", fps=24)

def add_music(final_dir: str):
    video = VideoFileClip(final_dir + "output.mp4")
    music = AudioFileClip("./bg-music.mp3")
    final_music = music
    while final_music.duration < video.duration:
        final_music = concatenate_audioclips([final_music, music])
    video.audio = CompositeAudioClip([video.audio, final_music])
    video.write_videofile(final_dir + "output-audio.mp4")



def make_video(final_dir: str):
    list_part_output = [] 
    make_parts(final_dir)
    # print(list_part_output)
    combine_video(final_dir)
    add_music(final_dir)


list_chaps = os.listdir("./final")

for chap in list_chaps:
    make_video(f"./final/{chap}/")