class vehicle():
    def __init__(self, fare):
        self.fare = fare

class bus(vehicle):
    def __init__(self, fare):
        super().__init__(fare)

busFare = bus(100)
print("Bus fare is:", busFare.fare)