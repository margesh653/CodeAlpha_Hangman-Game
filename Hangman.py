import random

def play_hangman():
    # Predefined list of 5 words
    words = ["python", "robotics", "arduino", "sensor", "coding"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    attempts_left = 6
    
    print("--- Welcome to Hangman! ---")
    
    while attempts_left > 0:
        # Display the word with underscores for unguessed letters
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"\nWord: {display_word}")
        print(f"Attempts remaining: {attempts_left}")
        
        # Check if user won
        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word_to_guess)
            break
            
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
            
        guessed_letters.append(guess)
        
        # Check if guess is correct
        if guess in word_to_guess:
            print(f"Good job! '{guess}' is in the word.")
        else:
            attempts_left -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            
    if attempts_left == 0:
        print("\nGame Over! The word was:", word_to_guess)

# Run the game
if __name__ == "__main__":
    play_hangman()