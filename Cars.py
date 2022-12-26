class cars:
    def __init__(self, name, hp, topspeed, seats, price):
        self.name = name
        self.hp = hp
        self.topspeed = topspeed
        self.seats = seats
        self.price = price

    def __repr__(self):
        return f"{self.name}, Horsepower: {self.hp}, Top Speed: {self.topspeed}, Number of Seats: {self.seats}, MSRP: {self.price}"
 
first = cars("Chevrolet S10", 120, 100, 2, 13961)
second = cars("Toyota Chaser", 135,110 , 4, 16221)
third = cars("Saturn SL1", 100, 110, 4, 11485)
fourth = cars("Kia Forte",147 ,160 ,4 , 19100)
fifth = cars("Mazda Miata", 116, 140, 2, 15896)

print(first)
print(second)
print(third)
print(fourth)
print(fifth)

