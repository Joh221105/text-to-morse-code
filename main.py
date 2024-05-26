morse_translation = {
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


morse_list = []

def get_user_input():
    while True:
        try:
            user_input = input("Enter the message you want to encrypt: ")
            # Check if input consists only of letters and/or spaces
            if all(char.isalpha() or char.isspace() for char in user_input):
                return user_input.split()  # Split the input by spaces and return as a list
            else:
                print("Please enter only letters and spaces.")
        except ValueError:
            print("An error occurred. Please try again.")

word_list = get_user_input()

for word in word_list:
    for x in range(len(word)):
        morse_list.append(morse_translation[word[x]])
    if not word == word_list[-1]:
        morse_list.append('/')

print(' '.join(morse_list))