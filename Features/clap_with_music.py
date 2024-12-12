import os
import pygame
import random
from pygame import mixer
from Features.clap_d import *

def play_random_music(folder_path):
    music_files = [file for file in os.listdir(folder_path) if file.endswith(('.mp3','.wav','.ogg','.flac'))]
    
    if not music_files:
        print("No music found in the specified folder !!")
        return
    
    selected_music = random.choice(music_files)
    music_path = os.path.join(folder_path, selected_music)
    
    try:
        pygame.init()
        mixer.init()
        
        mixer.music.load(music_path)
        mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        mixer.music.stop()
        mixer.quit()
        
    except Exception as e:
        print(f"Error playing music : {e}")
    
def clap_to_music():
    while True:
        tt = TapTester()
        clap_count = 0
        
        while True:
            if tt.listen():
               clap_count += 2
               
               if clap_count == REQUIRED_CLAP:
                   play_random_music(r"") 
                   break
        