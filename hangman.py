import random

def choose_word():
    words = ["hima", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    return random.choice(words)

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_completion = "_" * len(word)
    guessed = False
    
    print("Welcome to Hangman!")
    print(f"The word to guess has {len(word)} letters.")
    print_display(incorrect_guesses, max_incorrect_guesses, word_completion, guessed_letters)
    
    while not guessed and incorrect_guesses < max_incorrect_guesses:
        guess = input("Please guess a letter: ").lower()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You've already guessed '{guess}'. Try again.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                incorrect_guesses += 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! '{guess}' is in the word.")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                
                if "_" not in word_completion:
                    guessed = True
        else:
            print("Invalid guess. Please enter a single letter.")
        
        print_display(incorrect_guesses, max_incorrect_guesses, word_completion, guessed_letters)
    
    if guessed:
        print("Congratulations! You guessed the word correctly.")
    else:
        print(f"Sorry, you ran out of guesses. The word was '{word}'.")

def print_display(incorrect_guesses, max_incorrect_guesses, word_completion, guessed_letters):
    print(f"\nIncorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
    print("Guessed letters:", " ".join(guessed_letters))
    print("Word to guess:", word_completion)
    print("\n---------------------\n")

hangman()
