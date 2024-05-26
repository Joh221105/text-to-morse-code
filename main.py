from tkinter import *
import pygame
import time

morse_text_translation = {
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
}

# Initialize tkinter 
root = Tk()
root.title('Morse Code Generator')
root.minsize(width=1000, height=1000)

# Initialize Pygame 
pygame.mixer.init()

instruction_label = Label(text='Enter your message!', font=("Arial", 20))
instruction_label.pack(pady= 100)

entry = Entry(width=50, font=("Arial", 15))
entry.pack()

# Define the placeholder text
placeholder_text = "Enter your message!"

# Insert the placeholder text into the Entry widget
entry.insert(0, placeholder_text)

# Add an event handler to remove the placeholder text when the Entry widget is clicked
def on_click(event):
    if entry.get() == placeholder_text:
        entry.delete(0, END)

entry.bind("<Button-1>", on_click)

morse_code_result = Label(text="", font=("Arial", 30), wraplength=750)
morse_code_result.pack(pady=100)

morse_list = []
audio_button_created = False
audio_files =[]

# Makes sure that the user input contains only letters and spaces
def entry_validation(event=None):

    user_input = entry.get().strip().lower()
    if all(char.isalpha() or char.isspace() for char in user_input):
        translate(user_input.split(), user_input)  # Split the input by spaces and passes the list to translate function
    else:
        instruction_label.config(text="Please enter only letters and spaces.")

# using the dictionary, user input is translated into morse code and displayed using a label, also creates a play message button
def translate(user_input_list, user_input):
    global audio_button_created
    morse_list = []
    for word in user_input_list:
        for x in range(len(word)):
            morse_list.append(morse_text_translation[word[x]])
        if not word == user_input_list[-1]:
            morse_list.append('/')
    morse_code_result.config(text=f'{"  ".join(morse_list)}')

    audio_files.append([f"text-to-morse-code/audio/{letter}.mp3" if letter != " " else "text-to-morse-code/audio/space.mp3" for letter in user_input])
    
    if not audio_button_created:
        audio_button = Button(text="Play message", font=("Arial", 15), command=lambda:play_user_message(user_input))
        audio_button.pack()
        audio_button_created = True

# translates generated morse code into audio output
def play_user_message(user_input):
    global audio_files

    if len(audio_files) == 2:
        audio_files.pop(0)
        for audio_file_list in audio_files:
            for audio_file in audio_file_list:
                play_audio(audio_file)
                time.sleep(0.1)  # Add a small delay between letters
    else:
        for audio_file_list in audio_files:
            for audio_file in audio_file_list:
                play_audio(audio_file)
                time.sleep(0.1)  

# loads and plays the audio file
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)  
    pygame.mixer.music.play()  
    while pygame.mixer.music.get_busy(): # Keep the program running while the audio is playing
        time.sleep(0.1)

entry.bind("<Return>", entry_validation)


root.mainloop()