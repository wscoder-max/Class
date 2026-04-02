class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    
    def __str__(self):
        return self.word + '(' + self.meaning + ')'

flash = []

while True:
    word = input("Enter the word you want to add to your flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))

    cont = input("Do you want to add another word? (y/n): ")
    if cont == "y":
        continue
    elif cont == "n":   
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        break

for card in flash:
    print(card)