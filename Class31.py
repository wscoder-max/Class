class dog:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

dog1 = dog("German Shepherd", "Black")
dog2 = dog("Labrador", "Yellow")

print("Dog 1: " + dog1.breed + ", " + dog1.color)
print("Dog 2: " + dog2.breed + ", " + dog2.color)