class BMW():
    def fuel_type(self):
        print("BMW cars run on petrol.")
    
    def max_speed(self):
        print("BMW cars have a maximum speed of 155 mph or 250 km/h.")
    
class Ferrari():
    def fuel_type(self):
        print("Ferrari cars run on petrol.")
    
    def max_speed(self):
        print("Ferrari cars have a maximum speed of 211 mph or 340 km/h.")

obj_bmw = BMW()
obj_ferrari = Ferrari()

for car in (obj_bmw, obj_ferrari):
    car.fuel_type()
    car.max_speed()