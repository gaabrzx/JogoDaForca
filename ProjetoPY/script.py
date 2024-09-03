import random

def get_word():
    words = ["python", "java", "kotlin", "javascript"]
    return random.choice(words)

def play_hangman():
    word = get_word()
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    while attempts > 0 and "_" in guessed_word:
        print(" ".join(guessed_word))
        print(f"Tentativas restantes: {attempts}")
        guess = input("Adivinhe uma letra: ").lower()

        if guess in guessed_letters:
            print("Você já tentou essa letra.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1

    if "_" not in guessed_word:
        print(f"Parabéns! Você adivinhou a palavra: {word}")
    else:
        print(f"Você perdeu! A palavra era: {word}")

play_hangman()
