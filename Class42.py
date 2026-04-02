class WordReverser:
    def __init__(self):
        self.__text = ""

    def set_text_from_input(self):
        self.__text = input("Enter a string: ")

    def get_text(self):
        return self.__text

    def reverse_words(self):
        words = self.__text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

wr = WordReverser()
wr.set_text_from_input()
print("Reversed:", wr.reverse_words())
