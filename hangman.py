import random

def choose_word():
    categories = {
        "Fruit": ["apple", "banana", "kiwi", "grapes", "orange", "pineapple", "mango", "strawberry", "watermelon", "papaya"],
        "Profession": ["police", "teacher", "doctor", "student", "cleaner", "plumber", "builder", "engineer", "lawyer", "nurse"],
        "Vehicle": ["bicycle", "scooter", "ferry", "plane", "ship", "car", "bus", "train", "truck", "helicopter"],
        "Country": ["india", "canada", "brazil", "germany", "france", "japan", "italy", "australia", "mexico", "norway"],
        "Animal": ["tiger", "elephant", "lion", "giraffe", "kangaroo", "rabbit", "panda", "zebra", "fox", "monkey"],
        "Color": ["red", "blue", "green", "yellow", "purple", "orange", "black", "white", "violet", "indigo"],
        "Object": ["bottle", "laptop", "mirror", "chair", "pencil", "notebook", "blanket", "camera", "remote", "window"],
        "Body Part": ["heart", "lungs", "brain", "kidney", "stomach", "finger", "ankle", "elbow", "shoulder", "tongue"]
    }
    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])
    return word, category

def display_hangman(life):
    stages = [
        """
        _______|
        |     |
        |     O
        |    /|\\
        |    / \\
        |
        ========== """,
        """
        _______|
        |     |
        |     O
        |    /|\\
        |    /
        |
        ========== """,
        """
        _______|
        |     |
        |     O
        |    /|\\
        |
        |
        ========== """,
        """
        _______|
        |     |
        |     O
        |    /|
        |
        |
        ========== """,
        """
        _______|
        |     |
        |     O
        |     |
        |
        |
        ========== """,
        """
        _______|
        |     |
        |     O
        |
        |
        |
        ========== """,
        """
        _______|
        |     |
        |
        |
        |
        |
        ========== """
    ]
    print(stages[6 - life])

def display_saved():
    print("""
      \\O/     YOU SAVED HIM!
       |      
      / \\     
     SAFE AND SOUND!
====================
""")

def play_game():
    word, category = choose_word()
    guess = ['_'] * len(word)
    blanks = len(word)
    life = 6

    print("🎮 Welcome to Hangman!")
    print(f"💡 Hint: The word belongs to the category **{category.upper()}**")
    print("Guess the word: ", " ".join(guess))

    while life > 0 and blanks > 0:
        letter = input("\nEnter your guess: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("⚠️  Enter a single valid letter.")
            continue

        if letter in guess:
            print(f"✅ You've already guessed '{letter}'. Try another letter.")
            continue

        count = 0
        for i in range(len(word)):
            if word[i] == letter and guess[i] == '_':
                guess[i] = letter
                blanks -= 1
                count += 1

        if count == 0:
            life -= 1
            print(f"❌ '{letter}' is not in the word.")
        else:
            print(f"✅ Good guess! '{letter}' is in the word.")

        print("Current word: ", " ".join(guess))
        print(f"Lives left: {life}")
        display_hangman(life)

    if blanks == 0:
        display_saved()
        print("🎉 Yes, the word is:", word.capitalize())
    else:
        print("\n💀 GAME OVER. The man got hanged!")
        display_hangman(0)
        print("The correct word was:", word.capitalize())

# Run the game
play_game()
