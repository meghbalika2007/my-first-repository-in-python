import random

stages = [
    """+---+

        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =========""",
    """ 
        +---+

      |   |
      O   |
     /|\\  |
     /    |
          |
    =========""",
    """
    +---+

      |   |
      O   |
     /|\\  |
          |
    =========""",
    """
        +---+
    
      |   |
      O   |
     /|   |
          |
    =========""",
    """
      +---+
    
      |   |
      O   |
    
      |   |
          |
    =========""",
    """+---+
    
      |   |
      O   |
          |
          |
          |
    =========""",
    """+---+

      |   |
          |
          |
          |
          |
    =========""",
]

# Typo fixed in "abracadabra" just in case, feel free to change back!
word_list = ["Bicycle",
    "Whisper",
    "Avalanche",
    "Teapot",
    "Galaxy",
    "Laughter",
    "Submarine",
    "Cactus",
    "Velocity",
    "Orchestra",
    "Feather",
    "Pyramid",
    "Marathon",
    "Jacket",
    "Lantern",
    "Horizon",
    "Magnet",
    "Symphony",
    "Umbrella",
    "Tornado"]
lives = 6
chosen_word = random.choice(word_list)

# this the  placeholder 
word_length=len(chosen_word)

for position in range(word_length):
  placeholder+=" _"
print("Word to guess:", placeholder)

gameover = False
correct_letters = []

while not gameover:
    guess = input("Guess a letter: ").lower()
    
#to make sure they only put one alphabet per charecter
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Build the display string continuously
    display_list = []
    
    if guess in chosen_word and guess not in correct_letters:
        correct_letters.append(guess)

    for letter in chosen_word:
        if letter in correct_letters:
            display_list.append(letter)
        else:
            display_list.append("_")

    # Join with spaces for clean command line reading
    display = " ".join(display_list)
    print(display)

    # Check if the guess is wrong
    if guess not in chosen_word:
        lives -= 1
        print("***Wrong guess!***",lives," You have  lives left.")
        if lives == 0:
            gameover = True  
            # Fixed variable name spelling here
            print("!!!You lose!!!. The word was:" ,chosen_word)

    # Check if the player won
    if "_" not in display_list:
        gameover = True
        print("You win!")

    # Print the current stage of the hangman
    print(stages[lives])
