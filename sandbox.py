import pygame
import time

def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)  # Load the audio file
    pygame.mixer.music.play()  # Play the audio
    while pygame.mixer.music.get_busy():
        # Keep the program running while the audio is playing
        time.sleep(0.1)

# Initialize Pygame (should be done once at the beginning of your script)
pygame.mixer.init()

# Example usage
audio_file = "text-to-morse-code/audio/a.mp3"  # Replace with the path to your audio file
play_audio(audio_file)