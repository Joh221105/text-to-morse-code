from tkinter import *

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

root = Tk()
root.title('Morse Code Generator')
root.minsize(width=1000, height=1000)

instruction_label = Label(text='Enter your message!', font=("Arial", 20))
instruction_label.pack(pady= 100)

entry = Entry(width=50, font=("Arial", 15))
entry.pack()

morse_code_result = Label(text="", font=("Arial", 30), wraplength=750)
morse_code_result.pack(pady=100)

morse_list = []
audio_button_created = False

def entry_validation(event=None):

    user_input = entry.get().strip().lower()
    if all(char.isalpha() or char.isspace() for char in user_input):
        translate(user_input.split())  # Split the input by spaces and passes the list to translate function
    else:
        instruction_label.config(text="Please enter only letters and spaces.")

def translate(user_input_list):
    global audio_button_created
    for word in user_input_list:
        for x in range(len(word)):
            morse_list.append(morse_text_translation[word[x]])
        if not word == user_input_list[-1]:
            morse_list.append('/')
    morse_code_result.config(text=f'{"  ".join(morse_list)}')
    if not audio_button_created:
        audio_button = Button(text="Play message", font=("Arial", 15), command=play_audio)
        audio_button.pack()
        audio_button_created = True

def play_audio():
    pass

entry.bind("<Return>", entry_validation)


root.mainloop()